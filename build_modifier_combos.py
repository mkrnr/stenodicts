#!/usr/bin/env python3

import sys
from build_dict import DictBuilder


class ModifierCombosBuilder(object):

    def build(self, modifier_keys_path, keys_path):
        dict_builder = DictBuilder()
        
        key_strokes_dict = dict_builder.get_dict_from_md(keys_path)
        cleaned_key_strokes_dict = self.clean_key_strokes(key_strokes_dict)

        modifier_keys_dict = dict_builder.get_dict_from_md(modifier_keys_path)
        modifier_combos_dict = {}
        for modifier_key in modifier_keys_dict:
            print(modifier_key)
            modifier_combos_dict[modifier_key.replace("/?", "")] = "{#}"
            for key in cleaned_key_strokes_dict:
                inserted_modifier_key = modifier_key.replace("?", key)
                print(inserted_modifier_key)
                inserted_stroke = modifier_keys_dict[modifier_key].replace("?", cleaned_key_strokes_dict[key])
                print(inserted_stroke)
                modifier_combos_dict[inserted_modifier_key] = inserted_stroke
        dict_builder.write_dict(modifier_combos_dict, modifier_keys_path.replace("-keys", "-combos"))
    
    def clean_key_strokes(self, key_strokes_dict):
        cleaned_key_strokes_dict = {}

        for key in key_strokes_dict:
            stroke = key_strokes_dict[key]
            cleaned_stroke = stroke.replace("{#", "").replace("{", "").replace("}", "").replace("^", "")
            cleaned_key_strokes_dict[key] = cleaned_stroke

        return cleaned_key_strokes_dict


if __name__ == '__main__':
    stenodicts_root = sys.path[0]
    modifier_combos_builder = ModifierCombosBuilder()
    modifier_combos_builder.build(stenodicts_root + "/common/modifier-keys.md", stenodicts_root + "/common/keys.md")
