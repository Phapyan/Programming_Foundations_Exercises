einkaufszettel = ["bananen", "äpfel", "brot"]

# 1. Hängt Nüsse hinten an die Liste
einkaufszettel.append("Nüsse")

# 2. Fügt Butter der Liste zu, Zahl wichtig an welcher Stelle
einkaufszettel.insert(0,"Butter")

# 3. Entfern die Nüsse von der Liste
einkaufszettel.remove("Nüsse")

# 4. Schmeisst das letzte Element der Liste raus
einkaufszettel.pop()

# 5. Löschen einer bestimmten Position in der Liste
del einkaufszettel[0]

print(einkaufszettel)