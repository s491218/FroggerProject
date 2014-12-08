from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='blue')
Grass = drawpad.create_rectangle(0,250,800,600, fill="green")
Road = drawpad.create_rectangle(0,425,800,510, fill="grey")
Road1 = drawpad.create_rectangle(0,290,800,350, fill="grey")
car1 = drawpad.create_rectangle(350,465,400,490, fill="red")
car2 = drawpad.create_rectangle(350,435,400,460, fill="red")
bug = drawpad.create_rectangle(350,300,400,330, fill="purple")
log = drawpad.create_rectangle(350,200,450,230, fill="brown")
log2 = drawpad.create_rectangle(350,150,450,180, fill="brown")
log3 = drawpad.create_rectangle(350,100,450,130, fill="brown")
Finish = drawpad.create_rectangle(0,0,810,90, fill="dark gray")
player = drawpad.create_oval(390,580,410,600, fill="light green")

direction = 3
direction = -3
fast = 3
bugfast = 7
logspeed = 2
logspeed1 = -3
logspeed2 = 4

class myApp(object):
    def __init__(self, parent):
        
        global drawpad
        self.myParent = parent  
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        drawpad.pack()
        root.bind_all('<Key>', self.key)
        self.animate()
        





    
    def animate(self):
        global drawpad
        global enemy
        global fast
        global direction
        global bugfast
        global logspeed
        global logspeed1
        global logspeed2

        x1,y1,x2,y2 = drawpad.coords(car1)
        px1,py1,px2,py2 = drawpad.coords(player)

        if x2 > 800:
            direction = - 3
        elif x1 < 0:
            direction = 3
        drawpad.move(car1, direction, 0)
        drawpad.after(5,self.animate)
        x1,y1,x2,y2 = drawpad.coords(car2)
        if x2 > 800:
            fast = - 3
        elif x1 < 0:
            fast = 3
        drawpad.move(car2, fast, 0)
        x1,y1,x2,y2 = drawpad.coords(bug)
        if x2 > 800:
            bugfast = - 7
        elif x1 < 0:
            bugfast = 7
        drawpad.move(bug, bugfast, 0)
        x1,y1,x2,y2 = drawpad.coords(log)
        if x2 > 800:
            logspeed = -2
        elif x1 < 0:
            logspeed = 2
        drawpad.move(log, logspeed, 0)
        x1,y1,x2,y2 = drawpad.coords(log2)
        if x2 > 800:
            logspeed1 = - 3
        elif x1 < 0:
            logspeed1 = 3
        drawpad.move(log2, logspeed1, 0)
        x1,y1,x2,y2 = drawpad.coords(log3)
        if x2 > 800:
            logspeed2 = - 4
        elif x1 < 0:
            logspeed2 = 4
        drawpad.move(log3, logspeed2, 0)



    def key(self,event):
        global drawpad
        global player
        x1,y1,x2,y2 = drawpad.coords(player)
        if event.char == "w":
            if y1 <= 0:
                drawpad.move(player,0,30)
            else: 
                drawpad.move(player,0,-30)
        if event.char == "s":
            if y2 >= 600:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,0,30)
        if event.char == "d":
            if x2 >= 800:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,30,0)
        if event.char == "a":
            if x1 <= 0:
                drawpad.move(player,0,0)
            else: 
                drawpad.move(player,-30,0)
                

            
#Cant make this work for some reason    
    def collisionDetect(self):
        global car1
        global car2
        global bug
        global finish
        px1,py1,px2,py2 = drawpad.coords(player)
        c1x1,c1y1,c1x2,c1y2 = drawpad.coords(car1)
        c2x1,c2y1,c2x2,c2y2 = drawpad.coords(car2)
        bx1,by1,bx2,by2 = drawpad.coords(bug)
        fx1,fy1,fx2,fy2 = drawpad.coords(finish)
        if (px1 > fx1 and px2 < fx2)and(py1 > fy1 and py2 < fy2):
            print hit
        if (px1 < c1x1 and px2 > c1x2)and(py1 > c1y1 and py2 < c1y2):
            print hit
        if (px1 > bx1 and px2 < bx2)and(py1 < by1 and py2 > by2):
            print hit






            
app = myApp(root)
root.mainloop()