input_file = open("puisi.txt", "r")

jumlah_kata = 0
count = 0
for line in input_file:
    kata = line.split()
    jumlah_kata += len(kata)
    count += 1

rata_rata = jumlah_kata / count
print(f"rata-rata kata per baris adalah {rata_rata:.3f}")

input_file.close()