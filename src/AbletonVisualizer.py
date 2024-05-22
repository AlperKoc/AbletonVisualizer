import py5
import time
import csv

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

# # DUMMY DATA CONFIG
# kick_slices = 30
# hihat_slices = 30
# beats = 1000

# # DUMMY
# kick = ([i for i in range(kick_slices/2,0,-1)] +\
#         [i for i in range(0,kick_slices/2,1)]) * beats 

# hihat = ([i for i in range(0,hihat_slices/2,1)] + \
#          [i for i in range(hihat_slices/2,0,-1)]) * beats

instruments = {}

# APP CONFIG
W = 500
FPS = 30
# img = loadImage('bg.png')
# img.resize(W,W)

frameCount = 0

def setup():
    global instruments
    global img
    global frameCount
    py5.size(W,W)
    py5.frame_rate(FPS)
    with open("data/Test.csv", "r") as infile:
        reader = csv.reader(infile)
        headers = next(reader)[1:]
        for row in reader:
            instruments[row[0]] = {key: value for key, value in zip(headers, row[1:])}

    print(instruments)
    
def draw():
    
    tiles = 50
    tileSize = W/tiles
    global frameCount
    
    for x in range(tiles):
        for y in range(tiles):
            pass
            # c = img[100]#[int(x*tileSize),int(y*tileSize)]
            
    # background(0,0,0,0)
    frm = frameCount % len(instruments.keys())
    frameCount+=1
    
    kick_size = float(instruments[str(frm)]['Kick_Size'])
    kick_pan = float(instruments[str(frm)]['Kick_Pan'])
    hihat = float(instruments[str(frm)]['Hihat'])
    clap = float(instruments[str(frm)]['Clap'])
    bass = float(instruments[str(frm)]['Bass'])

    shape_circular(inst = kick_size,
                   fill_ = None,
                   stroke_ = _green+[255],
                   degrees_ = kick_size,
                   origin_ = [250,250],
                   detail_=1)
    
    shape_circular(inst = kick_pan,
            fill_ = None,
            stroke_ = _green+[255],
            degrees_ = kick_pan,
            origin_ = [125,125],
            detail_=1)
    shape_circular(inst = hihat,
            fill_ = None,
            stroke_ = _green+[255],
            degrees_ = hihat,
            origin_ = [375,375],
            detail_=1)
    shape_circular(inst = clap,
            fill_ = None,
            stroke_ = _green+[255],
            degrees_ = clap,
            origin_ = [125,375],
            detail_=1)
    shape_circular(inst = bass,
            fill_ = None,
            stroke_ = _green+[255],
            degrees_ = bass,
            origin_ = [375,125],
            detail_=1)
    
    
    
    
    
    # shape_circular(inst = clap,
    #                fill_ = None,
    #                stroke_ = _green+[255],
    #                degrees_ = clap,
    #                origin_ = [250,250])
    
    
    
    
  
def shape_circular(inst,
                   fill_,
                   stroke_,
                   degrees_,
                   origin_,
                   detail_):
 
    if fill_:
        py5.fill(*fill_)
    else:
        py5.no_fill()
    
    if stroke_:
        py5.stroke(*stroke_)
    else:
        py5.no_stroke()
    
    radians_ = degrees_ *  py5.PI/180
    
    py5.push_matrix()
    py5.translate(origin_[0],origin_[1])
    py5.rotate(radians_)
    for i in range(0,80,detail_):
        cc = _green+[inst+50]
        cc[1] -= i*2
        py5.stroke(*cc)
        py5.circle(0,0,inst-i )
        # line(0,0,100,100)

    py5.pop_matrix()
    
  
py5.run_sketch()
