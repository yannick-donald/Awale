from Trou import Trou

class Joueur:

    def __init__(self, id, nom):

        self.nom =nom
        self.score =0
        self.id_joueur=id
      

    def  choix_trou(self,id_trou,plateau):

       n= plateau[self.id_joueur-1][id_trou-1].mise_a_zero()

       if n==0:
           print(" choisir une case non vide")

       for i in range(n):

           k=(self.id_joueur-1)*6+id_trou+i
           plateau[(k//6)%2][(id_trou+i)%6].ajoute_graines()