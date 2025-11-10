# No. 1
class House(object):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    

# No. 2
class Person(object):
    def __init__(self, nama="Tidak Diketahui", usia=-1):
        self.nama = nama
        self.usia = usia

    def __str__(self):
        return f"Hai, ini saya, {self.nama}!"
    
    def get_age(self):
        return self.usia
    

# No. 3
class Snack(object):
    def __init__(self, name, flavor, price, weight, stock=0):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.weight = weight
        self.stock = stock

    def __str__(self):
        return f"Nama: {self.name}\n\
Rasa: {self.flavor}\n\
Harga: {self.price}\n\
Berat: {self.weight}\n\
Jumlah stok: {self.stock}"

    def increment_stock(self, quantity):
        self.stock += quantity
    
    def decrement_stock(self, quantity):
        self.stock -= quantity
