frames=20
pg=[None]*40
def setup():
    size(700,50)
    background(255)
    for i in range(frames):
        pg[i]=createGraphics(width,height)
        pg[i].beginDraw()
        pg[i].background(255)
        pg[i].background(random(0,255),random(0,200),random(0,255))
        pg[i].stroke(mouseX%5,0,0)
        pg[i].strokeWeight(3)
        pg[i].endDraw()
        
def draw():
    currFrame=frameCount % frames
    if(mousePressed):
        pg[currFrame].beginDraw()
        pg[currFrame].line(mouseX,mouseY,pmouseX,pmouseY)
        pg[currFrame].endDraw()
        
    image(pg[currFrame],0,0)               
        
