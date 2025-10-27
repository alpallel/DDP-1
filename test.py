a = int(input("a = "))

hasil = ""
b = 1
power = 0

while b < a:
    b *= 2
    power += 1
    print(power)

for i in range(power, -1, -1):
    if a - 2**i >= 0:
        a -= 2**i
        hasil = hasil + "1"
    else:
        hasil = hasil + "0"

print(hasil)