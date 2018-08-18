#!/usr/bin/env python3

import re

from git import Repo

from sort import Sorter

json_regex = r'.*/.*.json'
json_glob_pattern = '*/*.json'

sorter = Sorter()
# sort all json files in any subfolder of this project
sorter.sort_all(json_glob_pattern, print_files=False)

repo = Repo('.')

files_to_commit = []
for untracked_file in repo.untracked_files:
    if re.search(json_regex, str(untracked_file)):
        files_to_commit.append(untracked_file)
    
if len(files_to_commit) > 0:
    print('files to be committed:')
    for file in files_to_commit:
        print('\t' + file)

    print()

    answer = None
    while answer not in ['y', 'n']:
        answer = input('commit and push changes? [y/n]').lower()

    if answer == 'y':
        repo.index.add(files_to_commit)
        repo.index.commit('Update dicts')
        origin = repo.remote(name='origin')
        origin.push()
        print("changes were committed and pushed")
    else:
        print('exiting')
else:
    print('no untracked dictionary changes')
