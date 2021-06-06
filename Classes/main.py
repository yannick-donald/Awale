from Joueur import Joueur


from Trou import Trou
t=Trou(4)

Plateau   =[[],[]]
J1=Joueur(1,"yre")
for i in range(2):
    for j in range(6):
        t=Trou(4)
        Plateau[i].append(t)
for i in range(2):
    for j in range(6):
        print(Plateau[i][j], end="\t")
    print()
print("\n\n")
J1.choix_trou(4,Plateau)

for i in range(2):
    for j in range(6):
        print(Plateau[i][j], end="\t")
    print()