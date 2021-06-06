# classe  pour un trou

class Trou :
    
    def __init__(self, nb_graines) :
      
      self.nb_graines = nb_graines
      
    def ajoute_graines(self):

      self.nb_graines +=1
    
    def mise_a_zero(self):
      n = self.nb_graines

      self.nb_graines =0

      return n
    def __str__(self) :
      return str(self.nb_graines)





