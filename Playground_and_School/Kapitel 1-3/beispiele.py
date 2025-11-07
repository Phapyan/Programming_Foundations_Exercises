#Einlesen
number = int(input("Geben Sie eine Zahl ein: "))

#Option 1: Verwendung von if
if number > 0:
    print("Die Zahl ist positiv.")
if number < 0:
    print("Die Zahl ist negativ.")
if number == 0:
    print("Die Zahl ist null.")

#Option 2: Verwendung von if-elif-else
if number > 0:
    print("Die Zahl ist positiv.")
else:
    if number < 0:
        print("Die Zahl ist negativ.")
    else:
        print("Die Zahl ist null.")
#Option 3: Verwendung von if-elif-else
if number > 0:
    print("Die Zahl ist positiv.")
elif number < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")

#Option 4: Conditional Expression (Ternary Operator)
result = "Zahl ist grösser Null" if number > 0 else "Zahl in kleiner Null" if number < 0 else "Zahlt ist gleich Null"
print(result)

#Option 5: Conditional Expression + Walrus Operator
print(result := "Zahl ist grösser Null" if number > 0 else "Zahl in kleiner Null" if number < 0 else "Zahlt ist gleich Null")

#Option 6: March Case statement (Underscore wird verwendet, wenn nicht auf einen bestimmten Wert geprüft wird)
match(number): 
    case _ if number > 0:
        print("Die Zahl ist grösser als Null")
    case _ if number < 0:
        print("Die Zahl ist kleiner als Null")
    case _:
        print("Die Zahl ist gleich Null")


