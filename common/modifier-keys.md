# Modifier Keys

The `<key>` will be replaced by strokes and translations for all applicable keyboard keys using the `stenodict-cli` tool.

```yaml
PWA/<key>: '{#option(<key>)}' # Option
KPWA/<key>: '{#option(control(<key>))}' # Option+Control
SKPWA/<key>: '{#option(control(shift(<key>)))}' # Option+Control+Shift
SKPWRA/<key>: '{#option(control(shift(command(<key>))))}' # Option+Control+Shift+Command
KPWRA/<key>: '{#option(control(command(<key>)))}' # Option+Control+Command
SPWA/<key>: '{#option(shift(<key>))}' # Option+Shift
SPWRA/<key>: '{#option(shift(command(<key>)))}' # Option+Shift+Command
PWRA/<key>: '{#option(command(<key>))}' # Option+Command
KPW/<key>: '{#control(<key>)}' # Control
SKPW/<key>: '{#control(shift(<key>))}' # Control+Shift
SKPWR/<key>: '{#control(shift(command(<key>)))}' # Control+Shift+Command
KPWR/<key>: '{#control(command(<key>))}' # Control+Command
SPW/<key>: '{#shift(<key>)}' # Shift
SPWR/<key>: '{#shift(command(<key>))}' # Shift+Command
PWR/<key>: '{#command(<key>)}' # Command
```
