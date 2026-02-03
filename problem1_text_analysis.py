phrase = input("[+] Entrer un phrase: ")

phrase = phrase.lower()

listeMots = phrase.split()

print(f"[+] Le nombre total de mots: {len(listeMots)}")

len_max = len(listeMots[0])
motLong = ""

for mot in listeMots:
    if len(mot) > len_max:
        motLong = mot
        lenMax = len(mot)

print(f"[+] Le mot le plus long est: {motLong}")

lenVoyelle = 0
for l in phrase:
    if l in "aeoui":
        lenVoyelle += 1

print(f"[+] Nombre de voyelles: {lenVoyelle}")

# Fonction de création de la nouvelle phrase
def createNewSentence(listeMots):
    newMots = []
    for mot in listeMots:
        if len(mot) % 2 == 0:
            newMots.append(mot.upper()) 
        else:
            newMots.append(mot)

    return " ".join(newMots)

newPhrase = createNewSentence(listeMots)
print(f"[+] La nouvelle phrase: {newPhrase}")
