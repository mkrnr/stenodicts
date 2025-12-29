# Keys

## Letters

```yaml
A: '{^}a' # a
AP: '{^}A' # A
-B: '{^}b' # b
P-B: '{^}B' # B
KR: '{^}c' # c
KR-P: '{^}C' # C
TK: '{^}d' # d
TK-P: '{^}D' # D
E: '{^}e' # e
PE: '{^}E' # E
-F: '{^}f' # f
P-F: '{^}F' # F
-G: '{^}g' # g
P-G: '{^}G' # G
H: '{^}h' # h
H-P: '{^}H' # H
EU: '{^}i' # i
PEU: '{^}I' # I
-PBLG: '{^}j' # j
P-PBLG: '{^}J' # J
K: '{^}k' # k
K-P: '{^}K' # K
-L: '{^}l' # l
P-L: '{^}L' # L
-PL: '{^}m' # m
P-PL: '{^}M' # M
-PB: '{^}n' # n
P-PB: '{^}N' # N
O: '{^}o' # o
OP: '{^}O' # O
-P: '{^}p' # p
P-P: '{^}P' # P
KW: '{^}q' # q
KW-P: '{^}Q' # Q
-R: '{^}r' # r
P-R: '{^}R' # R
S: '{^}s' # s
S-P: '{^}S' # S
T: '{^}t' # t
T-P: '{^}T' # T
U: '{^}u' # u
PU: '{^}U' # U
SR: '{^}v' # v
SR-P: '{^}V' # V
W: '{^}w' # w
W-P: '{^}W' # W
-BGS: '{^}x' # x
P-BGS: '{^}X' # X
KWR: '{^}y' # y
KWR-P: '{^}Y' # Y
Z: '{^}z' # z
Z-P: '{^}Z' # Z
AE: '{#alt_r(a)}' # ä
AEP: '{#alt_r(shift(a))}' # Ä
OE: '{#alt_r(o)}' # ö
OEP: '{#alt_r(shift(o))}' # Ö
OU: '{#alt_r(u)}' # ü
OUP: '{#alt_r(shift(u))}' # Ü
S-S: '{#alt_r(s)}' # ß
```

## Numbers

```yaml
PW-R: '{^}1' # 1
PW-B: '{^}2' # 2
PW-G: '{^}3' # 3
PW-FR: '{^}4' # 4
PW-PB: '{^}5' # 5
PW-LG: '{^}6' # 6
PW-F: '{^}7' # 7
PW-P: '{^}8' # 8
PW-L: '{^}9' # 9
PW-E: '{^}0' # 0
```

## F-Keys

```yaml
TPW-R: '{#F1}' # F1
TPW-B: '{#F2}' # F2
TPW-G: '{#F3}' # F3
TPW-FR: '{#F4}' # F4
TPW-PB: '{#F5}' # F5
TPW-LG: '{#F6}' # F6
TPW-F: '{#F7}' # F7
TPW-P: '{#F8}' # F8
TPW-L: '{#F9}' # F9
TPWEPB: '{#F10}' # F10 (FEN)
TPWHR-L: '{#F11}' # F11 (FL-L)
TPWHR-F: '{#F12}' # F12 (FL-F)
```

## Special Keys

```yaml
-FRPB: '{}{#backspace}' # Backspace
TK-L: '{}{#delete}' # Delete
H-F: '{}{#escape}' # Escape
TPH-RT: '{}{#insert}' # Insert
R-R: '{}{#return}' # Return
T-B: '{}{#tab}' # Tab
ST-B: '{}{#shift(tab)}' # Shift-Tab
```

## Special Characters

```yaml
-PBD: '{^&}' # And
R-FBG: '{^*}' # Asterisk
PW-RT: '{^>}' # Bigger Than
S-RT: '{^<}' # Smaller Than
SPW-RT: '{^<>^}' # Smalle Than Bigger Than
T-T: '{^@}' # At
PW-RB: '{^\}' # Backslash
KPR-FR: '{^\{}' # Brace Left
KPR-FRP: '{\{}' # Brace Left (Leading space)
KPR-LG: '{^\}}' # Brace Right
KPR-PLG: '{\}}' # Brace Right (Leading space)
KPR-FRLG: '{^\{\}^}' # Brace Left and Right
SPR-FR: '{^[}' # Bracket Left
SPR-FRP: '{[}' # Bracket Left (Leading space)
SPR-LG: '{^]}' # Bracket Right
SPR-PLG: '{]}' # Bracket Right (Leading space)
SPR-FRLG: '{^[]^}' # Bracket Left and Right
TPR-FR: '{^<}' # Triange Brace Left
TPR-FRP: '{^ }{^<}' # Triange Brace Left (Leading space)
TPR-LG: '{^>}' # Triange Brace Right
TPR-PLG: '{^ }{^>}' # Triange Brace Right (Leading space)
TPR-FRLG: '{^<>^}' # Triange Brace Left and Right
KR-T: '{^}^' # Caret
K-L: '{^:}' # Colon
TWH: '{^$}' # Dollar
KW-L: '{^=}' # Equal
KWR-R: '{^€}' # Euro
T-BG: '{^!}' # Exclamation Mark
TP-BG: '{!}' # Exclamation Mark (Leading space)
H-PB: '{^-}' # Hyphen
P-RS: '{^%}' # Percent
PHR-S: '{^+}' # Plus
H-RB: '{^#}' # Hash
SK-L: '{^;}' # Semicolon
HR-RB: '{^/}' # Slash
HR-D: '{^~}' # Tilde
H-PL: '{^~}' # Tilde
PR-FR: '{^(}' # Parenthesis Left
PR-FRP: '{(}' # Parenthesis Left (Leading space)
PR-LG: '{^)}' # Parenthesis Right
PR-PLG: '{)}' # Parenthesis Right (Leading space)
PR-FRLG: '{^()^}' # Parenthesis Left and Right
T-PL: '{^.}' # Period
TP-PL: '{.}' # Period (Leading space)
K-BG: '{^,}' # Comma
KW-BG: '{,}' # Comma (Leading space)
K-PL: '{^?}' # Question Mark
KW-PL: '{?}' # Question Mark (Leading space)
TKWO: '{^"}' # Quote Double
TKWOP: '{"}' # Quote Double (Leading space)
TW-PG: '{^`}' # Quote Left
KWO: "{^'}" # Quote Single
KWOP: "{'}" # Quote Single (Leading space)
P: '{^ }' # Space
S-BG: '{^_}' # Underscore
S-BGS: '{^_}' # Underscore
SR-B: '{^|}' # Vertical Bar (should not be escaped)
```
