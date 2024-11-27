# Commands

## Text Manipulation

| Stroke | Description                    | Translation                  |
|--------|--------------------------------|------------------------------|
| KWRA   | Copy                           | {#command(c)}                |
| KWRAO  | Cut                            | {#command(x)}                |
| KWRO   | Paste                          | {#command(v)}                |
| KWHRO  | Past from history              | {#command(shift(v))}         |
| KPWHRO | Paste and match style          | {#option(command(shift(v)))} |
| K-FR   | Undo                           | {#command(z)}                |
| K-LG   | Redo                           | {#command(shift(z))}         |
| TK-FR  | Delete last character          | {#backspace}                 |
| TK-LG  | Delete next character          | {#delete}                    |
| TK-FRP | Delete last word               | {#option(backspace)}         |
| TK-PLG | Delete next word               | {#option(delete)}            |
| TK-FRB | Delete until beginning of line | {#command(backspace)}        |
| TK-BLG | Delete until end of line       | {#control(k)}                |
| TK-B   | Delete line                    | {#control(k)}                |
| R-RPB  | Option + Enter (new line)      | {#option(return)}            |
| AFPS   | Retroactively add space        | {\*?}                        |
| TK-FPS | Retroactively delete space     | {\*!}                        |
| KPR    | Capitalize, no leading space   | {^}{:case:cap_first_word}    |
| KP     | Capitalize                     | {}{:case:cap_first_word}     |
| R      | no leading space               | {^}{:case:lower_first_char}  |
| HR     | leading space                  | {}{:case:lower_first_char}   |


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

| Stroke | Description                         | Translation                                                                                        |
|--------|-------------------------------------|----------------------------------------------------------------------------------------------------|
| KHR-R  | Open Calendar                       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Calendar Calendar}                  |
| PW-S   | Open Obsidian                       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian}                  |
| T-RPL  | Open Terminal                       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Terminal Terminal}                  |
| Z-PL   | Open Zoom                           | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt zoom.us zoom.us}                    |
| TP-RPB | Open Finder                         | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Finder Finder}                      |
| R-RS   | Open Reminders                      | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}                |
| TPH-TS | Open Notes                          | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Notes Notes}                        |
| SR-S   | Open VS Code                        | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Visual Studio Code\" Code}        |
| KP-BG  | Open XCode                          | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Xcode Xcode}                        |
| PH-BG  | Open Music                          | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Music Music}                        |
| A-FL   | Open Alfred, suppress next space    | {#command(space)}{^}                                                                               |
| SR-PB  | Open VS Code window alfred workflow | {#command(space)}{PLOVER:DELAY:0.05}{^cw^}                                                         |
| S-R    | Toggle Siri                         | {#control(space)}                                                                                  |
| KPH-P  | Open command palette (Github)       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"GitHub\" \"GitHub\"}{#command(k)} |


## VS Code Commands

| Stroke | Description                               | Translation                                                                                                                 |
|--------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| T-FS   | Command: Terminal: Focus on Terminal View | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Visual Studio Code\" Code}{#control(shift(command(down)))} |
| KP-FS  | Command: Explorer: Focus on Folders View  | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Visual Studio Code\" Code}{#control(shift(command(left)))} |
| TK-FS  | Command: View: Focus Active Editor Group  | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Visual Studio Code\" Code}{#control(shift(command(up)))}   |

## Workflow Commands

| Stroke | Description  | Translation                                                                                      |
|--------|--------------|--------------------------------------------------------------------------------------------------|
| TKR-R  | Add reminder | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}{#command(n)} |
