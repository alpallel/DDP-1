print("==== Burhan Agritech ====\n")

n_kanal = int(input("Berapa banyak kanal yang ingin dihitung? "))
print()

for i in range(n_kanal):
    print(f"--- Input kanal ke-{i+1} ---")
    l_atas = float(input("Masukkan Lebar Atas Kanal (m): "))
    l_bawah = float(input("Masukkan Lebar Bawah Kanal (m): "))
    kedalaman = float(input("Masukkan Kedalaman Air (m): "))
    kunci_enkripsi = int(input("Masukkan Kunci Enkripsi: "))
    
    tipe_enkirpsi = input("Masukkan Kunci Enkripsi (binary/octal): ")
    tipe = ["binary", "octal"]
    if tipe_enkirpsi not in tipe:
        print("Mohon masukkan tipe enkirpsi yang sesuai")
        continue

    luas_penampang = (l_atas + l_bawah) * kedalaman / 2
    print(f"\n--- Hasil Perhitungan ---\nLuas penampang kanal tersebut adalah {luas_penampang:.2f} m2\n")

    if tipe_enkirpsi == "binary":
        kode = (bin(round(kunci_enkripsi + luas_penampang)))

    else: 
        kode = (oct(round(kunci_enkripsi + luas_penampang)))

    print(f"=== Kode Kontrol Aliran ke-{i+1} : DDP-{kode} ===\n")
print("=== Program Selesai ===")