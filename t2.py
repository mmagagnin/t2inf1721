'''
tabuleiro e regras:
1 2 3
4 5 6
7 8 9

no esquematico exibido ao longo do projeto, os numeros
de 1 a 8 representam suas respectivas pecas
o numero 0 representa o espaco vazio

possiveis movimentos:
posicao vazia -> movimento possivel a partir de outra posicao
1 -> 4 up || 2 left
2 -> 1 right || 5 up || 2 left
3 -> 2 right || 6 up
4 -> 1 down || 5 left || 7 up
5 -> 2 down || 4 right || 6 left || 8 up
6 -> 3 down || 5 right || 9 up
7 -> 4 down || 8 left
8 -> 7 right || 5 down || 9 left 
'''

def criaGrafo(l):
    g={
        "p1":l[0],
        "p2":l[1],
        "p3":l[2],
        "p4":l[3],
        "p5":l[4],
        "p6":l[5],
        "p7":l[6],
        "p8":l[7],
        "p9":l[8]
    }
    return g

def imprimeTabuleiro(g):
    s=""
    for i in range(1,10):
        posicao="p"+str(i)
        if (i)%3==0 and i!=9:
            s+="%d\n"%g[posicao]
        else:
            s+="%d "%g[posicao]
    return s

def validaTroca(ini,fin):
    if ini==1 and (fin==4 or fin==2):
        return True
    elif ini==2 and (fin==1 or fin==5 or fin==3):
        return True
    elif ini==3 and (fin==2 or fin==6):
        return True
    elif ini==4 and (fin==1 or fin== 5 or fin==7):
        return True
    elif ini==5 and (fin==2 or fin==4 or fin==6 or fin==8):
        return True
    elif ini==6 and (fin==3 or fin==5 or fin==9):
        return True
    elif ini==7 and (fin==4 or fin==8):
        return True
    elif ini==8 and (fin==7 or fin==5 or fin==9):
        return True
    elif ini==9 and (fin==6 or fin ==8):
        return True
    else:
        return False

def invertePos(g,n0,l):
    posicao="p"+str(n0)
    pos0=list(g.keys())[list(g.values()).index(0)]
    if validaTroca(int(pos0[1]),n0):
        nc=g
        aux=g[posicao]
        nc[pos0]=aux
        nc[posicao]=0
        l.append(nc)
        return nc
    else:
        return "TROCA NAO VALIDA"

listaConfigs=[]
dAdj={}

class Grafo:
    def __init__(self,cfg,pecas):
        self.config=cfg
        self.pecas=pecas
        self.dic=criaGrafo(pecas)
        listaConfigs.append(self.dic)

    def __str__(self):
        s=imprimeTabuleiro(self.dic)
        return s

    def troca(self,novaPos0):
        nc=invertePos(self.dic,novaPos0,listaConfigs)
        return nc

pecasg1=[1,2,3,4,5,6,7,8,0]
g1=Grafo("cfg1",pecasg1)
print(g1.dic)
print(g1)
g2=g1.troca(8)
print("\n")
print(g2)
print(dAdj)
