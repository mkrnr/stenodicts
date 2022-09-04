# Commands

## Text Manipulation

| Stroke  | Description                | Translation             |
|---------|----------------------------|-------------------------|
| RA      | Copy                       | {#command(c)}           |
| RAO     | Cut                        | {#command(x)}           |
| RO      | Paste                      | {#command(v)}           |
| KR-FR   | Undo                       | {#command(z)}           |
| KR-LG   | Redo                       | {#command(y)}           |
| -BLG    | Delete                     | {#Delete}               |
| -FRB    | Backspace                  | {#Backspace}            |
| KHR-BLG | Control + Delete           | {#Control_L(Delete)}    |
| KHR-FRB | Control + Backspace        | {#Control_L(Backspace)} |
| AFPS    | Retroactively add space    | {\*?}                   |
| TK-FPS  | Retroactively delete space | {\*!}                   |

## Plover Commands

| Stroke | Description     | Translation              |
|--------|-----------------|--------------------------|
| TKUPT  | Add Translation | {PLOVER:ADD_TRANSLATION} |
| PHRUP  | Lookup Word     | {PLOVER:LOOKUP}          |


## Open Applications

| Stroke | Description   | Translation                                                                       |
|--------|---------------|-----------------------------------------------------------------------------------|
| T-RPL  | Open Terminal | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2}      |
| PW-S   | Open Obsidian | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian} |
| PR-G   | Open program  | {#command(space)}                                                                 |
| SREU   | Toggle Siri   | {#control(space)}                                                                 |

