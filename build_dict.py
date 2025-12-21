import codecs
import glob
import json
import os
import re
import sys
from pathlib import Path

import yaml


class _NoDuplicateKeysLoader(yaml.BaseLoader):
    def construct_mapping(self, node, deep=False):
        mapping = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in mapping:
                raise ValueError("Duplicate key in YAML block: {}".format(key))
            mapping[key] = self.construct_object(value_node, deep=deep)
        return mapping


class DictBuilder(object):
    def get_dict_from_md(self, md_file_path):
        with codecs.open(md_file_path, "r", "utf-8") as md_file:
            md_lines = md_file.readlines()
            strokes_dict = {}

            for block in self._iter_yaml_blocks(md_lines):
                if not block.strip():
                    continue
                block_dict = self._load_yaml_block(block, md_file_path)
                for strokes, translation in block_dict.items():
                    if strokes.startswith("(DELETED)"):
                        continue
                    if strokes.startswith("(UPDATED)"):
                        strokes = strokes[len("(UPDATED)") :].strip()
                    if strokes in strokes_dict:
                        print(
                            "WARNING: defined more than once: " + strokes + " >>> ABORT"
                        )
                        continue
                    strokes_dict[strokes] = translation

        return strokes_dict

    def _iter_yaml_blocks(self, md_lines):
        in_block = False
        use_block = False
        fence = ""
        fence_re = re.compile(r"^(`{3,})(.*)$")
        buffer_lines = []

        for raw_line in md_lines:
            line = raw_line.rstrip("\n")
            if not in_block:
                match = fence_re.match(line)
                if not match:
                    continue
                fence = match.group(1)
                info = match.group(2).strip()
                lang = info.split()[0].lower() if info else ""
                use_block = lang in ("", "yaml")
                in_block = True
                buffer_lines = []
                continue

            if line.strip() == fence:
                if use_block:
                    yield "\n".join(buffer_lines)
                in_block = False
                use_block = False
                fence = ""
                buffer_lines = []
                continue

            if use_block:
                buffer_lines.append(line)

    def _load_yaml_block(self, block, md_file_path):
        try:
            data = yaml.load(block, Loader=_NoDuplicateKeysLoader)
        except ValueError as exc:
            raise ValueError("{} in {}".format(exc, md_file_path))
        if data is None:
            return {}
        if not isinstance(data, dict):
            raise ValueError("Expected a YAML mapping in {}".format(md_file_path))
        return {str(k): str(v) for k, v in data.items()}

    def build_from_md(self, md_file_path):
        strokes_dict = self.get_dict_from_md(md_file_path)
        self.write_dict(strokes_dict, md_file_path)

    def write_dict(self, strokes_dict, md_file_path):
        md_path = Path(md_file_path)
        generated_target_path = md_path.parent / "generated"
        if not os.path.exists(generated_target_path):
            os.makedirs(generated_target_path)
        json_target_path = generated_target_path / md_path.with_suffix(".json").name

        with codecs.open(json_target_path, "w", "utf-8") as json_file:
            json_string = json.dumps(
                strokes_dict,
                ensure_ascii=False,
                sort_keys=True,
                indent=0,
                separators=(",", ": "),
            )

            json_file.write(json_string)

            # adds a new line at the end of the file because json.dump doesn't
            json_file.write("\n")

    def build_all_from_md(self, regex, print_files):
        for md_file_path in glob.iglob(regex, recursive=True):
            if print_files:
                print("building dict: " + md_file_path)
            self.build_from_md(md_file_path)


if __name__ == "__main__":
    stenodicts_root = sys.path[0]
    dict_builder = DictBuilder()
    dict_builder.build_all_from_md(stenodicts_root + "/*/*.md", print_files=True)
