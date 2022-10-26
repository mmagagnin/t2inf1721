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
import random
import json

#bloco de funcoes
#tarefa 1
def imprimeTabuleiro(g):
    s=""
    for i in range(1,5):
        posicao="p"+str(i)
        if (i)%2==0 and i!=4:
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
    if zero=="p1" or zero=="p4":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,3))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,2))
    elif zero=="p2" or zero=="p3":
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,1))
        cfg=copy.deepcopy(aux)
        lArestas.append(troca(cfg,4))
    return lArestas

#tarefa 2

def BFS_node(G,s):
    global visited
    global parents
    #Initialize vector os leve 0: L[0] = {}
    L = {}
    L[0] = []
    L[0].append(s)
    #Mark s as visited
    visited[s] = True
    for i in range(1,len(G.keys())):
        L[i] = []
        #For each u in L[i-1]
        for u in L[i-1]:
            #For each v in Adj[u]
            for v in G[u]:
                if visited[v] == False:
                    L[i].append(v)
                    parents[v] = u
                    visited[v] = True
        if len(L[i]) == 0:
            return L

def BFS(G):
    global visited
    global parents
    
    for key in G.keys():
        visited[key] = False
        parents[key] = 0
    
    count_component = 0
    components = []
    
    for s in G.keys():
        if visited[s] == False:
            print("Launch BFS")
            components.append(BFS_node(G,s))
            count_component+=1
    
    print("Graph with %d connected components"%count_component)
    return components



class Grafo:
    def __init__(self,cfg,d):
        self.config=cfg
        self.dic=d
        d[self.config]=self.dic

    def __str__(self):
        s=imprimeTabuleiro(self.dic)
        return s

#implementacao



#tarefa 1 - criacao do grafo de estados de espacos
lTuplas=list(itertools.permutations([0,1,2,3]))
dicConfigs={}
dAdj={}

for i in range(0,len(lTuplas)):
    name="cfg"+str(i)
    config=configuraTupla(lTuplas[i])
    dicConfigs[name]=config

print("dicConfigs criado")

print(dicConfigs)

for (nome,cfg) in dicConfigs.items():
    lArestas=arestas(cfg)
    lAdjs=[]
    for el in lArestas:
        nomeConfig=list(dicConfigs.keys())[list(dicConfigs.values()).index(el)]
        lAdjs.append(nomeConfig)
    dAdj[nome]=lAdjs

print(dAdj)
print("dAdj criado")

exportar=""

#tarefa 2
parents = dict(keys=dicConfigs.keys())
visited = dict(keys=dicConfigs.keys())

for key in dicConfigs.keys():
    parents[key] = None
    visited[key] = False

components = BFS(dAdj)
s="A quantidade de componentes conexos no grafo é %d"%len(components)
print(s)
exportar=exportar+s+"\n"

#tarefa 3
for key in dicConfigs.keys():
    visited[key] = False
    parents[key] = 0

dicionario={'p1': 0, 'p2': 2, 'p3': 3, 'p4': 1,}
configuracao=list(dicConfigs.keys())[list(dicConfigs.values()).index(dicionario)]
print(configuracao)
print(imprimeTabuleiro(dicConfigs[configuracao]))
camadas_bfs_cfg1 = BFS_node(dAdj,configuracao)

indice_ultima_camada = len(camadas_bfs_cfg1) - 2
ultima_camada = camadas_bfs_cfg1[indice_ultima_camada]

#Podemos pegar qualquer nó da última camada
no_maior_caminho_mais_curto = random.sample(ultima_camada,1)[0]

s="Nó com o maior caminho mais curto de %s até %s"%(configuracao,no_maior_caminho_mais_curto)
print(s)
exportar=exportar+s+"\n"
s="Tamanho do caminho = %d"%indice_ultima_camada
print(s)
exportar=exportar+s+"\n"

maior_caminho_mais_curto = [no_maior_caminho_mais_curto]
no_corrente = no_maior_caminho_mais_curto
for i in range(0,indice_ultima_camada):
    maior_caminho_mais_curto.append(parents[no_corrente])
    no_corrente = parents[no_corrente]

s="O maior caminho mais curto ate a configuracao dada é:"+str(maior_caminho_mais_curto)
print(s)
exportar=exportar+s+"\n"

for el in maior_caminho_mais_curto:
    print("Proximo movimento:")
    print(imprimeTabuleiro(dicConfigs[el]))

    #exportando os resultados
#iremos exportar o dicConfig e o dAdj para .json
#as outras respostas serao exportadas para .txt

json_dConfigs=json.dumps(dicConfigs)
fDConfigs=open("dconfigs.json","w")
fDConfigs.write(json_dConfigs)
fDConfigs.close()

json_dAdj=json.dumps(dAdj)
fDAdj=open("dadj.json","w")
fDAdj.write(json_dAdj)
fDAdj.close()

respostas=open("respostas.txt","w")
respostas.write(exportar)
respostas.close()