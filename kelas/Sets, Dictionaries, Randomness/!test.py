file = open("C:\\Users\\alpal\\OneDrive\\Documents\\ngoding\\ddp1\\kelas\\items.txt", "r")

items_set = set()

for line in file:
    for item in line.split():
        items_set.add(item)
file.seek(0)

for key in items_set:
    print_lst = []

    for line in file:
        if key not in line:
            break

        for item in line.split(" "):
            if item != key:
                print_lst += item

    print(f"{key}: {print_lst}")

# print(items_set)