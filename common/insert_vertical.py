from os import listdir
 TKPWHR TKPWHR TKPWHR TKPWHR
from pathlib import Path
import json
#from plover import log

LONGEST_KEY = 20


INSERT_STROKE="R-T"
SAVE_STROKE="R-S"

MARK_LINE_STROKES = {'PH-RBG':1, 'PH-FPL':-1 }
REPEAT_NUMBER_STROKES={
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

# TODO: find better way than hardcoding which also works with this plugin
generated_dir=f"{Path.home()}/git/stenodicts/common/generated"

STROKES={}
for file in listdir(generated_dir):
    with open(f"{generated_dir}/{file}", 'r') as f:
        STROKES.update(json.load(f))


def lookup(key):
    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    #log.info(key) 
    last_stroke=key[len(key)-1]

    if last_stroke==INSERT_STROKE:
        number_of_lines=_count_rows(key) 
        if number_of_lines>0:
            #log.info("left") 
            return "{#left}"
        else:
            raise KeyError
        
    elif last_stroke==SAVE_STROKE:
        number_of_lines=_count_rows(key)
        if number_of_lines==0:
            raise KeyError
        
        strokes_to_insert=_get_strokes_to_insert(key)

        translated_strokes=[]
        for stroke_to_insert in strokes_to_insert:
            if stroke_to_insert in STROKES:
                translated_strokes.append(STROKES[stroke_to_insert])

        length=len(strokes_to_insert)
        strokes=""
        strokes+="".join(translated_strokes)
        for i in range(number_of_lines):
            if i<number_of_lines:
                for j in range(length):
                    strokes+="{#left}"
                strokes+="{#down}"
            strokes+="".join(translated_strokes)
        #log.info(strokes)
        return strokes


    
    raise KeyError

def _count_rows(key):
    found_insert_stroke=False
    movement_strokes=[]
    for stroke in reversed(key):
        if stroke==INSERT_STROKE:
            if found_insert_stroke:
                break
            else:
                found_insert_stroke=True
        elif found_insert_stroke:
            if stroke in MARK_LINE_STROKES  or stroke in REPEAT_NUMBER_STROKES:
                movement_strokes.insert(0,stroke)
            else:
                # only consider sequences where the first stroke is a movement related stroke
                return 0
    rows=0
    multiplier=None
    for movement_stroke in movement_strokes:
        if movement_stroke in REPEAT_NUMBER_STROKES:
            if multiplier:
                multiplier=int(str(multiplier)+str(REPEAT_NUMBER_STROKES[movement_stroke]))
            else:
                multiplier= REPEAT_NUMBER_STROKES[movement_stroke]
        else:
            if movement_stroke in MARK_LINE_STROKES:
                if multiplier:
                    rows+=multiplier*MARK_LINE_STROKES[movement_stroke]
                    multiplier=None
                else:
                    rows+=MARK_LINE_STROKES[movement_stroke]

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



