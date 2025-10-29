input_dict = {"a": [1,2,3],
              "b":[2,3],
              "c":[2,3,4,5]}

hasil = {}
for key in input_dict:
    for val in input_dict[key]:
        hasil.update({val: [key]})
        if key in hasil[val]:
            continue
        else:
            hasil[val].append(key)

print(hasil)