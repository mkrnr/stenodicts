# Stenodicts

This repository contains my [Plover](https://www.openstenoproject.org/plover/) dictionaries. Some of them are in usual
JSON format while others are organized in tables in Markdown files. The table format serves several purposes:

* It allows grouping inside a file
* It gives room for additional information about the strokes
* It can be displayed on websites using frameworks like [Jekyll](https://jekyllrb.com/),
  see [mkrnr.com/stenodicts/](https://mkrnr.com/stenodicts/)

The Markdown files are parsed to JSON dictionary files with [build_dict.py](build_dict.py).

There are a few more scripts:

* [build_modifier_combos.py](build_modifier_combos.py) to build stroke-combos of the modifier stokes
  in [modifier-keys.md](common/modifier-keys.md) with the stokes in [common/keys.md](common/keys.md)
* [remap_main.py](remap_main.py) to remap entries in the Plover main dictionary based on the custom strokes, for example
  the fingerspelling for both hands defined in [common/keys.md](common/keys.md)
* [sort.py](../dotfiles/scripts/sort.py) to sort the JSON dictionary files
* [upload_to_website.py](upload_to_website.py) to upload the Markdown files to my webspace
