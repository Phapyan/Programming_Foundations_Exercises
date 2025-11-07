from itertools import count
# Itertools ist eine Library die ermöglicht zu zählen ohne Obergrenze

# Nicht richtig!
#for i in (10**100):
   # print(i)

for i in count():
    print("Wert", i)