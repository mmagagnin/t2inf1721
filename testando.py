'''
def imprimeTabuleiro(l):
    s=""
    for i in range(0,9):
        if (i+1)%3==0 and i!=8:
            s+="%d\n"%l[i]
        else:
            s+="%d "%l[i]
    return s

#print(imprimeTabuleiro([1,2,3,4,5,6,7,8,0])) #funciona!
'''
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
9 -> 6 down || 8 right
'''
'''
#funcao que cria nova configuracao de grafo apos um movimento

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

def invertePos(g,n0):
    posicao="p"+str(n0)
    pos0=list(g.keys())[list(g.values()).index(0)]
    if validaTroca(int(pos0[1]),n0):
        nc=g
        aux=g[posicao]
        nc[pos0]=aux
        nc[posicao]=0
        return nc
    else:
        return "TROCA NAO VALIDA"

def imprimeTabuleiro(g):
    s=""
    for i in range(1,10):
        posicao="p"+str(i)
        if (i)%3==0 and i!=9:
            s+="%d\n"%g[posicao]
        else:
            s+="%d "%g[posicao]
    return s

def atualizaListaAdj(dAdj,cfg1,cfg2):
    lCfg=dAdj.get(cfg1,[])
    lCfg.append(cfg2)
    dAdj[cfg1]=lCfg
    return dAdj

dAdj={}
g={'p1': 1, 'p2': 2, 'p3': 3, 'p4': 4, 'p5': 0, 'p6': 6, 'p7': 7, 'p8': 8, 'p9': 5}
print(imprimeTabuleiro(g))
nc=invertePos(g,4)
print(imprimeTabuleiro(nc))

def cfgsValidos(cfg1,cfg2):
    zero1=list(cfg1.keys())[list(cfg1.values()).index(0)]
    zero2=list(cfg2.keys())[list(cfg2.values()).index(0)]
    validaTroca(zero1,zero2)

d=[1,2]

def lala(d):
    d["a"]=2
    return 

lala(d)

print(d)

'''

def configuraTupla(t):
    d={}
    for i in range(0,len(t)):
        nome="p"+str(i+1)
        d[nome]=t[i]
    return d

t=(0,1,2)

d=configuraTupla(t)
print(list(d.keys())[list(d.values()).index(0)])

