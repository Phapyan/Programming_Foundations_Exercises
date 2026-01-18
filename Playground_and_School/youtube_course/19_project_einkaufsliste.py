einkaufsliste = []

x = input("Was möchtest du einkaufen? (Tippe n sobald fertig.)")

einkaufsliste.append(x)

while x != "n":
    x = input("Was noch?")
    einkaufsliste.append(x)

if einkaufsliste[-1] == "n":
    del einkaufsliste[-1]


print(einkaufsliste)
