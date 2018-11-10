#c=color(0)
x=0.0
y=300.0
speed=5.0

def setup():
    size(800,800)
    
def draw():
    background(255);
    move()
    display()
    
def move():
    global x
    x=x+speed
    if x>width:
        x=0
        
def display():
    fill(x/4,y,x/2)
    rect(x,y,40,20)                                
