row = input("Enter a Row: ")
col = input("Enter a Column: ")

for x in range (1, (int(row) + 1)):
    for y in range (1, (int(col) +1)):
        print(f"{x*y:5}", end=" ")
    print()