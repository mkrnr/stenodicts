#!/usr/bin/env python3

import codecs
import glob
from pathlib import Path
import re

from git import Repo

from sort import Sorter

sorter = Sorter()
# sort all json files in any subfolder of this project
sorter.sort_all('*/*.json', print_files=False)

stenodicts_website_path = Path("..") / "stenodicts-website"
if stenodicts_website_path.exists():
    for md_file_string in glob.iglob('*/*.md', recursive=True):
        print(md_file_string)
        md_file_path = Path(md_file_string)
        with codecs.open(stenodicts_website_path / md_file_path.name, "w", "utf-8") as output_file:    
            output_file.write("---\n")
            output_file.write("layout: page\n")
            output_file.write("title: " + md_file_path.stem + "\n")
            output_file.write("permalink: /" + md_file_path.stem + "/\n")
            output_file.write("---\n\n")

            with open(md_file_path, 'r') as md_file:
                output_file.write(md_file.read())

repo = Repo('.')

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
