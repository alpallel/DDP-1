import random
import string

# Struktur Data
users = {}
role_admin = set()
role_pegawai = set()
role_pelanggan = set()

# Mapping nomor role ke nama dan set-nya
roles = {
    1: ("Admin", role_admin),
    2: ("Pegawai", role_pegawai),
    3: ("Pelanggan", role_pelanggan),
}


def generate_random_password():
    password = ""
    for i in range(4):
        password += str(random.choice(string.ascii_lowercase))
    return password
    


print("========================================")
print("SELAMAT DATANG DI SISTEM LOGIN STELLARON")
print("========================================")

while True:
    print("\nMenu:")
    print("1. Daftar akun baru")
    print("2. Tambah role ke username")
    print("3. Hapus role dari username")
    print("4. Cetak username dari role")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan (1-5): ").strip()

    if pilihan == "1":
        username = input("masukkan username: ")
        if username in users.keys():
            print("username sudah ada")
        else:
            password = generate_random_password()
            users.update({username: password})
            print(f"Password acak untuk user {username} adalah: {password}\nAkun berhasil ditambahkan")


    elif pilihan == "2":
        print("\nDaftar Role:")
        print("1. Admin")
        print("2. Pegawai")
        print("3. Pelanggan")
        username = input("masukkan username yang ingin ditambah role: ").strip()
        if username not in users.keys():
            print(f"user {username} belum terdaftar")
            continue

        inp = input("\nPilih role (1-3): ")
        if inp == "1":
            role_admin.add(username)
            print("role admin sukses ditambahkan ke user")
        elif inp == "2":
            role_pegawai.add(username)
            print("role pegawai sukses ditambahkan ke user")
        elif inp == "3":
            role_pelanggan.add(username)
            print("role pelanggan sukses ditambahkan ke user")
        else:
            print("mohon masukkan pilihan yang sesuai")
        

    elif pilihan == "3":
        print("\nDaftar Role:")
        print("1. Admin")
        print("2. Pegawai")
        print("3. Pelanggan")
        username = input("Masukkan username: ").strip()
        if username not in users.keys():
            print(f"user {username} belum terdaftar")
            continue

        inp = input("Pilih role (1-3): ").strip()
        if inp == "1":
            if username not in role_admin:
                print("user tidak memiliki role admin")
            else:
                role_admin.remove(username)
                print(f"User {username} berhasil dihapus dari role admin")
        elif inp == "2":
            if username not in role_pegawai:
                print("user tidak memiliki role pegawai")
            else:
                role_pegawai.remove(username)
                print(f"User {username} berhasil dihapus dari role pegawai")
        elif inp == "3":
            if username not in role_pelanggan:
                print("user tidak memiliki role pelanggan")
            else:
                role_pelanggan.remove(username)
                print(f"User {username} berhasil dihapus dari role pelanggan")
        else:
            print("mohon masukkan input yang sesuai")
            continue

    elif pilihan == "4":
        print("\nDaftar Role:")
        print("1. Admin")
        print("2. Pegawai")
        print("3. Pelanggan")
        role_input = input(
            "Cetak username dengan role (masukkan nomor role dipisahkan dengan koma mis. 1, 2):\nRole: "
        ).strip()
        role_input = role_input.split(", ")
        role_input = set(role_input)
        result = set(users.keys())

        if "1" in role_input:
            if len(role_admin) == 0:
                print("Tidak ditemukan pengguna")
                continue
            result = role_admin & result
        if "2" in role_input:
            if len(role_pegawai) == 0:
                print("Tidak ditemukan pengguna")
                continue
            result = role_pegawai & result
        if "3" in role_input:
            if len(role_pelanggan) == 0:
                print("Tidak ditemukan pengguna")
                
            result = role_pelanggan & result

        result = list(result)
        print("Username: ")
        for i in range(len(result)):
            print(f"{i+1}. {str(result[i])}")
        

    elif pilihan == "5":
        print("\nProgram selesai. Terima kasih telah menggunakan sistem ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")

