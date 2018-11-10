x=150
y=150
def setup():
    size(300,300)
    
    
def draw():
    global x,y
    background(255)
    fill(255,0,0)
    ellipse(x,y,20,20) 
    fill(0)
    rect(0,160,300,150)
    
def keyPressed():
    global x,y
    if(key==CODED):
        if(keyCode==LEFT):
            x=x-20
            
        if(keyCode==RIGHT):
            x=x+20
            
        if(keyCode==UP):
            y=y-20
            
        if(keyCode==DOWN):
            y=y+20   
                      
