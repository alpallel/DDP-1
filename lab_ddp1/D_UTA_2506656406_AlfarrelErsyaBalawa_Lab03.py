# ================== BAGIAN 1: INPUT DATA ==================

user_input = input("Masukkan data pemasukan perusahaan: \n")
print("=== LAPORAN KEUANGAN PERUSAHAAN ===")

# ================== BAGIAN 2: EKSTRAKSI IDENTITAS ==================
posisi_awal = user_input.find("(") + 1
posisi_akhir = user_input.find(")")
kode_perusahaan = user_input[posisi_awal:posisi_akhir]
print("Identitas:", kode_perusahaan)

# ================== BAGIAN 3: PROSES DATA PEMASUKAN ==================
# Loop untuk memproses setiap tahun
while True:
    # TODO: Temukan posisi kata "PEMASUKAN" pertama
    posisi_pemasukan = user_input.find("PEMASUKAN")

    # TODO: Cari posisi PEMASUKAN berikutnya untuk menentukan batas

    # Important Note: Saat input dari terminal, input \n akan dianggap 
    # sebagai literal \n (backslash + n), bukan newline
    # Gunakan r"\n" untuk mencari karakter \ dan n secara literal
    posisi_pemasukan_berikut = user_input.find("PEMASUKAN", posisi_pemasukan + len("PEMASUKAN"))
    
    # TODO: Ekstrak string pemasukan berdasarkan posisi yang ditemukan
    if posisi_pemasukan_berikut != -1:
        # Slice dari pos_pemasukan + len("PEMASUKAN") sampai pos_pemasukan_berikut
        data_pemasukan = user_input[posisi_pemasukan + len("PEMASUKAN"):posisi_pemasukan_berikut]
        
    else:
        # Slice dari pos_pemasukan + len("PEMASUKAN") sampai akhir
        data_pemasukan = user_input[posisi_pemasukan + len("PEMASUKAN"):]
    
    # TODO: Ekstrak tahun (4 karakter pertama setelah strip)
    tahun = user_input[posisi_pemasukan + len("PEMASUKAN "):posisi_pemasukan + len("PEMASUKAN ") + 4]
    print("Tahun:", tahun)
    
    # TODO: Slice mulai dari posisi setelah ":"
    data_pemasukan = data_pemasukan[data_pemasukan.find(":")+2:]

    # ================== BAGIAN 4: INISIALISASI STATISTIK ==================
    pendapatan_min = float('inf')
    pendapatan_max = float('-inf')
    bulan_min = ""
    bulan_max = ""
    total_pendapatan = 0
    jumlah_bulan = 0

    # ================== BAGIAN 5: BUAT HEADER TABEL ==================
    tabel_output = "| Bulan      |     Jumlah |\n"
    tabel_output += "|------------|------------|\n"

    # ================== BAGIAN 6: PROSES DATA BULANAN ==================
    # TODO: Split string pemasukan berdasarkan ";"
    for entri in data_pemasukan.split(";"):
        # Hilangkan spasi di awal dan split berdasarkan spasi
        entri = entri.strip()
        entri = entri.split(" ")
        
        bulan = entri[0]
        jumlah = int(entri[1])
        
        # Format dan tambahkan ke tabel
        tabel_output += "| {0:<10} | {1:10,} |\n".format(bulan, jumlah)
        
        # ================== BAGIAN 7: HITUNG STATISTIK ==================
        # TODO: Update nilai minimum
        if jumlah < pendapatan_min:
            pendapatan_min = jumlah
            bulan_min = bulan
        # TODO: Update nilai maksimum
        if jumlah > pendapatan_max:
            pendapatan_max = jumlah
            bulan_max = bulan
        # TODO: Update total dan counter
        total_pendapatan += jumlah
        jumlah_bulan += 1

    # ================== BAGIAN 8: TAMPILKAN HASIL ==================
    print(tabel_output)
    
    # TODO: Hitung rata-rata dengan pengecekan pembagian nol
    if jumlah_bulan == 0:
        rata_rata = 0
    else:
        rata_rata = total_pendapatan / jumlah_bulan
    
    print("\n=== STATISTIK DASAR ===")
    print(f"Bulan Terendah    : {bulan_min} ({pendapatan_min:,})")
    print(f"Bulan Tertinggi   : {bulan_max} ({pendapatan_max:,})")
    print(f"Total Pendapatan  : {total_pendapatan:,}")
    print(f"Rata-rata Bulanan : {rata_rata:,.2f}")
    print("=" * 25)

    # ================== BAGIAN 9: KONTROL LOOP ==================
    if posisi_pemasukan_berikut == -1:
        break
    else:
        user_input = user_input[posisi_pemasukan_berikut-1:]

