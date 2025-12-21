# Navigation

## Navigation Keys

```yaml
-FP: '{}{#up}' # Up
-RB: '{}{#down}' # Down
-FPL: '{}{#up}' # Up
-RBG: '{}{#down}' # Down
-FR: '{}{#left}' # Left
-LG: '{}{#right}' # Right
-RPG: '{}{#page_up}' # Page Up
-FBL: '{}{#page_down}' # Page Down
-RPBG: '{}{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/repeat-key-code.scpt 126 30}' # Page cursor 30x up
-FPBL: '{}{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/repeat-key-code.scpt 125 30}' # Move cursor 30x down
SR-FPL: '{#audioraisevolume}' # Volume Up
SR-RBG: '{#audiolowervolume}' # Volume Down
SR-FRPBLG: '{#audiomute}' # Volume Mute
PHR-P: '{#audioplay}' # Audio Play
PHR-FR: '{#audioprev}' # Audio Previous
PHR-LG: '{#audionext}' # Audio Next
-FRP: '{#option(left)}' # Move curser to word left
-PLG: '{#option(right)}' # Move curser to word right
-FRB: '{#command(left)}' # Move curser to beginning of line
-BLG: '{#command(right)}' # Move curser to end of line
-FRPLG: '{#command(up)}' # Move cursor to document beginning
-FRBLG: '{#command(down)}' # Move cursor to document end
PH-FR: '{#shift(left)}' # Mark last character
PH-LG: '{#shift(right)}' # Mark next character
PH-FRP: '{#option(shift(left))}' # Mark last word
PH-PLG: '{#option(shift(right))}' # Mark next word
PH-P: '{#option(left)}{#option(shift(right))}' # Mark word
PH-FRB: '{#control(shift(left))}' # Mark until beginning of line
PH-BLG: '{#control(shift(right))}' # Mark until end of line
PH-B: '{#command(left)}{#command(shift(right))}' # Mark line
PH-FPL: '{#option(shift(up))}' # Mark line up
PH-RBG: '{#option(shift(down))}' # Mark line down
PH-FRPBLG: '{#command(a)}' # Mark all
```


## Window Navigation

```yaml
H-FR: '{#command(bracketleft)}' # Move history left
H-LG: '{#command(bracketright)}' # Move history right
PWR-R: '{#command(1)}' # Switch to tab 1
PWR-B: '{#command(2)}' # Switch to tab 2
PWR-G: '{#command(3)}' # Switch to tab 3
PWR-FR: '{#command(4)}' # Switch to tab 4
PWR-PB: '{#command(5)}' # Switch to tab 5
PWR-LG: '{#command(6)}' # Switch to tab 6
PWR-F: '{#command(7)}' # Switch to tab 7
PWR-P: '{#command(8)}' # Switch to tab 8
PWR-L: '{#command(9)}' # Switch to last tab
PWR-FRPB: '{#control(shift(tab))}' # Switch to tab left
PWR-PBLG: '{#control(tab)}' # Switch to tab right
TW: '{#command(tab)}' # Switch to last application
W-FR: '{#command(quoteleft)}' # Switch to prev app window
W-FPL: '{#command(quoteleft)}' # Switch to prev app window
W-LG: '{#command(shift(quoteleft))}' # Switch to next app window
W-RBG: '{#command(shift(quoteleft))}' # Switch to next app window
PWR-BGS: '{#command(w)}' # Close window
PWR-FBGS: '{#command(q)}' # Close application
KPW-E: '{#control(0)}' # Control + 0
KPW-R: '{#control(1)}' # Control + 1
KPW-B: '{#control(2)}' # Control + 2
KPW-G: '{#control(3)}' # Control + 3
KPW-FR: '{#control(4)}' # Control + 4
KPW-PB: '{#control(5)}' # Control + 5
KPW-LG: '{#control(6)}' # Control + 6
KPW-F: '{#control(7)}' # Control + 7
KPW-P: '{#control(8)}' # Control + 8
KPW-L: '{#control(9)}' # Control + 9
R-FRPB: '{#control(option(command(left)))}' # Move window to screen left
R-PBLG: '{#control(option(command(right)))}' # Move window to screen right
R-RB: '{#control(option(down))}' # Move window down
R-RBG: '{#control(option(down))}' # Move window down
R-FR: '{#control(option(left))}' # Move window left
R-LG: '{#control(option(right))}' # Move window right
R-FP: '{#control(option(up))}' # Move window up
R-FPL: '{#control(option(up))}' # Move window up
R-FRPBLG: '{#control(option(return))}' # Move window full screen
TK-FP: '{#control(F3)}' # Focus dock (Dock change)
PWR-RPB: '{#command(return)}' # Command + Return
KPH-R: '{#shift(command(v))}' # Clipboard History
TP-RPL: '{#command(shift(control(f)))}' # Follow Link via Homerow app
TP: '{}{PLOVER:SHELL:printf TOGGLE        | /opt/homebrew/bin/socat - UNIX-SENDTO:/tmp/stenomouse.sock}' # Toggle stenomouse links
ST-PLS: '{}{PLOVER:SHELL:source ~/git/stenomouse/.venv/bin/activate && bash ~/git/stenomouse/start.sh}' # Restart stenomouse links
```


## Program Navigation

```yaml
PWR/-PB: '{#command(n)}' # New window
TPWR: '{#command(t)}' # New tab
PR-P: '{#command(comma)}' # Open program preferences
PWROFR: '{#command(option(left))}' # Switch to left tab group
PWROLG: '{#command(option(right))}' # Switch to right tab group
PWROFPL: '{#command(option(up))}' # Switch to top tab group
PWRORBG: '{#command(option(down))}' # Switch to bottom tab group
```

## Browser

```yaml
KP-LT: '{#command(k)}' # Open GitHub command palette
OL: '{#option(j)}' # Open link
OLT: '{#option(l)}' # Open link in new tab
```


## IntelliJ / PyCharm

```yaml
STP-L: '{#command(shift(o))}' # Go to File...
SK-LS: '{#command(o)}' # Go to Class...
S-FPL: '{#option(command(o))}' # Go to Symbol...
STK-L: '{#command(b)}' # Go to Declaration or Usages
TP-BGS: '{#shift(command(a))}' # Find Action...
SK-BGS: '{#option(return)}' # Show context actions
R-BG: '{#shift(control(r))}' # Run code
TK-BG: '{#shift(control(d))}' # Debug code
KPH-PB: '{#option(F5)}' # Activate Commit tool window
TKPW-PB: '{#option(F4)}' # Activate Git tool window
PR-PB: '{#shift(command(p))}' # Activate Project tool windo
SK-PL: '{#command(option(shift(k)))}' # Show Context Menu
TP-PBT: '{#command(option(shift(t)))}' # Fully Expand Tree Node
-RPL: '{#shift(F6)}' # Rename
THR-BG: '{#command(slash)}' # Toggle comments
```


## Obsidian

```yaml
SW-FP: '{#command(e)}' # Open quick switcher
PWR-PBZ: '{^Bronze/^}' # Create note in Bronze folder
TKPW-LD: '{^Gold/^}' # Create note in Gold folder
S-FRL: '{^Silver/^}' # Create note in Silver folder
KR-PBT: '{#shift(return)}' # Create note in quick switcher
P-PBT: '{#command(shift(e))}' # Pin note
TPHR: '{#option(return)}' # Follow link under cursor
```


## Terminal

```yaml
SR-FR: '{#control(r)}' # backward search
SR-LG: '{#control(s)}' # forward search
```


## Vim

```yaml
SR-BG: '{#control(v)}' # Visual block
```

## Reminders

```yaml
PHR-BG: '{#shift(command(c))}' # Mark reminder complete
```
