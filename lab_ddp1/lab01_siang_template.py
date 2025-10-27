"""
Lab 01 - Spiral Poligon Bergradasi

Program ini menggambar spiral yang tersusun dari n-sisi (poligon)
dengan panjang garis yang bertambah setiap langkah, serta gradasi warna
dari warna awal (r1,g1,b1) ke warna akhir (r2,g2,b2).
"""

import turtle

# --- Konfigurasi awal turtle ----
turtle.shape('turtle')
turtle.title('Lab 01')
turtle.speed("fastest")
turtle.setup(width=750, height=750)
turtle.colormode(255)
turtle.pendown()

# === Menerima input dari user ---

n = int(turtle.textinput("Lab 01",
    "The number of polygon sides for the spiral: "))

# TODO: membuat text input untuk r1,g1,b1 dan r2,g2,b2.

# TIPS: Untuk memudahkan testing, anda bisa memberikan nilai default secara manual (hardcode)
#       misalnya r1=1, g1=0, b1=0 untuk merah; r2=0, g2=0, b2=1 untuk biru,
#       sehingga tidak perlu memasukkan input setiap kali program dijalankan.
#       Jika sudah yakin, kembalikan ke turtle.textinput() agar nilai bisa diisi secara dinamis.

r1 = int(turtle.textinput("Lab 01",
    "The red value for the first color (beetween 0-255): "))  # Teks: "The red value for the first color (between 0-255): "
g1 = int(turtle.textinput("Lab 01",
    "The green value for the first color (beetween 0-255): ")) 
b1 = int(turtle.textinput("Lab 01",
    "The blue value for the first color (beetween 0-255): ")) 

r2 = int(turtle.textinput("Lab 01",
    "The red value for the first color (beetween 0-255): "))   # Teks: "The red value for the first color (between 0-255): "
g2 = int(turtle.textinput("Lab 01",
    "The green value for the first color (beetween 0-255): ")) 
b2 = int(turtle.textinput("Lab 01",
    "The blue value for the first color (beetween 0-255): ")) 


# --- Parameter Spiral ---

# TODO: Mengisi nilai dari variable berdasarkan ketentuan soal
layer       = 50    # jumlah putaran pada spiral
line_length = 1     # panjang garis saat ini, akan bertambah setiap langkah

# --- Nilai warna RGB saat ini ---
# note: Nilai dari r, g, dan b akan berubah dari warna pertama (r1,g1,b1) hingga akhirnya menjadi warna akhir (r2,g2,b2)

# TODO: mengisi nilai r, g, b dengan variabel yang tepat
r = r1
g = g1
b = b1

# --- Besaran perubahan warna per layer ---

# TODO: Hitung nilai increment (pertambahan warna per layer)
r_inc = round((r2 - r1) / (layer ))
g_inc = round((g2 - g1) / (layer ))
b_inc = round((b2 - b1) / (layer ))

# TODO: Menggambar spiral
for i in range(layer):
    # Mengatur warna garis   
    turtle.pencolor((r, g, b))   

    for j in range(n):

        # Menggambar polygon
        turtle.forward(line_length)
        turtle.left(360/n)
        line_length += 1
        
    # Menambahkan nilai increment pada nilai warna saat ini
    r += r_inc 
    g += g_inc 
    b += b_inc 


turtle.exitonclick() # Klik layar jendela untuk keluar