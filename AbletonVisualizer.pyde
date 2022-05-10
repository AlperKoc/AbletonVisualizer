# add_library('Ani')
import time
import csv

# print(Ani)
# TIMER START
start_time = time.time()

# COLORS
_pink = [209,45,127]
_pink_dark = [138,26,66]

_yellow = [251,233,78]
_yellow_dark = [244,191,66]
_yellow_darker = [188,122,44]

_turquoise = [117,250,253]
_green = [56,125,98]

_white = (255,255,255)
_black = [0,0,0]

# DUMMY DATA CONFIG
kick_slices = 30
hihat_slices = 30
beats = 1000

# DUMMY
kick = ([i for i in range(kick_slices/2,0,-1)] +\
        [i for i in range(0,kick_slices/2,1)]) * beats 

hihat = ([i for i in range(0,hihat_slices/2,1)] + \
         [i for i in range(hihat_slices/2,0,-1)]) * beats

instruments = {}

# APP CONFIG
W = 500
FPS = 25
def setup():
    global ani
    global instruments
    size(W,W)
    frameRate(FPS)
    # print(Ani.SINE_IN)
    
    mydict = {}

    dict1 = {}

    with open("Test.csv", "rb") as infile:
        reader = csv.reader(infile)
        headers = next(reader)[1:]
        for row in reader:
            dict1[row[0]] = {key: value for key, value in zip(headers, row[1:])}
            # break
    print(dict1)
        # print(dict1)

    instruments = dict1
    print(instruments.keys())
    
def draw():
    
    
    frm = frameCount % len(instruments.keys())
    background(0,0,0,0)

    # KICK
    # if frameCount % kick_slices > 15:
    #     fill(*_black)
    # else:
    #     fill(*_green+[255])
    
    
    
    # circle(250,250,kick[frameCount]* 2 )
    # print(instruments[frm])
    circle(250,250,float(instruments[str(frm)]['Kick_Size']) )

    # HIHAT
    
    fill(*_yellow+[255])
    
    
    fill(*_green+[255])
    circle(375,125,float(instruments[str(frm)]['Hihat'])*  1)
    
    
    fill(*_green+[255])
    circle(125,125,float(instruments[str(frm)]['Bass'])*  1)

    
    fill(*_green+[255])
    circle(375,375,float(instruments[str(frm)]['Clap'])*  1)

    # circle(375,125,20)
    current_seconds = time.time() - start_time


        
# 110 beats per minute
# 1.835 beats per second
# 0.5455 seconds per beat - 2.1818
# 0.061 beats per frame

#
            
# 120 beats per minute
# 2 beats per second
# 0.5 seconds per beat - 2
# 0.067 beats per frame

# 15 frames per beat for 120 bpm

  
