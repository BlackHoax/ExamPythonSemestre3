# Liste des étudiants et leurs notes
students = [
    ("Ali", 12),
    ("Fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibrahima", 7)
]

# Affichage des étudiants et leurs notes
def afficherNotesEtudiants(students: list[tuple]):
    print("-"*30)
    for entry in students:
        print(f"[+] Nom: {entry[0]}")
        print(f"[+] Note: {entry[1]}/20")
        print("-"*30)

afficherNotesEtudiants(students)

# Calcul de la moyenne
def calculeMoyenneClasse(students: list[tuple]):
    somme = 0
    for entry in students:
        somme += entry[1]

    # on retroune la moyenne
    return somme / len(students)

moyenneClasse = calculeMoyenneClasse(students)
print(f"[+] La moyenne de la classe: {moyenneClasse}/20")

# Calcul de la note minimale
def calculeNoteMinimale(students):
    # on considère la première note comme minimale
    noteMin = students[0][1] 

    for entry in students:
        if entry[1] < noteMin:
            noteMin = entry[1]

    return noteMin

noteMin = calculeNoteMinimale(students)
print(f"[+] La note minimale: {noteMin}/20")

# Calcul de la note maximale
def calculeNoteMaximale(students):
    # on considère la première note comme maximale
    maxNote = students[0][1] 

    for entry in students:
        if entry[1] > maxNote:
            maxNote = entry[1]

    return maxNote

maxNote = calculeNoteMaximale(students)
print(f"[+] La note minimale: {maxNote}/20")

# Liste des étudiants admins
etudiantsAdmis = [etudiant for etudiant in students if etudiant[1] >= 10]

print("[-] Liste des étudiant Admis [-]")
for etudiant in etudiantsAdmis:
    print(f"[+] Nom: {etudiant[0]} | note: {etudiant[1]}/20")

# Liste des étudiants ajournés
etudiantsAjourne = [etudiant for etudiant in students if etudiant[1] < 10]

print("[-] Liste des étudiant Ajournés [-]")
for etudiant in etudiantsAjourne:
    print(f"[+] Nom: {etudiant[0]} | note: {etudiant[1]}/20")