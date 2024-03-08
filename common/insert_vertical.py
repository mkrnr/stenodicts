import re
LONGEST_KEY = 20

MARK_LINE_STROKES = {'PH-RBG':'{#shift(down)}',
'PH-FPL':'{#shift(up)}'}

INSERT_STROKE="R-T"
SAVE_STROKE="R-S"

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
    
    last_stroke=key[len(key)-1]

    if last_stroke==INSERT_STROKE:
        number_of_lines=_count_rows(key) 
        if number_of_lines!=0:
            return "{#left}"
        else:
            raise KeyError
        
    elif last_stroke==SAVE_STROKE:
        #negative=up, positive=down
        number_of_lines=_count_rows(key)
        if number_of_lines==0:
            raise KeyError
        
        strokes_to_insert=_get_strokes_to_insert(key)

        #TODO make sure that strokes are only individual keys
        translated_strokes=[]
        for stroke_to_insert in strokes_to_insert:
            if stroke_to_insert in STROKES:
                translated_strokes.append(STROKES[stroke_to_insert])

        length=len(strokes_to_insert)
        strokes=""
        #TODO handle moving up (negative number of lines)
        for i in range(number_of_lines):
            if i<number_of_lines:
                for j in range(length):
                    strokes+="{#left}"
                strokes+="{#down}"
            strokes+="".join(translated_strokes)
        return strokes


    
    raise KeyError

def _count_rows(key):
    rows=0
    found_insert_stroke=False
    for stroke in reversed(key):
        if stroke==INSERT_STROKE:
            if found_insert_stroke:
                break
            else:
                found_insert_stroke=True
        elif found_insert_stroke:
            if stroke=='PH-RBG':
                rows+=1
            elif stroke=='PH-FPL':
                rows-=1
            #TODO add repeated strokes
            else:
                break
    return rows
    

def _get_strokes_to_insert(key):
    found_save_stroke=False
    strokes_to_insert=[]
    for stroke in reversed(key):
        if stroke==SAVE_STROKE:
            if found_save_stroke:
                return []
            else:
                found_save_stroke=True
        elif stroke==INSERT_STROKE:
            return strokes_to_insert
        else:
            strokes_to_insert.insert(0,stroke)



