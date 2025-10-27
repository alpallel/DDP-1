def get_positions(lst):
    return {num : [i for i, x in enumerate(lst) if x == num] for num in lst}

print(get_positions([1,2,3,5,1,5,2,1,2,4,5,2,3,5,3,1]))
# >>> {1: [0, 4, 7, 15], 2: [1, 6, 8, 11], 3: [2, 12, 14], 5: [3, 5, 10, 13], 4: [9]}

