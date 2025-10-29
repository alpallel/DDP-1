def reverse_dict(input_dict):
    hasil = {}
    for key in input_dict:
        for val in input_dict[key]:
            if val not in hasil:
                hasil.update({val: [key]})
            if key not in hasil[val]:
                hasil[val].append(key)
    return hasil

input_dict = {"a": [1,2,3],
              "b":[2,3],
              "c":[2,3,4,5]}
print(reverse_dict(input_dict))