import copy

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

def imprimeTabuleiro(g):
    s=""
    for i in range(1,10):
        posicao="p"+str(i)
        if (i)%3==0 and i!=9:
            s+="%d\n"%g[posicao]
        else:
            s+="%d "%g[posicao]
    return s

g1={'p1': 0, 'p2': 1, 'p3': 2, 'p4': 3, 'p5': 4, 'p6': 5, 'p7': 6, 'p8': 7, 'p9': 8}

print(imprimeTabuleiro(g1))
#nc=troca(g1,2)
print()
#print(imprimeTabuleiro(nc))
l=arestas(g1)
print(l)