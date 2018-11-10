def setup():
    size(700,300,P3D)
    background(0,150,255)
    noFill()
    
def draw():
    strokeWeight(random(3,10))
    stroke(random(255),random(255),random(255),random(255))
    rainbow_size=random(600,750)
    ellipse(700,300,rainbow_size,rainbow_size)
