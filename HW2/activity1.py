mydict={}
mydictSize = int(input("Matrix size: "))

for x in range (mydictSize):
    val = str(input(f"Shopping Item {x+1}: "))
    mydict[x] = val

while(True):
    print("What would you like to do: [C]hange item [R]emove [D]isplay [S]earch")
    userInput = str(input("-"))
    
    if userInput == '*':
        break

    if userInput.lower() == "d":
        print("Displaying Values")
        print("Key   Value")
        for x, y in mydict.items():
            print(f"{x}     {y}", end=" ")
            print()
    elif userInput.lower() == "s":
        search = int(input("Enter key to search: "))
        if search in mydict:
            print(f"Found {mydict[search]} item")
        else:
            print("I'm sorry, not in the cart")
    elif userInput.lower() == "r":
        search = int(input("Enter key to remove: "))
        if search in mydict:
            removed_value = mydict.pop(search)
            print(f"The key {search} with value {removed_value} has been deleted")
        else:
            print("Key not found")
    elif userInput.lower() == "c":
        search = int(input("Enter key to change: "))
        if search in mydict:
            print(f"Found {mydict[search]} item")
            change = str(input("Enter new value: "))
            mydict[search] = change 
        else:
            print("I'm sorry, not in the cart")