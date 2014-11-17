# Lab 16
# 70pt -  Add in movement buttons for up, down, left and right using WASD
# 80pt -  Make sure the player can't go out of bounds to the left, right or down.
# 90pt -  When you hit space, fire a missile straight up! 
#         Subtract from how many missiles you have left
# 100pt - Destroy the target if a missile hits it! 
# Hints: use drawpad.delete(enemy) in the collision detect function, which you can trigger
# from the key press event... maybe a loop to keep checking until the rocket goes out of bounds?
from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='white')
rocket1 = drawpad.create_rectangle(400,585,405,590)
player = drawpad.create_oval(390,580,410,600, fill="blue")
car1 = drawpad.create_rectangle(50,50,100,60, fill="red")
car2 = drawpad.create_rectangle(90,30,20,10, fill="purple")
rocket1Fired = False

direction = 5
direction = -5
faste = 7


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
        global direction
        global rocket
        global rocket1Fired
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
            faste = - 7
        elif x1 < 0:
            faste = 7
        drawpad.move(car2, direction, 0)
 
            

    def key(self,event):
        global drawpad
        global player
        global rocket1Fired
        if event.char == "w":
            drawpad.move(player,0,-4)
            drawpad.move(rocket1,0,-4)
        if event.char == "s":
            drawpad.move(player,0,4)
            drawpad.move(rocket1,0,4)
        if event.char == "d":
                drawpad.move(player,4,0)
                drawpad.move(rocket1,4,0)
        if event.char == "a":
            drawpad.move(player,-4,0)
            drawpad.move(rocket1,-4,0)
        if event.char == " ":
            rocket1Fired = True
      

            
    
    def collisionDetect(self, rocket):
        rx1,ry1,rx2,ry2 = drawpad.coords(rocket)
app = myApp(root)
root.mainloop()