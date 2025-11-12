class Barang():
    def __init__(self, nama:str, kode:str, harga:int):
        if harga <0:
            raise ValueError
        self.__nama = nama
        self.__kode = kode
        self.__harga = harga 

    def __str__(self):
        return f"Nama: {self.__nama}, Kode: {self.__kode}, Harga: {self.__harga}"

    def __repr__(self):
        return f"Nama_Barang= {self.__nama}, Kode_barang= {self.__kode}, Harga_Barang= {self.__harga}"
    
    def set_nama(self, new_name:str):
        self.__nama = new_name

    def set_harga(self, new_price:int):
        self.__harga = new_price

    def get_nama(self):
        return self.__nama
    
    def get_kode(self):
        return self.__kode
    
    def get_harga(self):
        return self.__harga
    
    def __mul__(self, value:int):
        return self.__harga * value
    
    def __add__(self, other):
        return f"Paket {self.get_nama()} dan {other.get_nama()}, Kode: {self.get_kode() + other.get_kode()}, Harga: {self.get_harga() + other.get_harga()}"

    
barang = Barang("Sabun Cap Bambang", "BZB", 1000)
print(barang * 5)

barang1 = Barang("Sabun Cap Bambang", "BZB", 1000)
barang2 = Barang("Sabun Cap Usep", "BZU", 5000)
print(barang1 + barang2)