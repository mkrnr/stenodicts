# Commands

## Text Manipulation

| Stroke  | Description         | Translation             |
|---------|---------------------|-------------------------|
| RA     | Copy                | {#command(c)}           |
| RAO    | Cut                 | {#command(x)}           |
| RO     | Paste               | {#command(v)}           |
| -BLG    | Delete              | {#Delete}               |
| -FRB    | Backspace           | {#Backspace}            |
| KHR-BLG | Control + Delete    | {#Control_L(Delete)}    |
| KHR-FRB | Control + Backspace | {#Control_L(Backspace)} |

## Plover Commands

| Stroke | Description       | Translation              |
|--------|-------------------|--------------------------|
| TKUPT  | Add Translation   | {PLOVER:ADD_TRANSLATION} |
| PHRUP  | Lookup Word       | {PLOVER:LOOKUP}          |

## Open Applications

| Stroke | Description   | Translation                                                                  |
|--------|---------------|------------------------------------------------------------------------------|
| T-RPL  | Open Terminal | {PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2} |
| PR-G   | Open program  | {#command(space)}                                                            |
| SREU   | Toggle Siri   | {#control(space)}                                                            |


"KHR-BG": "{#Control_L(c)}",
"KPH*BG": "{#Super_L(k)}",
"KPH*F": "{#Super_L(v)}",
"PHROLG": "{PLOVER:TOGGLE}",
"PW*FP": "{#BackSpace}",
"PW-FP": "{#BackSpace}",
"R*R": "{#Return}{^}",
"R-R": "{^}{#Return}{^}{-|}",
"SH-FT": "{#Control_L(Home)}{^}",
"SKW-BGS": "{#Return}{^}",
"SKWRAEURBGS": "{#Return}{#Return}{^}{-|}",
"SKWRAURBGS": "{#Return}{#Return}{^}{-|}",
"SR-RS": "{#Control_L(End)}{^}",
"STPH-B": "{#Down}{^}",
"STPH-BG": "{#Control_L(Right)}{^}",
"STPH-G": "{#Right}{^}",
"STPH-P": "{#Up}{^}",
"STPH-R": "{#Left}{^}",
"TA*B": "{#Tab}{^}",
"TPW-G": "{#Alt_L(Right)}",
"TPW-R": "{#Alt_L(Left)}"
