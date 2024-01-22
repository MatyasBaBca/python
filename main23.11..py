class Student:
    def __init__(self, jmeno, prijmeni, predmet=None, hodnoceni=[]):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.predmet = predmet
        self.hodnoceni = hodnoceni

    def zobraz_informace(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Příjmení: {self.prijmeni}")
        print(f"Předmět: {self.predmet}")
        print(f"Hodnocení: {', '.join(map(str, self.hodnoceni))}")

    def pridej_predmet(self, predmet):
        self.predmet = predmet


class Teacher:
    def __init__(self, jmeno, predmet):
        self.jmeno = jmeno
        self.predmet = predmet

    def pridej_hodnoceni(self, student, hodnoceni):
        if student.predmet == self.predmet:
            student.hodnoceni.append(hodnoceni)
            print(f"Hodnocení přidáno studentovi {student.jmeno} {student.prijmeni} z předmětu {self.predmet}.")
        else:
            print(f"Chyba: Student {student.jmeno} {student.prijmeni} není zapsán do předmětu {self.predmet}.")

student1 = Student("Jan", "Novák")
student1.pridej_predmet("Matematika")

ucitel = Teacher("Mgr. Novotná", "Matematika")

ucitel.pridej_hodnoceni(student1, 85)
student1.zobraz_informace()
