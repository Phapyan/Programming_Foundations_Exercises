kids = 5
adults = 10
seniors = 7.50

age = int(input("Wie alt bist du?"))

if age < 10:
    print("Dein Ticket kostet:", kids)
elif age < 60:
    print("Dein Ticket kostet:", adults)
else:
    print("Dein Ticket kostet:", seniors)