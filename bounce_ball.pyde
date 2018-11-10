PaddleX=500/2
PaddleY=500/1.2
  
def setup():
    size(500,500)
    frameRate(120)
    global s,X,Y,x,y
    s=0
    X=1
    Y=2
    x=250
    y=75


def draw():
    global x,y,X,Y,s
    background(0)
    fill(random(255),random(255),random(255))
    ellipse(x,y,30,30)
    
    x=x+X
    y=y+Y
    
    if(x>width-15 or x<15):
        X=-X
            
    if(y>height-15 or y<15):
        Y=-Y    
    draw_paddle() 
    hit_ball()
    score()
    Bounce_Off()
    
    if(mousePressed):
        setup()
    
def Bounce_Off():
    global PaddleX,PaddleY    
    if(y+15==500):
        GameOver()
        background(0)
        text("GAME OVER",150,200)
        text("Score:",150,270)
        text(s,290,270)
    
def score():
    global s
    textSize(32)
    fill(255)
    text(s,100.0,100.0)
        
def draw_paddle():
    global PaddleX,PaddleY,Paddle
    fill(0,255,0) 
    rect(PaddleX,PaddleY,60,20)
    PaddleX=constrain(PaddleX,0,width-60)

def hit_ball():
    global Y,X,s
    if(y-15>PaddleY-20 and x-15<PaddleX+30 and x+15>PaddleX-30):
        Y=-Y
        s=s+1
           
def keyPressed():
    global PaddleX,PaddleY
    if(key==CODED):
        if(keyCode==LEFT):
            PaddleX=PaddleX-20
            
        if(keyCode==RIGHT):
            PaddleX=PaddleX+20
            
def GameOver():
    global s
    global X,Y
    X=0
    Y=0
    textSize(40)
    
    
    

            
                        
    
    
    
             

                       
    


            
                
            
                    
    
