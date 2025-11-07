#Modul-Bewertung in Python programmiert
grade_pp = float(input("Bitte Note für PP eingeben: "))
grade_exam = float(input("Bitte Note für Exam eingeben:"))
#Drucken
print("Note PP: ", grade_pp)
print("Note Exam: ", grade_exam)

#Auswertung
#Happy path
if grade_pp >= 4.0 and grade_exam >= 4.0:
    print("Bestanden")
    grade_final = grade_pp * 0.4 + grade_exam * 0.6
    print(f"Die Gesamtnote ist: {grade_final:.2f}")
elif grade_pp < 4.0 and grade_exam >= 4.0:
    print("Leider negativ, weil PP negativ ist.")
elif grade_pp >= 4.0 and grade_exam < 4.0:
    print("Leider negativ, weil Exam negativ ist.")
