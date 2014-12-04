from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='gray')
player = drawpad.create_oval(390,580,410,600, fill="blue")
car1 = drawpad.create_rectangle(50,50,100,60, fill="red")
car2 = drawpad.create_rectangle(50,50,100,60, fill="red")



direction = 5
direction = -5
fast = 7


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
        x1,y1,x2,y2 = drawpad.coords(car1)
        px1,py1,px2,py2 = drawpad.coords(player)

        if x2 > 800:
            direction = - 5
        elif x1 < 0:
            direction = 5
        drawpad.move(car1, direction, 0)
        drawpad.after(5,self.animate)
        x1,y1,x2,y2 = drawpad.coords(car2)
        if x2 > 800:
            fast = - 7
        elif x1 < 0:
            fast = 7
        drawpad.move(car2, fast, 0)
 
            

    def key(self,event):
        global drawpad
        global player
        if event.char == "w":
            drawpad.move(player,0,-4)
        if event.char == "s":
            drawpad.move(player,0,4)
        if event.char == "d":
                drawpad.move(player,4,0)
        if event.char == "a":
            drawpad.move(player,-4,0)

            
    
    def collisionDetect(self, player):
        rx1,ry1,rx2,ry2 = drawpad.coords(player)
            
app = myApp(root)
root.mainloop()