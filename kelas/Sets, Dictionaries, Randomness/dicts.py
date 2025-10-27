def get_numbers(num_list):
    num_set = set(num_list)
    return {num : num_list.count(num) for num in num_set}

print(get_numbers([1,1,1,2,4,2,4,1,24,1,5]))
# >>> {1: 5, 2: 2, 4: 2, 5: 1, 24: 1}