import tkinter as tk
import random

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("test")
        master.geometry("200x200")
        self.label = tk.Label(master, text="hai")
        self.label.pack()
        self.button1 = tk.Button(master, text="hoho", command=self.hoho)
        self.button1.pack()

    
    def hoho(self):
        for i in range(75):
            window = tk.Toplevel(self.master,background=f"#{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
            window.geometry(f"{random.randint(0,500)}x{random.randint(0,500)}+{random.randint(-100,1000)}+{random.randint(-75,500)}")
            tk.Label(window).pack()

root = tk.Tk()
GUI(root)
root.mainloop()