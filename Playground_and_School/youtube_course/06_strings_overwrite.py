x = "hallo"

# Strings sind unveränderlich. Hier eine Methode trotzdem zu überschreiben.
x = "H" + x[1:]
print(x)


# Übung wie gebe ich es 10 mal aus
print(x * 10)

# Schleife, wenn ich das Hallo untereinander haben möchte. Die Variable _ ist einfach ein Platzhalter.
for _ in range(10):
    print(x)