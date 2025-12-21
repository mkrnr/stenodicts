# Commands

## Text Manipulation

```yaml
KWRA: '{#command(c)}' # Copy
KWRAO: '{#command(x)}' # Cut
KWRO: '{}{#command(v)}' # Paste
KWHRO: '{}{#command(shift(v))}' # Past from history
KPWHRO: '{}{#option(command(shift(v)))}' # Paste and match style
K-FR: '{}{#command(z)}' # Undo
K-LG: '{}{#command(shift(z))}' # Redo
TK-FR: '{}{#backspace}' # Delete last character
TK-LG: '{}{#delete}' # Delete next character
TK-FRP: '{}{#option(backspace)}' # Delete last word
TK-PLG: '{}{#option(delete)}' # Delete next word
TK-FRB: '{}{#command(backspace)}' # Delete until beginning of line
TK-BLG: '{}{#control(k)}' # Delete until end of line
TK-B: '{}{#control(k)}' # Delete line
R-RPB: '{}{#shift(return)}' # Shift + Enter (new line)
AFPS: '{*?}' # Retroactively add space
TK-FPS: '{*!}' # Retroactively delete space
KPR: '{^}{:case:cap_first_word}' # Capitalize, no leading space
KP: '{}{:case:cap_first_word}' # Capitalize
R: '{^}{:case:lower_first_char}' # no leading space
HR: '{}{:case:lower_first_char}' # leading space
```

## Plover Commands

```yaml
TKUPT: '{PLOVER:ADD_TRANSLATION}' # Add Translation
PHRUP: '{PLOVER:LOOKUP}' # Lookup Word
R-F: '{PLOVER:SWITCH_SYSTEM:Plover Mod-Z}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/english.sh}' # Switch to English system
H-R: '{PLOVER:SWITCH_SYSTEM:Regenpfeifer}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/german.sh}' # Switch to German system
HR-FR: '{PLOVER:SWITCH_SYSTEM:Plover Mod-Z Raw}{PLOVER:SHELL:~/git/dotfiles/scripts/sphero/raw.sh}' # Switch to Raw system
```

## Terminal Commands

```yaml
SR-PL: '{}{^vim ^}' # Type vim with trailing space
KR-D: '{}{^cd ^}' # Type cd with trailing space
TKPW-T: '{}{^git}' # Type git with no leading or trailing space
TKPW-TS: '{}{^~/git/^}' # Type ~/git/ with no leading or trailing space
H-PLS: '{}{^~/^}' # Home with slash
H-RPL: '{}{^cd ~^}{#return}' # Home with enter
TKUP: '{}{^../^}' # Type ../ with no leading or trailing space
```

## Open Applications

```yaml
KHR-R: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Calendar Calendar}' # Open Calendar
KR-PL: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "Google Chrome" Chrome}' # Open Google Chrome
PW-S: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Obsidian Obsidian}' # Open Obsidian
T-RPL: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt iTerm iTerm2}' # Open Terminal
Z-PL: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt zoom.us zoom.us}' # Open Zoom
TP-RPB: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Finder Finder}' # Open Finder
R-RS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}' # Open Reminders
TPH-TS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Notes Notes}' # Open Notes
TPH-BS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Numbers Numbers}' # Open Numbers
SR-S: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "Visual Studio Code" Code}' # Open VS Code
KP-BG: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Xcode Xcode}' # Open XCode
PH-BG: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Music Music}' # Open Music
TPR-FPL: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Freeform Freeform}' # Open Freeform
A-FL: '{#command(space)}{^}' # Open Alfred, suppress next space
SR-PB: '{#command(space)}{PLOVER:DELAY:0.05}{^cw^}' # Open VS Code window alfred workflow
S-R: '{#control(space)}' # Toggle Siri
KPH-P: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "GitHub" "GitHub"}{#command(k)}' # Open command palette (Github)
```

## VS Code Commands

```yaml
T-FS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "Visual Studio Code" Code}{#control(shift(command(down)))}' # Command: Terminal: Focus on Terminal View
KP-FS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "Visual Studio Code" Code}{#control(shift(command(left)))}' # Command: Explorer: Focus on Folders View
TK-FS: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt "Visual Studio Code" Code}{#control(shift(command(up)))}' # Command: View: Focus Active Editor Group
```

## Workflow Commands

```yaml
TKR-R: '{PLOVER:SHELL:osascript ~/git/stenodicts/scripts/open-app.scpt Reminders Reminders}{#command(n)}' # Add reminder
```
