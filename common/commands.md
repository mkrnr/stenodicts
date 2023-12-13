# Commands

## Text Manipulation

| Stroke  | Description                  | Translation                   |
|---------|------------------------------|-------------------------------|
| KWRA    | Copy                         | {#command(c)}                 |
| KWRAO   | Cut                          | {#command(x)}                 |
| KWRO    | Paste                        | {#command(v)}                 |
| KWROP   | Paste with Pure Paste        | {#control(command(shift(v)))} |
| KR-FR   | Undo                         | {#command(z)}                 |
| KR-LG   | Redo                         | {#command(shift(z))}          |
| -BLG    | Delete                       | {#delete}                     |
| -FRB    | Backspace                    | {#backspace}                  |
| KHR-BLG | Control + Delete             | {#control(delete)}            |
| KHR-FRB | Control + Backspace          | {#control(backspace)}         |
| R-RPB   | Option + Enter (new line)    | {#option(return)}             |
| AFPS    | Retroactively add space      | {\*?}                         |
| TK-FPS  | Retroactively delete space   | {\*!}                         |
| KPR     | Capitalize, no leading space | {^}{:case:cap_first_word}     |
| KP      | Capitalize                   | {}{:case:cap_first_word}      |
| R       | no leading space             | {^}{:case:lower_first_char}   |
| HR      | leading space                | {}{:case:lower_first_char}      |


## Plover Commands

| Stroke | Description                  | Translation                                                                                |
|--------|------------------------------|--------------------------------------------------------------------------------------------|
| TKUPT  | Add Translation              | {PLOVER:ADD_TRANSLATION}                                                                   |
| PHRUP  | Lookup Word                  | {PLOVER:LOOKUP}                                                                            |
| R-F    | Switch to English system     | {PLOVER:SWITCH_SYSTEM:Plover Mod-Z}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/english.sh} |
| H-R    | Switch to German system      | {PLOVER:SWITCH_SYSTEM:Regenpfeifer}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/german.sh}  |
| HR-FR  | Switch to Raw system         | {PLOVER:SWITCH_SYSTEM:Plover Mod-Z Raw}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/raw.sh} |

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

| Stroke | Description     | Translation                                                                           |
|--------|-----------------|---------------------------------------------------------------------------------------|
| KHR-R  | Open Calendar   | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Calendar Calendar}     |
| PW-S   | Open Obsidian   | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian}     |
| T-RPL  | Open Terminal   | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2}          |
| SHR-BG | Open Slack      | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Slack Slack}           |
| PH-PL  | Open Mattermost | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Mattermost Mattermost} |
| Z-PL   | Open Zoom       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt zoom.us zoom.us}       |
| TP-RPB | Open Finder     | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Finder Finder}         |
| R-RS   | Open Reminders  | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}   |
| TPH-TS | Open Notes      | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Notes Notes}           |
| SR-S   | Open VS Code    | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Code Code}             |
| A-FL   | Open Alfred     | {#command(space)}                                                                     |
| S-R    | Toggle Siri     | {#control(space)}                                                                     |

## Zoom

| Stroke | Description     | Translation                  |
|--------|-----------------|------------------------------|
| PH-T   | Mute Microphone | {#command(shift(option(m)))} |

## Workflow Commands

| Stroke | Description  | Translation                                                                                      |
|--------|--------------|--------------------------------------------------------------------------------------------------|
| TKR-R  | Add reminder | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}{#command(n)} |
