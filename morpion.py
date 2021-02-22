from random import *
t={}

val = [0,1,2,3,4,5,6,7,8]

def init(t):
    for i in range(0,9):
        t[i]=' '


def afficherTexte(t):
    texte= f"\t{t[0]}{t[1]}{t[2]}\t012\n\t{t[3]}{t[4]}{t[5]}\t345\n\t{t[6]}{t[7]}{t[8]}\t678"
    texte2= f"+-----+-----+-----+\n|  {t[0]}  |  {t[1]}  |  {t[2]}  |\t0 1 2\n+-----+-----+-----+\n|  {t[3]}  |  {t[4]}  |  {t[5]}  |\t3 4 5\n+-----+-----+-----+\n|  {t[6]}  |  {t[7]}  |  {t[8]}  |\t6 7 8\n+-----+-----+-----+"
    print(texte2)


def remplir(t, v):
    # juste remplir une case libre
    '''
    for i in range(9):
        if t[i] == ' ':
            t[i]=v
            break
        else:
            pass
    '''
    t2=[]
    
    for i in range(9):
        if t[i]==' ': t2.append(i)
        
    shuffle(t2)
    t[t2[0]]=v
    
    
def verifier(t,v):
        
    if   t[0] == t[1] == t[2] == v:
        return True
    elif t[3] == t[4] == t[5] == v:
        return True
    elif t[6] == t[7] == t[8] == v:
        return True
    elif t[0] == t[3] == t[6] == v:
        return True
    elif t[1] == t[4] == t[7] == v:
        return True
    elif t[2] == t[5] == t[8] == v:
        return True
    elif t[0] == t[4] == t[8] == v:
        return True
    elif t[2] == t[4] == t[6] == v:
        return True
    else: return False


def remplirContre(t,lettre):
    gg = [[0,1,2],[3,4,5],[6,7,8],[0,3,4],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    coun = 0
    c=''
    if lettre =='X':
        c='O' 
    elif lettre=='O':
        c='X' 
    
    for g in gg:
        g2=[ t[g[i]] for i in range(3)]
        
        if g2.count(c)==2 and g2.count(' ')==1:    
            v = g2.index(' ')
            t[g[v]]=lettre
            break
        else: coun+=1
        
    if coun==8: remplirAtak(t, lettre)


def remplirAtak(t,lettre):
    gg = [[0,1,2],[3,4,5],[6,7,8],[0,3,4],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    coun = 0 
    
    for g in gg:
        g2=[ t[g[i]] for i in range(3)]
        
        if g2.count(lettre)==2 and g2.count(' ')==1:    
            v = g2.index(' ')
            t[g[v]]=lettre
            break
        else: coun+=1
        
    if coun==8: remplir(t, lettre)
        

def jouer(t):
    
        init(t)
        po=''
        px=''
        count= 0
        afficherTexte(t)
        while count!=9:
            '''
            while (po=='') or (po not in val) or (t[po] in ['X','O']):
                po = int(input('joueur O : '))
            t[po]='O'
            '''
            print('joueur O : ')
            remplirContre(t,'O')
            
            count+=1
            afficherTexte(t)
            if verifier(t, 'O'): break
            if count==9: 
                break
            
            while (px=='') or (px not in val) or (t[px] in ['X','O']):        
                px = int(input('joueur X : '))
            t[px]='X'
            '''
            print('joueur X : ')
            remplirContre(t,'X')
            '''
            count+=1
            afficherTexte(t)
            if verifier(t, 'X'): break
        
        print(quiGagne(t)+" !!!!!!👍")
        print("fin du jeu")
    
    
def quiGagne(t):
    if verifier(t, 'O') == True: return "joueur O"
    
    if verifier(t, 'X')==True: return "joueur X"
    if verifier(t, 'O')==False and verifier(t, 'X')==False:
        return "EGALITé"
         
    
def isVide(tv):
    return tv==tInit
    
    
def isFinish(t):
    nb=0
    for i in range(9):
        if t[i] != '.':
            nb+=1
    return nb

if __name__ == '__main__':
    jouer(t)            