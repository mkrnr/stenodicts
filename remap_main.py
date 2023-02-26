#!/usr/bin/env python3

import codecs
import json
import os
import sys

from build_dict import DictBuilder

ignored_files = ["modifier-keys.md"]


class MainRemapper(object):
    left_consonant_keys = ['Z', 'S', 'T', 'K', 'P', 'W', 'H', 'R']
    right_consonant_keys = ['F', 'R', 'P', 'B', 'L', 'G', 'T', 'S', 'D', 'Z']

    replace_dict = {}

    def __init__(self, specific_language_path):
        self.add_replacements_in_dir("common")
        self.add_replacements_in_dir(specific_language_path)

    def add_replacements_in_dir(self, directory):
        path = os.path.dirname(sys.argv[0])
        for file in os.listdir(os.path.join(path, directory)):
            if file.endswith(".md") and file not in ignored_files:
                self.add_replacement(os.path.join(path, directory, file))

    def remap(self, main_path, output_path):
        new_strokes_dict = {}
        with codecs.open(main_path, "r", "utf-8") as json_file:
            main_dict = json.load(json_file)
            print(len(main_dict))
            for key in main_dict:
                strokes = key.split("/")
                new_strokes = self.replace_strokes(strokes)
                new_strokes_string = '/'.join(new_strokes)
                if new_strokes_string != key and new_strokes_string in main_dict:
                    if main_dict[key] != main_dict[new_strokes_string]:
                        print('' + new_strokes_string + ':"' + main_dict[new_strokes_string] + '" --> "' + main_dict[
                            key] + '"')

                new_strokes_dict[new_strokes_string] = main_dict[key]

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with codecs.open(output_path, "w", "utf-8") as json_file:
            json_string = json.dumps(new_strokes_dict, ensure_ascii=False, sort_keys=True,
                                     indent=0, separators=(',', ': '))

            json_file.write(json_string)

            # adds a new line at the end of the file because json.dump doesn't
            json_file.write("\n")

    def replace_strokes(self, strokes):
        new_strokes = []
        for stroke in strokes:
            new_strokes.append(self.replace_stroke(stroke))
        return new_strokes

    def replace_stroke(self, stroke):
        if stroke in self.replace_dict:
            return self.replace_dict[stroke]
        else:
            return stroke

    def add_replacement(self, keys_path):
        dict_builder = DictBuilder()

        key_strokes_dict = dict_builder.get_dict_from_md(keys_path)
        for stroke_to_be_replaced in key_strokes_dict:
            self.replace_dict[stroke_to_be_replaced] = self.add_asterisk(stroke_to_be_replaced)

    def add_asterisk(self, stroke):
        if '-' in stroke:
            return stroke.replace('-', '*')
        new_stroke = ''
        saw_vowel = False
        for letter in stroke:
            if letter == "A" or letter == "O":
                saw_vowel = True
            elif letter in self.left_consonant_keys:
                if "*" not in new_stroke and saw_vowel:
                    new_stroke += "*"
            elif letter in self.right_consonant_keys or letter == "E" or letter == "U" and '*' not in new_stroke:
                new_stroke += "*"
            new_stroke += letter
        if '*' not in new_stroke:
            new_stroke += "*"

        return new_stroke


if __name__ == '__main__':
    main_path = sys.argv[1]
    specific_language_path = sys.argv[2]
    output_path = sys.argv[3]
    main_remapper = MainRemapper(specific_language_path)
    main_remapper.remap(main_path, output_path)
