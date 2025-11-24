import tkinter as tk
import random

class GUI:

    #TODO HIASS(font, warna, dll)
    def __init__(self, master):
        self.master = master
        master.title("Suit")
        master.geometry("400x200")

        self.label = tk.Label(master, text="Para Clanker Menginvasi Bumi!!!\nAnda adalah harapan terakhir umat manusia!\nKalahkan clanker-clanker itu dengan main suit!!\n\nBeritahu Kami Nama Anda")
        self.label.pack()

        self.entry = tk.Entry(master, width=30)
        self.entry.pack()

        self.button1 = tk.Button(text="Mulai", command=self.game_start)
        self.button1.pack()

    def game_start(self):

        # Hapus semua widget di __init__
        self.label.destroy()
        self.entry.destroy()
        self.button1.destroy()

        # Variables
        master = self.master
        self.bot_choice = random.choice(["batu","gunting","kertas"])

        print(self.bot_choice) #TODO for debugging purposes (REMOVE THIS WHEN DONE)

        # Components
        #TODO HIASSSS (font, warna, dll apa gitu)
        self.label = tk.Label(master, text="Pilih senjata anda!")
        self.label.pack()
        
        self.batu = tk.Button(master, text="batu", command=lambda: self.game_result("batu"))
        self.batu.pack()

        self.gunting = tk.Button(master, text="gunting", command=lambda: self.game_result("gunting"))
        self.gunting.pack()

        self.kertas = tk.Button(master, text="kertas", command=lambda: self.game_result("kertas"))
        self.kertas.pack()

    def game_result(self, user_choice):

        # variable bot_choice untuk mempersingkat code
        bot = self.bot_choice

        # Mencoba menghapus label2. Jika belum ada label2 (pertamakali func game_result dipanggil), program lanjut
        try:
            self.label2.destroy()
        except:
            pass

        # Inisiasi variable label2
        self.label2 = tk.Label(self.master)
        
        # If statements membandingkan input user dan bot
        if user_choice == bot:
            self.label2.destroy()

            #TODO Hias
            self.label2 = tk.Label(self.master, text=f"Clanker itu menggunakan {bot}! Anda seri! Jangan sampai kalah!")
            self.label2.pack(side='bottom')
        
        elif (user_choice == "batu" and bot == "gunting") or \
            (user_choice == "gunting" and bot == "kertas") or\
            (user_choice == "kertas" and bot == "batu"):

            self.label2.destroy()

            #TODO Hias🙏
            self.label2 = tk.Label(self.master, text=f"Clanker itu menggunakan {bot}! Anda menang :) Terus maju!")
            self.label2.pack(side='bottom')
        
        #TODO tambahin game over (opsional)
        else:
            self.surprise()
            

        # Hapus semua component kemudian memanggil func game_start untuk memunculkannya kembali
        self.label.destroy()
        self.batu.destroy()
        self.gunting.destroy()
        self.kertas.destroy()
        self.game_start()

    # Spam pop-up
    def surprise(self):
        for i in range(100):
            window = tk.Toplevel(self.master, bg='red')
            window.geometry(f"{random.randint(00,700)}x{random.randint(00,700)}+{random.randint(-150,1160)}+{random.randint(-125,650)}")
            window.title("Yah kalah :( ")
            #TODO optional hias
            tk.Label(window, text=("kalahh :(  "*100 + "\n")*100,bg='red').pack()
            window.lower(self.master)

root = tk.Tk()
GUI(root)
root.mainloop()