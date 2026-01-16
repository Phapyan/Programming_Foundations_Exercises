def main():
    number_string = input("Bitte Ziffern eingeben: ")
    total = string_total(number_string)
    print("Die Ziffersumme ist: ", total)

def string_total():
    total = 0
    number = 0
    #Iteration
    for i in range(len(string)):
        number = int(string[i])
        total += number
    return total
main()