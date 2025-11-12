class apa:
    a = 0
    pass

a1 = apa()
a2 = apa()
a3 = apa()
a1.a = 10
apa.a = 100
a1.a = a1.a + a2.a

print(a1.a)
print(a2.a)
print(a3.a)