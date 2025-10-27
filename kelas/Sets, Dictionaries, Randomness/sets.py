file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

words_file1 = set()
for line in file1:
    words_file1 = words_file1 | set(line.split())

words_file2 = set()
for line in file2:
    words_file2 = words_file2 | set(line.split())

combined = len(words_file2 | words_file1)
similar = len(words_file1 & words_file2)

# print(combined)
# print(similar)

similarity_score = abs(similar) / abs(combined)

print(f"j_score = {similarity_score}")

file1.close()
file2.close()
