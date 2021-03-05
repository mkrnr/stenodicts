#!/usr/bin/env python3

import re
import sys

from git import Repo

from sort import Sorter

print()
print("sort all json files in any subfolder of this project")
sorter = Sorter()
sorter.sort_all('*/*.json', print_files=False)

# repo path needs to have trailing slash
repo_path = sys.argv[1]

print("check for dictionary changes in " + repo_path)

repo = Repo(repo_path)

files_to_commit = []

changed_files = [item.a_path for item in repo.index.diff(None) ]
changed_files.extend(repo.untracked_files)

for changed_file in changed_files:
    if re.search(r'.*/.*(\.json|\.md)', str(changed_file)):
        files_to_commit.append(changed_file)
    
if len(files_to_commit) > 0:
    print('files to be committed:')
    for md_file_string in files_to_commit:
        print('\t' + md_file_string)
   
    repo.index.add(files_to_commit)
    repo.index.commit('Update dicts')
    origin = repo.remote(name='origin')
    origin.pull()
    origin.push()
    print("changes were committed and pushed")
    
else:
    print('no untracked dictionary changes')
    
print("done")
