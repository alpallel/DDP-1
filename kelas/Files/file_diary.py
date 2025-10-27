import time

nama = input("Nama penulis: ")
lokasi = input("Lokasi saat ini: ")
date = time.localtime()
isi_diary = input("Isi: ")

diary_file = open("MyDiary.txt", "a")
print(f"Ditulis oleh {nama} di {lokasi} pada {date}\n", file=diary_file)
print(isi_diary, end="\n\n", file=diary_file)
print("="*25, file=diary_file)

diary_file.close()