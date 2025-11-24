class Participant:
    def __init__(self, name: str):
        # Inisialisasi atribut private:
        # - name
        # - score = 10
        # - status = "aktif"
        self.__name = name
        self.__score = 10
        self.__status = "aktif"
        

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def get_status(self):
        return self.__status

    def evaluate_status(self):
        """
        - Jika score < 0 → status = "nonaktif"
        - Else → status = "aktif"
        """
        if self.__score < 0:
            self.__status = "nonaktif"
        else:
            self.__status = "aktif"

    def add_fault(self, kind: str):
        """
        - Mapping kesalahan:
            ringan = -2
            sedang = -4
            berat  = -6
            penalti_divisi = -8
        - Jika jenis tidak valid → print("Jenis kesalahan tidak valid.")
        - Kurangi skor sesuai jenis
        - Panggil evaluate_status()
        """
        if kind.lower() == "ringan":
            self.__score -= 2
        elif kind.lower() == "sedang":
            self.__score -= 4
        elif kind.lower() == "berat":
            self.__score -= 6
        elif kind.lower() == "penalti_divisi":
            self.__score -= 8
        else:
            print("Jenis kesalahan tidak valid")
        self.evaluate_status()

    def add_merit(self):
        """
        - Tambah score +2
        - Panggil evaluate_status()
        """
        self.__score += 2
        self.evaluate_status()

    def is_active(self):
        """
        - Return True jika status "aktif"
        """
        return self.__status == "aktif"

    def __str__(self):
        return f"{self.__name} — skor: {self.__score} — status: {self.__status}"


class Division:
    def __init__(self, name: str):
        # - name
        # - participants: list kosong
        # - fault_count = 0
        self.name = name
        self.participants = []
        self.fault_count = 0
        pass

    def get_name(self):
        return self.name

    def get_participants(self):
        return self.participants

    def add_participant(self, name: str):
        """
        - Buat Participant baru
        - Tambahkan ke list participants
        """
        name = Participant(name)
        self.participants.append(name)

    def show(self):
        """
        - Jika kosong → print("Divisi ini tidak memiliki peserta.")
        - Else tampilkan seluruh peserta (pakai enumerate)
        """
        if self.participants == []:
            print("Divisi ini tidak memiliki peserta.")
        else:
            for i in enumerate(self.participants):
                print(f"{i[0]+1}. {i[1].capitalize()} - skor:")

    def find_participant(self, name: str):
        """
        - Cari participant berdasarkan name (case-insensitive)
        - Kembalikan objek Participant atau None
        """
        if name.lower() not in self.participants:
            return None
        
        return Participant(name) #FIXME

    def increment_fault(self):
        """
        - Tambah fault_count sebanyak 1
        """
        self.fault_count += 1

    def check_division_penalty(self):
        """
        - Jika fault_count sudah mencapai 3:
            → beri penalti -8 ke semua peserta
            → reset fault_count ke 0
        """
        if self.fault_count >= 3:
            for person in self.participants:
                person = Participant(person)
                person.add_fault("penalti_divisi")

    def _set_participants(self, new_list):
        """
        - Mengganti isi participants dengan new_list
        """
        self.participants = []


class ManagementSystem:
    def __init__(self):
        self.__divisions: dict[str, Division] = {}

    def add_division(self, name: str):
        """
        - Tambahkan Division baru
        """
        self.__divisions[name] = Division(name)

    def get_division(self, name: str):
        """
        - Jika tidak ada → print("Divisi tidak ditemukan.")
        - Kembalikan objek Division
        """
        if name not in self.__divisions:
            print("Divisi tidak ditemukan")
        else:
            return Division(name) #FIXME

    def register_participant(self, div: str, name: str):
        """
        - Tambahkan participant baru ke sebuah divisi
        """
        self.__divisions[div].add_participant(name) #FIXME

    def apply_fault(self, div: str, name: str, kind: str):
        """
        - Cari divisi
        - Cari participant
        - Jika tidak ditemukan → print("Peserta tidak ditemukan.")
        - Beri fault
        - Update fault_count divisi
        - Cek penalti divisi
        """
        division = Division(div) #FIXME
        participant = Participant(name)
        if participant.get_name() not in Division(div).get_participants:
            print("Peserta tidak ditemukan.")
        
        participant.add_fault("penalti_divisi")
        division.increment_fault()
        division.check_division_penalty()

    def apply_merit(self, div: str, name: str):
        """
        - Mirip apply_fault
        """
        division = Division(div) #FIXME
        participant = Participant(name)
        if participant.get_name() not in Division(div).get_participants:
            print("Peserta tidak ditemukan.")
        
        #FIXME
        participant.add_merit()
        participant.evaluate_status()
        division.check_division_penalty()

    def display_division(self, div: str):
        for div in enumerate(self.__divisions):
            print(f"{div[0]+1}. {div[1]}")

    def remove_inactive(self, div: str):
        """
        - Hapus seluruh peserta dengan status nonaktif
        - Jika tidak ada → print("Tidak ada peserta nonaktif yang dapat dihapus.")
        """
        deleted = 0
        peserta_list = self.__divisions[div]
        for peserta in peserta_list:
            if peserta.get_status() == "nonaktif":
                self.__divisions[div].remove(peserta)
                deleted += 1
        if deleted == 0:
            print("Tidak ada peserta nonaktif yang dapat dihapus")

def main():
    system = ManagementSystem()

    # Init divisions
    system.add_division("Design")
    system.add_division("Marketing")
    system.add_division("IT")

    preset = {
    "Design": ["Upin", "Ipin", "Ehsan"],
    "Marketing": ["Mail", "Jarjit", "Fizi"],
    "IT": ["Mei Mei", "Tok Dalang", "Kak Ros"]
    }

    for div_name, names in preset.items():
        for n in names:
            system.register_participant(div_name, n)

    while True:
        print("\n✦  S T E L L A R O N   E X P R E S S  ✦")
        print("\n=== Stellaron Internship Menu ===")
        print("1. Tambah Peserta")
        print("2. Beri Hukuman (Fault)")
        print("3. Beri Apresiasi (Merit)")
        print("4. Lihat Peserta Divisi")
        print("5. Hapus Peserta Nonaktif")
        print("6. Keluar")
        print("=================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            divisi = input("Nama divisi: ")
            peserta = input("Nama peserta:")
            system.register_participant(divisi, peserta)
            print(f"Peserta dengan nama {peserta} berhasil ditambahkan.")

        elif pilihan == "2":
            divisi = input("Nama divisi: ")
            peserta = input("Nama peserta:")
            kind = input("Jenis hukuman (ringan/sedang/berat): ")

            system.apply_fault(divisi, peserta, kind)
            print(f"Berhasil memberikan hukuman '{kind}' kepada {peserta}")

        elif pilihan == "3":
            divisi = input("Nama divisi: ")
            peserta = input("Nama peserta:")

            system.apply_merit(divisi, peserta)
            print(f"Berhasil memberikan apresiasi kepada {peserta}")

        elif pilihan == "4":
            divisi = input("Nama divisi: ")
            system.display_division(divisi)
            

        elif pilihan == "5":
            divisi = input("Nama divisi: ")
            system.remove_inactive(divisi)

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
