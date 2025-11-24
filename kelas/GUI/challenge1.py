import tkinter as tk
import random

class GUI:
    def __init__(self, master):
        self.colors = ['red','green','blue','yellow','cyan','lime']
        self.radius = 100
        self.random_color = random.choice(self.colors)

        self.master = master

        self.canvas_w = 200
        self.canvas_h = 200
        self.canvas = tk.Canvas(master, width=self.canvas_w, height=self.canvas_h, bg='white')
        x0 = (self.canvas_w - self.radius) // 2
        y0 = (self.canvas_h - self.radius) // 2
        x1 = x0 + self.radius
        y1 = y0 + self.radius
        self.oval_id = self.canvas.create_oval(x0, y0, x1, y1, fill=self.random_color)
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.add_radius)
        self.canvas.bind('<Button-3>', self.subtract_radius)

    def add_radius(self, event=None):
        self.radius += 2
        max_size = min(self.canvas_w, self.canvas_h)
        self.radius = min(self.radius, max_size)
        self.new_color()
        self.redraw_oval()
        
    def subtract_radius(self, event=None):
        self.radius = max(10, self.radius - 2)
        self.new_color()
        self.redraw_oval()

    def redraw_oval(self):
        try:
            self.canvas.delete(self.oval_id)
        except:
            pass
        x0 = (self.canvas_w - self.radius) // 2
        y0 = (self.canvas_h - self.radius) // 2
        x1 = x0 + self.radius
        y1 = y0 + self.radius
        self.oval_id = self.canvas.create_oval(x0, y0, x1, y1, fill=self.random_color)

    def new_color(self):
        if not self.colors:
            return
        new = self.random_color
        attempts = 0
        while new == self.random_color and attempts < 10 and len(self.colors) > 1:
            new = random.choice(self.colors)
            attempts += 1
        self.random_color = new

root = tk.Tk()
GUI(root)
root.mainloop()