# Navigation

## Navigation Keys

| Stroke    | Description                       | Translation                                                                     |
|-----------|-----------------------------------|---------------------------------------------------------------------------------|
| -FP       | Up                                | {}{#up}                                                                         |
| -RB       | Down                              | {}{#down}                                                                       |
| -FPL      | Up                                | {}{#up}                                                                         |
| -RBG      | Down                              | {}{#down}                                                                       |
| -FR       | Left                              | {}{#left}                                                                       |
| -LG       | Right                             | {}{#right}                                                                      |
| -RPG      | Page Up                           | {}{#page_up}                                                                    |
| -FBL      | Page Down                         | {}{#page_down}                                                                  |
| -RPBG     | Page cursor 30x up                | {}{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/repeat-key-code.scpt 126 30} |
| -FPBL     | Move cursor 30x down              | {}{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/repeat-key-code.scpt 125 30} |
| SR-FPL    | Volume Up                         | {#audioraisevolume}                                                             |
| SR-RBG    | Volume Down                       | {#audiolowervolume}                                                             |
| SR-FRPBLG | Volume Mute                       | {#audiomute}                                                                    |
| PHR-P     | Audio Play                        | {#audioplay}                                                                    |
| PHR-FR    | Audio Previous                    | {#audioprev}                                                                    |
| PHR-LG    | Audio Next                        | {#audionext}                                                                    |
| -FRP      | Move curser to word left          | {#option(left)}                                                                 |
| -PLG      | Move curser to word right         | {#option(right)}                                                                |
| -FRB      | Move curser to beginning of line  | {#command(left)}                                                                |
| -BLG      | Move curser to end of line        | {#command(right)}                                                               |
| -FRPLG    | Move cursor to document beginning | {#command(up)}                                                                  |
| -FRBLG    | Move cursor to document end       | {#command(down)}                                                                |
| PH-FR     | Mark last character               | {#shift(left)}                                                                  |
| PH-LG     | Mark next character               | {#shift(right)}                                                                 |
| PH-FRP    | Mark last word                    | {#option(shift(left))}                                                          |
| PH-PLG    | Mark next word                    | {#option(shift(right))}                                                         |
| PH-P      | Mark word                         | {#option(left)}{#option(shift(right))}                                          |
| PH-FRB    | Mark until beginning of line      | {#control(shift(left))}                                                         |
| PH-BLG    | Mark until end of line            | {#control(shift(right))}                                                        |
| PH-B      | Mark line                         | {#command(left)}{#command(shift(right))}                                        |
| PH-FPL    | Mark line up                      | {#option(shift(up))}                                                            |
| PH-RBG    | Mark line down                    | {#option(shift(down))}                                                          |
| PH-FRPBLG | Mark all                          | {#command(a)}                                                                   |


## Window Navigation

| Stroke   | Description                 | Translation                                                                                         |
|----------|-----------------------------|-----------------------------------------------------------------------------------------------------|
| H-FR     | Move history left           | {#command(bracketleft)}                                                                             |
| H-LG     | Move history right          | {#command(bracketright)}                                                                            |
| PWR-F    | Switch to tab 1             | {#command(1)}                                                                                       |
| PWR-P    | Switch to tab 2             | {#command(2)}                                                                                       |
| PWR-FP   | Switch to tab 3             | {#command(3)}                                                                                       |
| PWR-L    | Switch to tab 4             | {#command(4)}                                                                                       |
| PWR-FL   | Switch to tab 5             | {#command(5)}                                                                                       |
| PWR-PL   | Switch to tab 6             | {#command(6)}                                                                                       |
| PWR-FPL  | Switch to tab 7             | {#command(7)}                                                                                       |
| PWR-T    | Switch to tab 8             | {#command(8)}                                                                                       |
| PWR-FT   | Switch to last tab          | {#command(9)}                                                                                       |
| PWR-FR   | Switch to tab left          | {#control(shift(tab))}                                                                              |
| PWR-LG   | Switch to tab right         | {#control(tab)}                                                                                     |
| TW       | Switch to last application  | {#command(tab)}                                                                                     |
| W-FR     | Switch to prev app window   | {#command(quoteleft)}                                                                               |
| W-FPL    | Switch to prev app window   | {#command(quoteleft)}                                                                               |
| W-LG     | Switch to next app window   | {#command(shift(quoteleft))}                                                                        |
| W-RBG    | Switch to next app window   | {#command(shift(quoteleft))}                                                                        |
| PWR-BGS  | Close window                | {#command(w)}                                                                                       |
| PWR-FBGS | Close application           | {#command(q)}                                                                                       |
| KPW-D    | Control + 0                 | {#control(0)}                                                                                       |
| KPW-F    | Control + 1                 | {#control(1)}                                                                                       |
| KPW-P    | Control + 2                 | {#control(2)}                                                                                       |
| KPW-FP   | Control + 3                 | {#control(3)}                                                                                       |
| KPW-L    | Control + 4                 | {#control(4)}                                                                                       |
| KPW-FL   | Control + 5                 | {#control(5)}                                                                                       |
| KPW-PL   | Control + 6                 | {#control(6)}                                                                                       |
| KPW-FPL  | Control + 7                 | {#control(7)}                                                                                       |
| KPW-T    | Control + 8                 | {#control(8)}                                                                                       |
| KPW-FT   | Control + 9                 | {#control(9)}                                                                                       |
| R-FRPB   | Move window to screen left  | {#control(option(command(left)))}                                                                   |
| R-PBLG   | Move window to screen right | {#control(option(command(right)))}                                                                  |
| R-RB     | Move window down            | {#control(option(down))}                                                                            |
| R-RBG    | Move window down            | {#control(option(down))}                                                                            |
| R-FR     | Move window left            | {#control(option(left))}                                                                            |
| R-LG     | Move window right           | {#control(option(right))}                                                                           |
| R-FP     | Move window up              | {#control(option(up))}                                                                              |
| R-FPL    | Move window up              | {#control(option(up))}                                                                              |
| R-FRPBLG | Move window full screen     | {#control(option(return))}                                                                          |
| TK-FP    | Focus dock (Dock change)    | {#control(F3)}                                                                                      |
| PWR-R    | Command + Return            | {#option(return)}                                                                                   |
| KPH-R    | Clipboard History           | {#shift(command(v))}                                                                                |
| TP       | Follow Link via Homerow app | {#command(shift(control(f)))}                                                                       |
| TP-PLS   | Toggle stenomouse links     | {}{PLOVER:SHELL:printf TOGGLE        \| /opt/homebrew/bin/socat - UNIX-SENDTO:/tmp/stenomouse.sock} |


## Program Navigation

| Stroke  | Description                | Translation               |
|---------|----------------------------|---------------------------|
| PWR-PB  | New window                 | {#command(n)}             |
| TPWR    | New tab                    | {#command(t)}             |
| PR-P    | Open program preferences   | {#command(comma)}         |
| PWROFR  | Switch to left tab group   | {#command(option(left))}  |
| PWROLG  | Switch to right tab group  | {#command(option(right))} |
| PWROFPL | Switch to top tab group    | {#command(option(up))}    |
| PWRORBG | Switch to bottom tab group | {#command(option(down))}  |

## Browser

| Stroke  | Description                 | Translation          |
|---------|-----------------------------|----------------------|
| KP-LT   | Open GitHub command palette | {#command(k)}        |
| OL      | Open link                   | {#option(j)}         |
| OLT     | Open link in new tab        | {#option(l)}         |


## IntelliJ / PyCharm

| Stroke  | Description                 | Translation                  |
|---------|-----------------------------|------------------------------|
| STP-L   | Go to File...               | {#command(shift(o))}         |
| SK-LS   | Go to Class...              | {#command(o)}                |
| S-FPL   | Go to Symbol...             | {#option(command(o))}        |
| STK-L   | Go to Declaration or Usages | {#command(b)}                |
| TP-BGS  | Find Action...              | {#shift(command(a))}         |
| SK-BGS  | Show context actions        | {#option(return)}            |
| R-BG    | Run code                    | {#shift(control(r))}         |
| TK-BG   | Debug code                  | {#shift(control(d))}         |
| KPH-PB  | Activate Commit tool window | {#option(F5)}                |
| TKPW-PB | Activate Git tool window    | {#option(F4)}                |
| PR-PB   | Activate Project tool windo | {#shift(command(p))}         |
| SK-PL   | Show Context Menu           | {#command(option(shift(k)))} |
| TP-PBT  | Fully Expand Tree Node      | {#command(option(shift(t)))} |
| -RPL    | Rename                      | {#shift(F6)}                 |
| THR-BG  | Toggle comments             | {#command(slash)}            |


## Obsidian

| Stroke  | Description                   | Translation          |
|---------|-------------------------------|----------------------|
| SW-FP   | Open quick switcher           | {#command(e)}        |
| PWR-PBZ | Create note in Bronze folder  | {^Bronze/^}          |
| TKPW-LD | Create note in Gold folder    | {^Gold/^}            |
| S-FRL   | Create note in Silver folder  | {^Silver/^}          |
| KR-PBT  | Create note in quick switcher | {#shift(return)}     |
| P-NT    | Pin note                      | {#command(shift(e))} |
| TPHR    | Follow link under cursor      | {#option(return)}    |




## Terminal

| Stroke | Description     | Translation   |
|--------|-----------------|---------------|
| KPW-R  | backward search | {#control(r)} |
| KPW-S  | forward search  | {#control(s)} |


## Vim

| Stroke | Description  | Translation   |
|--------|--------------|---------------|
| SR-BG  | Visual block | {#control(v)} |

## Reminders

| Stroke | Description            | Translation          |
|--------|------------------------|----------------------|
| PHR-BG | Mark reminder complete | {#shift(command(c))} |

