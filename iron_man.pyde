def setup():
    size(1000,1000)
    #background(0)

    
def draw():
    ambientLight(102,102,102)
    body()
    head()
    helmet()
    eyes()
    mouth()
    legs()
    arms()
    
   
def head():     
    beginShape()
    fill('#AA0505')
    vertex(300,300)
    vertex(300,400)
    vertex(350,450)
    vertex(400,450)
    vertex(450,400)
    vertex(450,300)
    arc(375,300,150,100,PI,2*PI)
    endShape()
    
def helmet():
    beginShape()
    fill('#B97D10')
    vertex(310,300)
    vertex(330,280)
    vertex(350,280)
    vertex(360,300)
    vertex(390,300)
    vertex(410,280)
    vertex(430,280)
    vertex(440,300)
    vertex(440,400)
    vertex(400,440)
    vertex(350,440)
    vertex(310,400)
    vertex(310,300)
    
    
    endShape()
    
    
    
def eyes():
    
    fill('#67C7EB')
    rect(315, 320, 40, 13, 3, 6, 12, 18)
    rect(390, 320, 40, 13, 3, 6, 12, 18)
    strokeWeight(3)
    
def mouth():
    line(350,400,400,400)    
    line(350,400,342,405)
    line(400,400,408,405)
   
def body():
    fill('#AA0505')
    rect(300,450,150,200,3,6,12,18)    
    line(300,490,340,550)
    line(340,550,410,550)
    line(410,550,450,490)
    line(340,550,350,590)
    line(350,590,400,590)
    line(400,590,410,550)
    line(342,564,406,564)
    line(345,576,404,576)
    fill('#AA0505')
    ellipse(375,510,45,45)
    fill('#67C7EB')
    ellipse(375,510,35,35)
    fill('#B97D10')
    rect(300,550,40,12)
    rect(300,575,45,12)
    rect(404,575,45,12)
    rect(407,550,42,12)
    
def legs():
    fill('#B97D10')
    rect(320,650,40,60)
    rect(390,650,40,60)
    fill('#AA0505')
    rect(390,690,40,30, 3, 6, 12, 18)
    rect(320,690,40,30, 3, 6, 12, 18)
    
def arms():
    fill('#B97D10')
    rect(270,460,30,120,6, 10, 30, 50)  
    rect(450,460,30,120,6, 10, 30, 50)  
    fill('#AA0505')
    ellipse(285,570,35,30)
    ellipse(465,570,35,30)
    rect(270,450,30,15,3,8,12,18)
    rect(450,450,30,15,3,8,12,18)
    

      

    
