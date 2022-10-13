# Commands

## Text Manipulation

| Stroke  | Description                | Translation           |
|---------|----------------------------|-----------------------|
| RA      | Copy                       | {#command(c)}         |
| RAO     | Cut                        | {#command(x)}         |
| RO      | Paste                      | {#command(v)}         |
| KR-FR   | Undo                       | {#command(z)}         |
| KR-LG   | Redo                       | {#command(shift(z))}  |
| -BLG    | Delete                     | {#delete}             |
| -FRB    | Backspace                  | {#backspace}          |
| KHR-BLG | Control + Delete           | {#control(delete)}    |
| KHR-FRB | Control + Backspace        | {#control(backspace)} |
| R-RPB   | Option + Enter (new line)  | {#option(return)}     |
| AFPS    | Retroactively add space    | {\*?}                 |
| TK-FPS  | Retroactively delete space | {\*!}                 |


## Plover Commands

| Stroke | Description     | Translation              |
|--------|-----------------|--------------------------|
| TKUPT  | Add Translation | {PLOVER:ADD_TRANSLATION} |
| PHRUP  | Lookup Word     | {PLOVER:LOOKUP}          |


## Open Applications

| Stroke | Description   | Translation                                                                       |
|--------|---------------|-----------------------------------------------------------------------------------|
| KHR-R  | Open Calendar | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Calendar Calendar} |
| PW-S   | Open Obsidian | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian} |
| T-RPL  | Open Terminal | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2}      |
| SHR-BG | Open Slack    | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Slack Slack}       |
| SAOPL  | Open Zoom     | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt zoom.us zoom.us}   |
| A-FL   | Open Alfred   | {#command(space)}                                                                 |
| SREU   | Toggle Siri   | {#control(space)}                                                                 |
| SREU   | Toggle Siri   | {#control(space)}                                                                 |

