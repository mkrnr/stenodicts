import subprocess

LONGEST_KEY = 4

INITIAL_STROKES = {'SPW-RBG':'{#shift(down)}',
'SPW-FPL':'{#shift(up)}'}

PASTE_STROKE="KWRO"

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
}

ROWS=0


def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    
    if key[0] not in INITIAL_STROKES:
        raise KeyError

    if len(key) == 1:
        return INITIAL_STROKES.get(key[0])
    

    # TODO raise KeyError when none movement and none paste command

    
    # TODO use different paste command
    if key[len(key)-1]=="KWRO":
        #negative=up, positive=down
        rows=count_rows(key)

        completed_process=subprocess.run(["pbpaste","-Prefer","txt"],text=True,capture_output=True)
        text=completed_process.stdout

        length=len(text)
        return "{}{#Left}{^}"+f"X{length}X"
    
    raise KeyError



def count_rows(key):
    rows=0
    current_multiplier=1
    for stroke in key:
        if stroke=='SPW-RBG':
            rows+=1
        elif stroke=='SPW-FPL':
            rows-=1
    return rows
    



