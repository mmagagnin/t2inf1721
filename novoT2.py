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

import itertools
import copy

def imprimeTabuleiro(g):
    s=""
    for i in range(1,10):
        posicao="p"+str(i)
        if (i)%3==0 and i!=9:
            s+="%d\n"%g[posicao]
        else:
            s+="%d "%g[posicao]
    return s

def configuraTupla(t):
    d={}
    for i in range(0,len(t)):
        nome="p"+str(i+1)
        d[nome]=t[i]
    return d

def invertePos(g,n0):
    posicao="p"+str(n0)
    pos0=list(g.keys())[list(g.values()).index(0)]
    nc=g
    aux=g[posicao]
    nc[pos0]=aux
    nc[posicao]=0
    return nc

def troca(dic,novaPos0):
    nc=invertePos(dic,novaPos0)
    return nc

def arestas(aux):
    lArestas=[]
    zero=list(aux.keys())[list(aux.values()).index(0)]
    if zero=="p1":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,4))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,2))
    elif zero=="p2":
        aux=copy.deepcopy(cfg)
        lArestas.append(troca(cfg,1))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,5))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,2))
    elif zero=="p3":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,2))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,6))
    elif zero=="p4":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,1))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,5))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,7))
    elif zero=="p5":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,2))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,4))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,6))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,8))
    elif zero=="p6":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,3))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,5))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,9))
    elif zero=="p7":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,4))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,8))
    elif zero=="p8":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,7))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,5))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,9))
    elif zero=="p9":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,6))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,8))
    return lArestas


class Grafo:
    def __init__(self,cfg,d):
        self.config=cfg
        self.dic=d
        d[self.config]=self.dic

    def __str__(self):
        s=imprimeTabuleiro(self.dic)
        return s

lTuplas=list(itertools.permutations([0,1,2,3,4,5,6,7,8]))
dicConfigs={}
dAdj={}

#ok
for i in range(0,len(lTuplas)):
    name="cfg"+str(i)
    config=configuraTupla(lTuplas[i])
    dicConfigs[name]=config

print("dicConfigs criado")

#print(dicConfigs)

for (nome,cfg) in dicConfigs.items():
    lArestas=arestas(cfg)
    lAdjs=[]
    for el in lArestas:
        nomeConfig=list(dicConfigs.keys())[list(dicConfigs.values()).index(el)]
        lAdjs.append(nomeConfig)
    dAdj[nome]=lAdjs

#print(dAdj)
print("dAdj criado")
