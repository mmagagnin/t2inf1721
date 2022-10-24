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

from re import X

x=1

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

def createNewConfigName(i,cfg):
    myVars=vars()
    s="cfg"+str(i)
    myVars[s]=cfg
    return s

def cfgsValidos(cfg1,cfg2):
    zero1=list(cfg1.keys())[list(cfg1.values()).index(0)]
    zero2=list(cfg2.keys())[list(cfg2.values()).index(0)]
    validaTroca(zero1,zero2)

def removeCfgRepetida(dConfig,dAdj,cfg):
    lChaves=list(dConfig.keys())
    for i in range(len(lChaves)-1):
        if dConfig[lChaves[i]]==dConfig[cfg]:
            dConfig.pop(cfg) #essa linha nao esta funcionado - INVESTIGAR!
            dAdj.pop(cfg)
            for (c,l) in dAdj.items():
                if cfg in l:
                    l.remove(cfg)
    return

def atualizaDAdj(cfg1,cfg2,dAdj,dConfigs):
        #lista 1
        lCfg=dAdj.get(cfg1,[])
        lCfg.append(cfg2)
        dAdj[cfg1]=lCfg
        #lista 2
        lCfg2=dAdj.get(cfg2,[])
        lCfg2.append(cfg1)
        dAdj[cfg2]=lCfg2
        #vê se a configuracao é repetida
        removeCfgRepetida(dConfigs,dAdj,cfg2)
        return dAdj

dicConfigs={}
dAdj={}

class Grafo:
    def __init__(self,cfg,d):
        if type(d)==str:
            print("CFG NAO VALIDA")
            return None
        else:
            global x
            x+=1
            self.config=cfg
            self.dic=d
            d[self.config]=self.dic

    def __str__(self):
        s=imprimeTabuleiro(self.dic)
        return s

    def troca(self,n0):
        posicao="p"+str(n0)
        pos0=list(self.dic.keys())[list(self.dic.values()).index(0)]
        if validaTroca(int(pos0[1]),n0):
            nc=self.dic
            aux=nc[posicao]
            nc[pos0]=aux
            nc[posicao]=0
            global x
            name=createNewConfigName(x,nc)
            x+=1
            dicConfigs[name]=nc
            atualizaDAdj(self.config,name,dAdj,dicConfigs)
            return nc
        else:
            return "TROCA NAO VALIDA"
        

g1={'p1': 1, 'p2': 2, 'p3': 3, 'p4': 0, 'p5': 4, 'p6': 6, 'p7': 7, 'p8': 8, 'p9': 5}
cfg1=Grafo("cfg1",g1)
print("CFG1:")
print(cfg1)

g2=cfg1.troca(7)
cfg2=Grafo("cfg2",g2)
print("CFG2:")
print(cfg2)
print(dicConfigs)
print(dAdj)

g3=cfg2.troca(4)
cfg3=Grafo("cfg3",g3)
print("CFG3:")
print(cfg3)
print(dicConfigs)
print(dAdj)

g4=cfg3.troca(8)
cfg4=Grafo("cfg4",g4)


