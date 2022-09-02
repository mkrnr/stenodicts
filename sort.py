#!/usr/bin/env python3

import codecs
import collections
import glob
import json


class Sorter(object):

    def sort(self, json_file_path):
        with codecs.open(json_file_path, "r", "utf-8") as json_file:
            strokes = json.load(json_file)
            sorted_strokes = collections.OrderedDict(sorted(strokes.items()))
        with codecs.open(json_file_path, "w", "utf-8") as json_file:
            json.dump(sorted_strokes, json_file, ensure_ascii=False, sort_keys=True,
                      indent=0, separators=(',', ': '))
            # adds a new line at the end of the file because json.dump doesn't
            json_file.write("\n")

    def sort_all(self, regex, print_files):
        for json_file_path in glob.iglob(regex, recursive=True):
            if print_files:
                print("sorting: " + json_file_path)
            self.sort(json_file_path)


if __name__ == '__main__':
    sorter = Sorter()
    # sort all json files in any subfolder of this project
    sorter.sort_all("*/*.json", print_files=True)
