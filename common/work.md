# Work

## Open Applications

| Stroke | Description   | Translation                                                                                         |
|--------|---------------|-----------------------------------------------------------------------------------------------------|
| T-PBLG | Open IntelliJ | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"IntelliJ IDEA\" \"IntelliJ IDEA\"} |
| W-B    | Open Browser  | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Google Chrome\" \"Google Chrome\"} |
| TK-G   | Open DataGrip | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt DataGrip DataGrip}                   |

## Run Scripts

| Stroke | Description       | Translation                                        |
|--------|-------------------|----------------------------------------------------|
| WHR-PB | Webcam Lights On  | {PLOVER:SHELL:shortcuts run \"Webcam Lights On\"}  |
| WHR-F  | Webcam Lights Off | {PLOVER:SHELL:shortcuts run \"Webcam Lights Off\"} |

## Chrome

| Stroke | Description                       | Translation                                                                                                      |
|--------|-----------------------------------|------------------------------------------------------------------------------------------------------------------|
| -BGT   | Open Okta selector                | {#command(shift(o))}                                                                                             |
| PH-L   | Open Mail (first chrome tab)      | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Google Chrome\" \"Google Chrome\"}{#command(1)} |
| KHR-R  | Open Calendar (second chrome tab) | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Google Chrome\" \"Google Chrome\"}{#command(2)} |
| SKWR-R | Open Jira (third chrome tab)      | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"Google Chrome\" \"Google Chrome\"}{#command(3)} |
| TPHR-P | Insert password with bitwarden    | {#command(shift(l))}                                                                                             |


## Mattermost

| Stroke | Description           | Translation                                                                                        |
|--------|-----------------------|----------------------------------------------------------------------------------------------------|
| PH-F   | Mattermost Find       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Mattermost Mattermost}{#command(k)} |
| PH-R   | React to last message | {#command(shift(backslash))}                                                                       |
