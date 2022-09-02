#!/usr/bin/env python3

import codecs
import glob
import json
import os
import sys
from pathlib import Path


class DictBuilder(object):

    def get_dict_from_md(self, md_file_path):
        with codecs.open(md_file_path, "r", "utf-8") as md_file:
            md_lines = md_file.readlines()
            strokes_dict = {}

            in_table = False
            for md_line in md_lines:

                if md_line.startswith("|--"):
                    in_table = True
                    continue
                if in_table and not md_line.startswith("|"):
                    in_table = False
                if in_table:
                    md_line = md_line.replace('\|', '{ESCAPED_PIPE}')
                    md_line_split = md_line.split('|')
                    md_line_split = [sub.replace('{ESCAPED_PIPE}', '|') for sub in md_line_split]
                    strokes = md_line_split[1].strip()
                    strokes = strokes.replace("\|", "|")
                    translation = md_line_split[len(md_line_split) - 2].strip()
                    translation = translation.replace("\*", "*")
                    if strokes in strokes_dict:
                        sys.exit("defined more than once: " + strokes + " >>> ABORT")
                    else:
                        strokes_dict[strokes] = translation

        return strokes_dict

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
            json_string = json.dumps(strokes_dict, ensure_ascii=False, sort_keys=True,
                                     indent=0, separators=(',', ': '))

            # replace redundantly escaped backslashes
            json_string = json_string.replace("\\\\", "\\")
            json_string = json_string.replace('\\"', '"')

            json_file.write(json_string)

            # adds a new line at the end of the file because json.dump doesn't
            json_file.write("\n")

    def build_all_from_md(self, regex, print_files):
        for md_file_path in glob.iglob(regex, recursive=True):
            if print_files:
                print("building dict: " + md_file_path)
            self.build_from_md(md_file_path)


if __name__ == '__main__':
    stenodicts_root = sys.path[0]
    dict_builder = DictBuilder()
    dict_builder.build_all_from_md(stenodicts_root + "/*/*.md", print_files=True)
