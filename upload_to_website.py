#!/usr/bin/env python3

import codecs
import glob
import os
import sys
from pathlib import Path

# repo path needs to have trailing slash
repo_path = sys.argv[1]

print("building jekyll and uploading to webspace")

stenodicts_website_path = Path(repo_path + "/../stenodicts-website")
if stenodicts_website_path.exists():

    print("generate .md files with headers")
    for md_file_string in glob.iglob(repo_path + '/*/*.md', recursive=True):
        print(md_file_string)
        md_file_path = Path(md_file_string)
        with codecs.open(str(stenodicts_website_path / md_file_path.name), "w", "utf-8") as output_file:
            output_file.write("---\n")
            output_file.write("layout: page\n")
            output_file.write("title: " + md_file_path.stem + "\n")
            output_file.write("permalink: /" + md_file_path.stem + "/\n")
            output_file.write("---\n\n")

            with open(str(md_file_path), 'r') as md_file:
                output_file.write(md_file.read())

    print("build jekyll files")
    os.system('cd ' + repo_path + '/../stenodicts-website && JEKYLL_ENV=production bundle exec jekyll build')

    print("upload to webspace")
    os.system(
        'rsync -avh ' + repo_path + '/../stenodicts-website/_site/ webspace:/www/htdocs/\\*/mkrnr.com/stenodicts --delete')

else:
    print('path does not exist: ' + str(stenodicts_website_path))

print("done")
