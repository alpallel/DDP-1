def read_matrix(rows, cols):
    hasil = []
    print("Masukkan elemen matriks: ")
    for i in range(rows):
        inp = input()
        inp.strip()
        if len(inp) != cols * 2 - 1:
            print("Jumlah elemen tidak sesuai dengan jumlah kolom")
            exit()
        temp = []
        for num in inp:
            try:
                temp.append(int(num))
            except:
                continue
            
        hasil.append(temp)
    return hasil


def print_matrix(matrix):
    for baris in matrix:
        for col in baris:
            print(col, end=" ")
        print()
    pass


def transpose_matrix(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def add_row(matrix):
    global rows
    pos = int(input("Masukkan posisi baris baru: "))
    
    if pos > rows:
        print("Nomor baris di luar jangkauan!")
    else:
        element = input("Masukkan elemen-elemen baris baru: ")
        temp = []
        for num in element:
            try:
                temp.append(int(num))
            except:
                continue
        matrix.insert(pos, temp)
        rows += 1
        print("Baris berhasil ditambahkan")


def add_col(matrix):
    global cols
    pos = int(input("Masukkan posisi kolom baru: "))
    if pos > cols:
        print("Nomor baris di luar jangkauan!")
    else:
        element = input("Masukkan elemen-elemen kolom baru: ")
        temp = []
        for num in element:
            try:
                temp.append(int(num))
            except:
                continue
        
        for i in range(len(matrix)):
            matrix[i].insert(pos, temp[i])
        cols += 1
        print("Kolom berhasil ditambahkan")


# Main Program
def main():
    global rows
    global cols
    rows = int(input("Masukkan jumlah baris: "))
    cols = int(input("Masukkan jumlah kolom: "))
    A = read_matrix(rows, cols)

    while True:
        print("\n=== Menu Matriks Dekdepe ===")
        print("1. Tampilkan Matriks")
        print("2. Hitung Transpose Matriks")
        print("3. Tambah Baris Baru")
        print("4. Tambah Kolom Baru")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        
        print()

        if pilihan == "1":
            print("Matriks Sekarang:")
            print_matrix(A)      
        elif pilihan == "2":
            print("Matriks Transpose:")
            T = transpose_matrix(A)
            print_matrix(T)
        elif pilihan == "3":
            add_row(A)
        elif pilihan == "4":
            add_col(A)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
