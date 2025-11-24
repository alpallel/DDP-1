import tkinter as tk
import random


class Grid:
    def __init__(self, master):
        self.master = master
        self.rows = 8
        self.colls = 8
        self.cell_size = 40
        self.colors = ['black', 'white']

        self.save_button = tk.Button(master, text='save to map.eps', command=self.save)
        self.save_button.pack(pady=4)

        self.canvas_width = self.colls * self.cell_size
        self.canvas_height = self.rows * self.cell_size

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack(padx=10, pady=10)

        self.rects = [[None for _ in range(self.colls)] for _ in range(self.rows)]
        self.create_grid()
        self.generate_bitmap()
        self.canvas.bind('<Double-Button-1>', lambda e: self.generate_bitmap())

    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.colls):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                rect = self.canvas.create_rectangle(x0, y0, x1, y1, outline='', fill='white')
                self.rects[i][j] = rect

    def generate_bitmap(self):
        for i in range(self.rows):
            for j in range(self.colls):
                color = random.choice(self.colors)
                rect = self.rects[i][j]
                self.canvas.itemconfig(rect, fill=color)

    def save(self):
        filename = 'map.eps'
        self.canvas.postscript(file=filename, colormode='color')

root = tk.Tk()
grid = Grid(root)
root.mainloop()