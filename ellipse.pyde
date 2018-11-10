import random
x=70
speed=5
radius=25
y=387.5
X=400
Y=340
H=60
def setup():
    size(500,500)
    background(255)
    frameRate(50)
    smooth()
    
def draw():
    global radius
    fill(152,120,0)
    noStroke()
    rect(0,400,500,100)
    fill(255,0,0)
    ellipse(x,y,radius,radius)
    obstacle()
    move()
      
    
def keyPressed():
    global x,y,radius,X
    if(keyCode==RIGHT and x<width-(radius/2)):
        fill(255)
        noStroke()
        background(255)
        fill(152,120,0)                            
        noStroke()
        rect(0,400,500,100)
        x=x+speed
    if(keyCode==LEFT and x>(radius/2)):
        fill(255)
        noStroke()
        background(255)
        fill(152,120,0)                            
        noStroke()
        rect(0,400,500,100)
        x=x-speed
    if(keyCode==UP and y>(radius/2)):
        fill(255)
        noStroke()
        background(255)
        fill(152,120,0)                            
        noStroke()
        rect(0,400,500,100)
        y=y-speed   
    if(keyCode==DOWN and y<height-(radius/2)):
        fill(255)
        noStroke()
        background(255)
        fill(152,120,0)                            
        noStroke()
        rect(0,400,500,100)
        y=y+speed 
        
    if(keyCode==LEFT and X>0):
        fill(255)
        noStroke()
        background(255)
        fill(152,120,0)                            
        noStroke()
        rect(0,400,500,100)
        X=X-speed   
        
def obstacle():
    global X,Y,H
    fill(152,120,0)
    noStroke()
    rect(0,400,500,100)
    fill(0)
    rect(X,Y,20,H)
    X=X
    
def move():
    global speed,X
    X=X-speed
    if X <= 0 :
        X=780
        H= random.randrange(20, 50)
        Y= 200 - H

    
    
                    
        
