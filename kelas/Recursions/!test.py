def binary_search(arr, target, low, high):
        if low > high:
            return -1
        mid = (high-low) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr,target, mid, high-1)

arr = [2, 4, 6, 8, 10, 12, 14, 16]
print("Data:", arr)
target = int(input("Masukkan angka yang ingin dicari: "))
hasil = binary_search(arr, target, 0, len(arr) - 1)
if hasil != -1:
    print(f"Angka {target} ditemukan pada index ke-{hasil}.")
else:
    print(f"Angka {target} tidak ditemukan dalam list.")