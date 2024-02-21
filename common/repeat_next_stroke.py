LONGEST_KEY = 2

SHOW_STROKE_STENO = 'SRAU'

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

NAVIGATION_STROKES={
    "-FPL":"{}{#up}",
    "-RBG":"{}{#down}"
}


def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    
    if key[0] not in NUMBER_STROKES:
        raise KeyError
    if len(key) == 1:
        return ' '
    
    if key[1] not in NAVIGATION_STROKES:
        raise KeyError
    
    strokes=''
    for i in range(NUMBER_STROKES.get(key[0])):
        strokes+=NAVIGATION_STROKES.get(key[1])
    return strokes