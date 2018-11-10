def setup():
    global viewport;
    size(700,300,P3D);
    
def draw():
    background(255);
    translate(mouseX,mouseY);
    sphere(100);
    fill(mouseX/6,mouseY/3,mouseX/5);
    rotate(mouseX);
