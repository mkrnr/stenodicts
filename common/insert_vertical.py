import subprocess
import re
LONGEST_KEY = 4

INITIAL_STROKES = {'PH-RBG':'{#shift(down)}',
'PH-FPL':'{#shift(up)}'}

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
    "H-RB":"{^#}",
    "-RBG":"{}{#down}",
}

ROWS=0


def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    
    if key[0] not in INITIAL_STROKES:
        raise KeyError

    if len(key) == 1:
        return INITIAL_STROKES.get(key[0])
    if len(key) !=4:
        raise KeyError

    #TODO count how many lines down
    number_of_lines=2

    # TODO raise KeyError when none movement and none paste command

    
    # TODO use different paste command
    if key[len(key)-3]=="-PBS":
        #negative=up, positive=down
        rows=count_rows(key)

        #completed_process=subprocess.run(["pbpaste","-Prefer","txt"],text=True,capture_output=True)
        #text=completed_process.stdout
        if key[len(key)-2] not in STROKES:
            raise KeyError
        text=extract_text_from_plover_stroke(STROKES.get(key[len(key)-2]))
        length=len(text)
        #left repeat(paste len-paste-left down)
        strokes="{}{#left}"
        for i in range(number_of_lines):
            strokes+="{^}"+text
            for j in range(length):
                strokes+="{#left}"
            strokes+="{#down}"
        return strokes
    
    raise KeyError

def extract_text_from_plover_stroke(stroke):
    stroke=re.sub("^{\^","",stroke)
    stroke=re.sub("^{","",stroke)
    stroke=re.sub("}$","",stroke)
    return stroke

def count_rows(key):
    rows=0
    current_multiplier=1
    for stroke in key:
        if stroke=='SPW-RBG':
            rows+=1
        elif stroke=='SPW-FPL':
            rows-=1
    return rows
    



