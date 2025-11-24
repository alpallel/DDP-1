import tkinter as tk
import random
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("test")
        master.geometry("200x60+530+300")
        self.label = tk.Label(master, text="hai :)")
        self.label.pack()
        self.button1 = tk.Button(master, text="press for surprise", command=self.surprise)
        self.button1.pack()

    def surprise(self):
        bg = tk.PhotoImage(file="C:\\Users\\alpal\\OneDrive\\Documents\\ngoding\\ddp1\\monke.gif")
        for i in range(150):
            # window = tk.Toplevel(self.master, background=f"#{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}{random.randint(0,9)}")
            window = tk.Toplevel(self.master)
            window.geometry(f"{random.randint(00,700)}x{random.randint(00,700)}+{random.randint(-150,1160)}+{random.randint(-125,650)}")
            window.title("hai :)")
            tk.Label(window, text=("hai :) "*100 + "\n")*100).pack()
            window.lower(self.master)

root = tk.Tk()
GUI(root)
root.mainloop()