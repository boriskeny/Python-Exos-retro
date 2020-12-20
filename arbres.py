class Ville:
    
    def __init__(self, l=[]):
        self.nom = l[0]
        self.numero = l[1]
        self.popul = l[2]
        self.superf = l[3]
        self.rang = l[4]
    
    def getRang(self):
        return self.rang
    
    def getSuperficie(self):
        return self.superf
    
    def afficherNom(self):
        print(self.nom)
        
    def afficherVille(self):
        print(self.nom)
class Arbre:
    def __init__(self, val=None, g=None,d=None):
        self.gauche = g
        self.droite = d
        self.val    = val
    def toString(self):
        print(f'{self.val}, {self.gauche}, {self.droite}')
    
    def parcours(self):
        return(f'({self.val}, {self.gauche.parcours() if self.gauche != None else self.gauche}, {self.droite.parcours() if self.droite!=None else self.droite})')

    def isVide(self):
        if self==None:
            return True
        else:
            return False

    def niveau(self):
        if self.isVide(): 
            return 0
        else: 
            return (1+max(0 if self.gauche==None else self.gauche.niveau(),0 if self.droite==None else self.droite.niveau()))
            
            
    
p1 = Arbre(5, None, None)
p2 = Arbre(9, None, None)
p2 = Arbre(7, p1  , p2)
p1 = Arbre(6, None, None)
p1 = Arbre(3, None, p1)
p1 = Arbre(1, p1  , p2)

print(p1.parcours())
print(p1.niveau())

