try:    
    nama_file = input("Masukkan file yang akan di decode: ")
    with open(nama_file, "r", encoding="utf-8", errors="ignore") as f:
        f = f.read()
        
except FileNotFoundError:
    print("File tidak ditemukan")

data_binary = ""
for line in f:
    for ch in line:
        if ch == "\u200b":
            data_binary += "0"
        elif ch == "\u200c":
            data_binary += "1"

biner = []
for i in range(0, len(data_binary), 8):
    bit = data_binary[i:i+8]
    if len(bit) != 8:
        continue
    else:
        biner.append(bit)

msg = ""
for bit in biner:
    msg += chr(int(bit,2))

if msg == "":
    print("Pesan tersembunyi: Tidak ada pesan tersembunyi dalam file ini!")
else:
    print(f"Pesan tersembunyi: {msg}")

