global nama_makanan
global harga
global jumlah_pesanan

nama_makanan = []
harga = []
jumlah_pesanan = []

def add_to_order(food, price, quantity):

    if int(price) <= 0 or int(quantity) <= 0:
        print("Harga dan jumlah harus lebih dari 0")
        
    elif food not in nama_makanan:
        
        nama_makanan.append(food)
        harga.append(int(price) * int(quantity))
        jumlah_pesanan.append(quantity)
        print(f"{food} berhasil ditambahkan ke pesanan.")
    else:
        harga[nama_makanan.index(food)] += price * quantity
        jumlah_pesanan[nama_makanan.index(food)] += quantity
        print(f"{food} sudah ada dalam pesanan, jumlah diperbarui menjadi {jumlah_pesanan[nama_makanan.index(food)]}")
    

def remove_from_order(item):
    if nama_makanan == []:
        print("Pesanan masih kosong")

    elif item in nama_makanan:
        harga.remove(harga[nama_makanan.index(item)])
        jumlah_pesanan.remove(jumlah_pesanan[nama_makanan.index(item)])
        nama_makanan.remove(item)
        print(f"{item} berhasil dihapus dari pesanan")
    else:
        print("Menu tidak ditemukan di daftar pesanan")

def view_order():
    if nama_makanan == []:
        print("Belum ada pesanan")
    else:
        print("=== Daftar Pesanan Anda===")
        count = 1
        for makanan in nama_makanan:
            print(f"{count}. {makanan} - {jumlah_pesanan[nama_makanan.index(makanan)]} x Rp {harga[nama_makanan.index(makanan)]}")
            count += 1
        print(f"Total item: {sum(jumlah_pesanan)}")

def hitung_total_harga():
    total = sum(harga)
    return total

def cek_kode_promo(kode):
    if "HEMAT" in kode:
        diskon = str(kode).split("HEMAT")
        diskon = diskon[1]
        if int(diskon) > 50:
            print("Kode promo tidak valid. Kode promo tidak akan diterapkan.")
            return -1
        else:
            return int(diskon) / 100

    else:
        print("Kode promo tidak valid. Kode promo tidak akan diterapkan.")
        return -1

def checkout(kode):
    if nama_makanan == []:
        print("Pesanan masih kosong")
        return None
        

    total_harga = hitung_total_harga()

    persen = cek_kode_promo(kode)

    potongan = None
    if persen != -1:
        potongan = total_harga * persen
    else:
        potongan = 0
        kode = None

    total_setelah_promo = total_harga - potongan

    pajak = total_setelah_promo * (11/100)

    total_akhir = total_setelah_promo + pajak

    print("\n===================================")
    print("MakanYuk! - Ringkasan Pembayaran")
    print("===================================")
    count = 1
    for makanan in nama_makanan:
        print(f"{count}. {makanan} - {jumlah_pesanan[nama_makanan.index(makanan)]} x Rp {harga[nama_makanan.index(makanan)]}")
        count += 1
    print("-----------------------------------")
    print(f"Total Awal     : Rp {int(total_harga)}")
    if kode != None:
        print(f"Promo ({kode:^8}) : -Rp {potongan}")
    else:
        print(f"Promo          : -Rp {potongan}")
    print(f"Pajak (11%)    : Rp {int(pajak)}")
    print("-----------------------------------")
    print(f"TOTAL AKHIR    : Rp {round(total_akhir, 2)}")
    print("===================================\n")

    print("Checkout selesai. Terima kasih telah memesan di MakanYuk!")

def main():
    while True:
        print("=== Menu MakanYuk! ===")
        print("1. Tambah Pesanan")
        print("2. Hapus Pesanan")
        print("3. Lihat Pesanan")
        print("4. Checkout")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            data = input("Masukkan pesanan: ")
            try:
                data = data.split(" ")
                food = data[0]
                price = int(data[1])
                quantity= int(data[2])
                add_to_order(food, price, quantity)
            except IndexError:
                print("Mohon masukkan data sesuai format. Data tidak dimasukkan")

        elif pilihan == "2":
            item = input("Masukkan nama makanan yang ingin dihapus: ")
            remove_from_order(item)

        elif pilihan == "3":
            view_order()

        elif pilihan == "4":
            kode_promo = input("Masukkan kode promo: ")
            cek_kode_promo(kode_promo)
            checkout(kode_promo)
            break
        else:
            print("Pilihan tidak valid.\n")
        print()

if __name__ == "__main__":
    main()
