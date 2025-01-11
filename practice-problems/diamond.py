num_rows = int(input("Enter the number of rows: "))
for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in range(0, i+1):
        print("*", end=" ")
    print()
for i in range(num_rows-1, 0, -1):
    for j in range(num_rows-i):
        print(end=" ")
    for j in range(0, i):
        print("✨", end=" ")
    print()
