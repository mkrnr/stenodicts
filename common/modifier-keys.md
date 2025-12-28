# Modifier Keys

The `<outline>` and `<translation>` tags will be replaced by outlines and translations for all applicable keyboard keys using the `stenodict-cli` tool.

```yaml
PWA/<outline>: '{#option(<translation>)}' # Option
KPWA/<outline>: '{#option(control(<translation>))}' # Option+Control
SKPWA/<outline>: '{#option(control(shift(<translation>)))}' # Option+Control+Shift
SKPWRA/<outline>: '{#option(control(shift(command(<translation>))))}' # Option+Control+Shift+Command
KPWRA/<outline>: '{#option(control(command(<translation>)))}' # Option+Control+Command
SPWA/<outline>: '{#option(shift(<translation>))}' # Option+Shift
SPWRA/<outline>: '{#option(shift(command(<translation>)))}' # Option+Shift+Command
PWRA/<outline>: '{#option(command(<translation>))}' # Option+Command
KPW/<outline>: '{#control(<translation>)}' # Control
SKPW/<outline>: '{#control(shift(<translation>))}' # Control+Shift
SKPWR/<outline>: '{#control(shift(command(<translation>)))}' # Control+Shift+Command
KPWR/<outline>: '{#control(command(<translation>))}' # Control+Command
SPW/<outline>: '{#shift(<translation>)}' # Shift
SPWR/<outline>: '{#shift(command(<translation>))}' # Shift+Command
PWR/<outline>: '{#command(<translation>)}' # Command
```

