# Home 

## Special keys

| Stroke | Description              | Translation                                                                     |
|--------|--------------------------|---------------------------------------------------------------------------------|
| H-F    | Escape, to fix XCode bug | {PLOVER:SHELL:osascript -e 'tell application \"System Events\" to key code 53'} |

## Open Applications

| Stroke | Description                  | Translation                                                                                            |
|--------|------------------------------|--------------------------------------------------------------------------------------------------------|
| P-RPL  | Open PyCharm                 | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"PyCharm CE\" PyCharm}                 |
| T-PBLG | Open IntelliJ                | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt \"IntelliJ IDEA CE\" \"IntelliJ IDEA\"} |
| W-B    | Open Browser                 | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}                          |
| PH-L   | Open Mail                    | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Mail Mail}                              |
| PW-RPB | Open brain.fm (Safari tab)   | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}{#command(3)}             |
| SKWR-R | Open Jira (first Safari tab) | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}{#command(1)}             |


## Commands

| Stroke  | Description                  | Translation                                                                                          |
|---------|------------------------------|------------------------------------------------------------------------------------------------------|
| TW-B    | Toggle play pause in browser | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}{#space}{#command(tab)} |
| W-FRB   | Press left in browser        | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}{#left}{#command(tab)}  |
| W-BLG   | Press right in browser       | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Safari Safari}{#right}{#command(tab)} |
| TKPW-PT | Open macGPT                  | {#command(shift(control(c)))}                                                                        |

