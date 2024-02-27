import re
LONGEST_KEY = 4

INITIAL_STROKES = {'PH-RBG':'{#shift(down)}',
'PH-FPL':'{#shift(up)}'}

INSERT_STROKE="R-T"

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


    # TODO detect and count row movement strokes
    # TODO raise KeyError when aborting movement strokes
    if len(key) == 1:
        return INITIAL_STROKES.get(key[0])
    number_of_lines=2
    
    # last stroke is insert stroke
    if key[len(key)-1]==INSERT_STROKE:
        return "{#left}"

    #TODO detect strokes between insert stroke and confirm/abort stroke
    if len(key)==3:
        return STROKES.get(key[len(key)-1])

    if key[len(key)-3]==INSERT_STROKE:
        #negative=up, positive=down
        rows=count_rows(key)

        #completed_process=subprocess.run(["pbpaste","-Prefer","txt"],text=True,capture_output=True)
        #text=completed_process.stdout
        if key[len(key)-2] not in STROKES:
            raise KeyError
        stroke=STROKES.get(key[len(key)-2])
        text=extract_text_from_plover_stroke(stroke)
        length=len(text)
        #left repeat(paste len-paste-left down)
        strokes=""
        for i in range(number_of_lines):
            strokes+=stroke
            if i<number_of_lines-1:
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
    



