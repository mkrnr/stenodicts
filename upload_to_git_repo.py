#!/usr/bin/env python3

import sys

from git import Repo

from sort import Sorter

# repo path needs to have trailing slash
repo_path = sys.argv[1]

print("sort all json files in any subfolder of this project")
sorter = Sorter()
sorter.sort_all(repo_path+'/*.json', print_files=True)

print("check for dictionary changes in " + repo_path)

repo = Repo(repo_path)

changed_files = [item.a_path for item in repo.index.diff(None)]
changed_files.extend(repo.untracked_files)

if len(changed_files) > 0:
    print('files to be committed:')
    for md_file_string in changed_files:
        print('\t' + md_file_string)

    repo.index.add(changed_files)
    repo.index.commit('Update files')
    origin = repo.remote(name='origin')
    origin.push()
    print("changes were committed and pushed")

else:
    print('no untracked dictionary changes')

print("done")
