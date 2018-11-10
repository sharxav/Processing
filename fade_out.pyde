def setup():
    size(700,300,P3D)
    background(0)
    noStroke()

    
def draw():
    fill(0,50)
    rect(0,0,width,height)
    
    fill(255)
    ellipse(random(width),random(height),5,5)
