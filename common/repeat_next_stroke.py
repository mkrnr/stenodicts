LONGEST_KEY = 3

NUMBER_STROKES={
    "PWH-F":1,
    "PWH-P":2,
    "PWH-FP":3,
    "PWH-L":4,
    "PWH-FL":5,
    "PWH-PL":6,
    "PWH-FPL":7,
    "PWH-T":8,
    "PWH-FT":9,
    "PWH-R":0,
}

STROKES={
    "-FPL":"{}{#up}",
    "-RBG":"{}{#down}",
    "KWRO":"{#command(v)}",
}


def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    
    if key[0] not in NUMBER_STROKES:
        raise KeyError
    if len(key) == 1:
        return ' '
    number=NUMBER_STROKES.get(key[0])

    if key[1] in NUMBER_STROKES:
        if len(key) == 2:
            return ' '
        number=int(str(number)+str(NUMBER_STROKES.get(key[1])))
        if key[2] not in STROKES:
            raise KeyError
        stroke=STROKES.get(key[2])
    else:
        if key[1] not in STROKES:
            raise KeyError
        
        stroke=STROKES.get(key[1])
    strokes=''
    for i in range(number):
        strokes+=stroke
    return strokes