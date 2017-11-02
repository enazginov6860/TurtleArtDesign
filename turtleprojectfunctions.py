def rainbowsnow (t,size,x,y):
        move (t,x,y)
        t.begin_fill ()
        t. color ()
        t.circle (size)
        t.end_fill ()


def rainbowsnowflake (t):
    angle= 1
    t.begin_fill ()
    move (t,0,0)
    
    t.color (255,0,0)
    star (t,500)
    t.left (angle)
    
    t.color (255,0,255)
    star (t,450)
    t.left (angle)
    
    t.color (255,255,0)
    star (t,400)
    t.left (angle)
   
    t.color (0,255,255)
    star (t,350)
    t.left (angle)
   
    t.color (0,255,0)
    star (t,300)
    t.left (angle)
    
    t.color (0,0,255)
    star (t,250)
    t.left (angle)
  
    t.color (90,230,255)
    star (t,200)
    t.left (angle)
   
    t.color (255,0,0)
    star (t,150)
    t.left (angle)
   
    t.color (246,30,90)
    star (t,100)
    t.left (angle)
   
    t.color (8,255,60)
    star (t,50)
    t.left (angle)
    t.color (255,255,255)
    t.end_fill ()


        
def polygon (t,distance, side):
    angle= 360/side
    t.begin_fill ()
    for times in range (side):
        t.forward (distance)
        t.left (angle)
        t.end_fill ()



def move (t,x,y):
    t.penup ()
    t.goto (x,y)
    t.pendown ()


def star (t,distance):
    angle= 135
   
   
    for times in range (4):
        t.forward (distance)
        t.left (angle)

