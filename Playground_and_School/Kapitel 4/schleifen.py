#While-Schleife

i = 0

while i <= 10:
    if i % 2 == 0: #„Nimm den Rest, wenn i durch 2 geteilt wird.“
        print(i)
    i = i + 1

#For-Schleife
for _ in range(1, 11):
    if _ % 2 == 0:   
        print(_)

#For-Schleife-mit-Inkrement
for _ in range(1, 11, 2): #(Startwert, Endwert, Inkrement oder Dekrement)
        print(_)


#break and continue
num = 0

while num < 10:
    num += 1

    if num == 5:
        print("Skip!!")
        continue
     
    if num == 8:
        print ("Breaking at 8!")
        break

    print("Derzeitige Zahl: ", num)

print("Schleife beendet ...")
