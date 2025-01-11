num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows, 0, -1):
    for j in range(num_rows-i):
        print(end=" ")
    for j in range(0, i):
        print("*", end=" ")
    print()
