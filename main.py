import random

# Creazione classe

class Domanda:
    def __init__(self, domanda: str, livello: int, risposta: str, alt1: str, alt2: str, alt3: str):
        self.domanda = domanda
        self.livello = livello
        self.risposta = risposta
        self.alt1 = alt1
        self.alt2 = alt2
        self.alt3 = alt3

class Punteggio:
    def __init__(self, nickname: str, punti: int):
        self.nickname = nickname
        self.punti = punti

# Memorizzazione domande

lista_domande = []
liv_max = 0

with open('domande.txt', 'r') as file:
    i = 0

    for line in file:
        if i == 0:
            domanda = line.strip()
            i += 1

        elif i == 1:
            livello = int(line.strip())
            i += 1

        elif i == 2:
            risposta = line.strip()
            i += 1

        elif i == 3:
            alt1 = line.strip()
            i += 1

        elif i == 4:
            alt2 = line.strip()
            i += 1

        elif i == 5:
            alt3 = line.strip()
            i += 1

        else:
            i = 0
            d = Domanda(domanda, livello, risposta, alt1, alt2, alt3)
            lista_domande.append(d)
            if livello > liv_max:
                liv_max = livello

# Elaborazione gioco

j = 0
lista_livello = []
continuo = True

while continuo == True:

    if j > liv_max:
        break

    for d in lista_domande:
        if d.livello == j:
            lista_livello.append(d)
    scelta = random.choice(lista_livello)

    print(f"Livello {j}) {scelta.domanda}")

    opzioni = [scelta.risposta, scelta.alt1, scelta.alt2, scelta.alt3]
    random.shuffle(opzioni)
    print(f"\t\t1. {opzioni[0]}\n\t\t2. {opzioni[1]}\n\t\t3. {opzioni[2]}\n\t\t4. {opzioni[3]}")

    risp = input("Inserisci risposta: ")

    while not risp.isdigit() or int(risp) < 1 or int(risp) > 4:
        print("No, devi inserire un numero da 1 a 4")
        risp = input("Inserisci risposta: ")

    risp = int(risp)

    if opzioni[risp - 1] == scelta.risposta:
        print("Risposta corretta!\n")
        j += 1
        lista_livello = []

    else:

        if opzioni[0] == scelta.risposta:
            stampa = 1

        elif opzioni[1] == scelta.risposta:
            stampa = 2

        elif opzioni[2] == scelta.risposta:
            stampa = 3

        elif opzioni[3] == scelta.risposta:
            stampa = 4

        print(f"Risposta sbagliata! La risposta corretta era: {stampa}\n")
        continuo = False

nickname = input(f"Hai totalizzato {j} punti!\nInserisci il tuo nickname: ")

# Memorizzo nickname e risultati

risultati = [Punteggio(nickname, j)]

with open('punti.txt', 'r') as file2:
    for line in file2:
        riga = line.split()
        p = Punteggio(riga[0], int(riga[1]))
        risultati.append(p)

risultati.sort(key = lambda x: x.punti, reverse = True)

with open('punti.txt', 'w') as file3:
    pass

    for r in risultati:
        file3.write(f"{r.nickname} {r.punti}\n")