def main():
    #Einleses der Namen
    full_name = input("Bitte den Namen eingeben: ")

    #Split
    name = full_name.split()
    #Iteration
    for string in name:
        print(string[0].upper(), end="")
        print(".", end=" ")


main()