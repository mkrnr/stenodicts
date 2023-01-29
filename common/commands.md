# Commands

## Text Manipulation

| Stroke  | Description                | Translation                   |
|---------|----------------------------|-------------------------------|
| RA      | Copy                       | {#command(c)}                 |
| RAO     | Cut                        | {#command(x)}                 |
| RO      | Paste with Pure Paste                      | {#control(command(shift(v)))} |
| KR-FR   | Undo                       | {#command(z)}                 |
| KR-LG   | Redo                       | {#command(shift(z))}          |
| -BLG    | Delete                     | {#delete}                     |
| -FRB    | Backspace                  | {#backspace}                  |
| KHR-BLG | Control + Delete           | {#control(delete)}            |
| KHR-FRB | Control + Backspace        | {#control(backspace)}         |
| R-RPB   | Option + Enter (new line)  | {#option(return)}             |
| AFPS    | Retroactively add space    | {\*?}                         |
| TK-FPS  | Retroactively delete space | {\*!}                         |


## Plover Commands

| Stroke | Description              | Translation                                                                                |
|--------|--------------------------|--------------------------------------------------------------------------------------------|
| TKUPT  | Add Translation          | {PLOVER:ADD_TRANSLATION}                                                                   |
| PHRUP  | Lookup Word              | {PLOVER:LOOKUP}                                                                            |
| R-F    | Switch to English system | {PLOVER:SWITCH_SYSTEM:Plover Mod-Z}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/english.sh} |
| H-R    | Switch to German system  | {PLOVER:SWITCH_SYSTEM:Regenpfeifer}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/german.sh}  |
| HR-FR  | Switch to Raw system     | {PLOVER:SWITCH_SYSTEM:Plover Mod-Z Raw}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/raw.sh} |

## Terminal Commands

| Stroke       | Description                                   | Translation               |
|--------------|-----------------------------------------------|---------------------------|
| SR-PL        | Type vim with trailing space                  | {}{^vim ^}                |
| KR-D         | Type cd with trailing space                   | {}{^cd ^}                 |
| TKPW-T       | Type git with no leading or trailing space    | {}{^git}                  |
| TKPW-TS      | Type ~/git/ with no leading or trailing space | {}{^~/git/^}              |
| H-PLS        | Home with slash                               | {}{^~/^}                  |
| H-RPL        | Home with enter                               | {}{^cd ~^}{#return}       |
| TKUP         | Type ../ with no leading or trailing space    | {}{^../^}                 |


## Open Applications

| Stroke | Description   | Translation                                                                       |
|--------|---------------|-----------------------------------------------------------------------------------|
| KHR-R  | Open Calendar | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Calendar Calendar} |
| PW-S   | Open Obsidian | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian} |
| T-RPL  | Open Terminal | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2}      |
| SHR-BG | Open Slack    | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Slack Slack}       |
| SAOPL  | Open Zoom     | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt zoom.us zoom.us}   |
| TP-RPB | Open Finder   | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Finder Finder}     |
| A-FL   | Open Alfred   | {#command(space)}                                                                 |
| SREU   | Toggle Siri   | {#control(space)}                                                                 |

