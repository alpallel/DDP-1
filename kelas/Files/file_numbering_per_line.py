input_file = open("puisi.txt", "r")
output_file = open("output.txt", "w")

count = 1
for line in input_file:
    print(f"/*{count}*/ {line}", end="", file=output_file)
    count += 1

input_file.close()
output_file.close()