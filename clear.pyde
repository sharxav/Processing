def setup():
    global viewport;
    size (700,300,P3D)
    

    
def draw():
    #background(255);
    translate(mouseX,mouseY);
    ellipse(60,60,60,60);
    
    stroke(mouseX/6,mouseY/5,mouseX/2);
    strokeWeight(10);
    
def mousePressed():
    background(255);
    
    
    
