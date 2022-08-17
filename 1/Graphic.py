# from ast import Pass
# from re import X
import tkinter as tk
import numpy as num
import pandas as panda


# -----------------------------------------------------
# Area for class

class Veiw_triangle():

    def __init__(self) -> None:
        pass
        self.can = tk.Canvas(root,width=600,height=600)
        self.can.place(x=0,y=0)
        self.id1 = self.can.create_polygon(300,500,100,100,500,100,fill="green")
        self.can.move(self.id1,-100,0)



class Learn_canvas():

    def __init__(self) -> None:
        self.c = tk.Canvas(root,bg="white",width=500,height=500)
        self.c.place(x=10,y=10)
        pass

    
    def draw(self):
        id1 = self.c.create_line(10,10,400,400,fill="red",tag="line")
        id2 = self.c.create_rectangle(30,30,300,300,fill="green",tag="rect")
        id3 = self.c.create_polygon(10,10
                                    ,100,400
                                    ,400,70,fill="red",tag='poly1')
        # self.c.delete("rect")
        self.c.delete(id3)
        # self.c.delete(id1)
        # self.c.move(id1,300,100)
        self.c.scale(id1,10,10,10,1)
        self.c.move(id1,10,100)
        self.point = self.c.coords(id1)
        self.point[0:2]=[100,100]
        self.c.coords(id1,self.point)
        self.c.lift(id1,id2)
        self.c.lower(id1,id2)

        pass

# End area for class
# -----------------------------------------------------



root = tk.Tk()
root.geometry("600x600")
root.title("Hello world in 3D!")


# -----------------------------------------------------
# Use class

# ins1 = Learn_canvas()
# ins1.draw()

ins2 = Veiw_triangle()

root.mainloop()





