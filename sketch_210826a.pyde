angulo=-PI/2


def setup():
    size (400,250)
    

def draw():
    global s
    global m
    global h
    s = map( second(),0,60, -PI/2, 3*PI/2)    
    m = map( minute(), 0, 60, -PI/2, 3*PI/2)
    h = map( hour(), 0, 24, -PI/2, 3*PI/2)
    background(0)

    noStroke()
    
    fill(0,255,10)
    arc(350, height/2, 80, 80, -PI/2,s)
    fill(245,2,11)
    arc(width/2, height/2, 80, 80, -PI/2,m)
    fill(2,210,245)
    arc(45, height/2, 80, 80, -PI/2,h)
