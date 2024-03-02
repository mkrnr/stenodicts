from os import listdir
from pathlib import Path
import json
#from plover import log
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

# TODO: find better way than hardcoding which also works with this plugin
generated_dir=f"{Path.home()}/git/stenodicts/common/generated"

STROKES={}
for file in listdir(generated_dir):
    with open(f"{generated_dir}/{file}", 'r') as f:
        STROKES.update(json.load(f))

def get_repeated_stroke(number,stroke):
    strokes=''
    for i in range(number):
        strokes+=stroke
    #log.info('\t%s',strokes)
    return strokes

def lookup(key):
    #log.info('%s',key)

    assert len(key) <= LONGEST_KEY, '%d/%d' % (len(key), LONGEST_KEY)
    
    if len(key) == 2:
        if key[0] in NUMBER_STROKES and key[1] in STROKES:
            return get_repeated_stroke(NUMBER_STROKES.get(key[0]),STROKES.get(key[1]))
    elif len(key) == 3:
        if key[0] in NUMBER_STROKES and key[1] in NUMBER_STROKES and key[2] in STROKES:
            return get_repeated_stroke(int(str(NUMBER_STROKES.get(key[0]))+str(NUMBER_STROKES.get(key[1]))),STROKES.get(key[2]))
        elif key[0] not in NUMBER_STROKES and key[1] in NUMBER_STROKES and key[2] in STROKES:
            return get_repeated_stroke(NUMBER_STROKES.get(key[1]),STROKES.get(key[2]))
    #log.info("\tKeyError")  
    raise KeyError
