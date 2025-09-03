while True:
    row = input("Enter a Row: ")
    col = input("Enter a Column: ")
    search = input("Enter number to search: ")

    if int(col) <= 0 or int(row) <= 0:
        print("Invalid Input")
        break

    for x in range (1, (int(row) + 1)):
        for y in range (1, (int(col) +1)):
            prod = x * y
            if prod == int(search):
                print(f"[{prod}]", end=" ")
            else:
                print(f"{prod}", end=" ")
        print()
