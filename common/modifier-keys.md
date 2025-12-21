# Modifier Keys

The question marks will be replaced by strokes and translations for all applicable keyboard keys such as numbers, letters, and F-keys. This is done with the script `build_modifier_combos.py`.

```yaml
PWA/?: '{#option(?)}' # Option
KPWA/?: '{#option(control(?))}' # Option+Control
SKPWA/?: '{#option(control(shift(?)))}' # Option+Control+Shift
SKPWRA/?: '{#option(control(shift(command(?))))}' # Option+Control+Shift+Command
KPWRA/?: '{#option(control(command(?)))}' # Option+Control+Command
SPWA/?: '{#option(shift(?))}' # Option+Shift
SPWRA/?: '{#option(shift(command(?)))}' # Option+Shift+Command
PWRA/?: '{#option(command(?))}' # Option+Command
KPW/?: '{#control(?)}' # Control
SKPW/?: '{#control(shift(?))}' # Control+Shift
SKPWR/?: '{#control(shift(command(?)))}' # Control+Shift+Command
KPWR/?: '{#control(command(?))}' # Control+Command
SPW/?: '{#shift(?)}' # Shift
SPWR/?: '{#shift(command(?))}' # Shift+Command
PWR/?: '{#command(?)}' # Command
```
