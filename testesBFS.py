# %% [markdown]
# ## Notebook para implementação e teste da BFS

# %% [markdown]
# ### Bibliotecas Necessárias

# %%
import itertools
import random
random.seed(0)

# %% [markdown]
# ## Criação do grafo fake
# 
# As células abaixo criam um grafo aleatório a partir de uma dada sequência de números.

# %%
possible_configs = list(itertools.permutations([0,1,2,3,4,5,6,7,8]))

qtd_configs = len(possible_configs)

possible_config_names = []

for i in range(1,qtd_configs+1):
    possible_config_names.append("cfg"+str(i))


# %%
grafo = {}
for cfg in possible_config_names:
    m_cfg = random.randint(0,10)
    grafo[cfg] = random.sample(possible_config_names,m_cfg)

grafo

# %%
parents = dict(keys=grafo.keys())
visited = dict(keys=grafo.keys())

for key in grafo.keys():
    parents[key] = None
    visited[key] = False

# %% [markdown]
# ## BFS e contagem de componentes conexos

# %%
def BFS_node(G,s):
    global visited
    global parents
    
    #Initialize vector os leve 0: L[0] = {}
    L = {}
    L[0] = []
    L[0].append(s)
    
    # print("L[0] = ",L[0])
    
    #Mark s as visited
    visited[s] = True
    
    #Não sei exatamente o ponto de parada do for
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
                    
        # print("L[%d] = "%i,L[i])
        
        if len(L[i]) == 0:
            return L

# %%
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
             

# %%
components = BFS(grafo)

# %%
components

# %% [markdown]
# ## Caminho mais curto
# 
# Para essa questão, assumo que a configuração final é *"cfg1"*.
# 
# Para resolver a questão, nós implementamos a BFS a partir do nó final e montamos sua árvore BFS.
# 
# A partir dela, sabemos o caminho mais curto do nó da configuração *"cfg1"* até todos os outros nós alcançaveis a partir dele (em seu componente conexo).
# 
# Sendo assim, para obter o nó com o maior caminho mais curto até *"cfg1"*, basta escolher qualquer nó da camada mais funda da árvore BFS e obter o caminho até a raiz.

# %% [markdown]
# A célula abaixo roda a BFS a partir do nó final *"cfg1"*, retornando as camadas da busca.

# %%
for key in grafo.keys():
    visited[key] = False
    parents[key] = 0
        
camadas_bfs_cfg1 = BFS_node(grafo,"cfg1")

camadas_bfs_cfg1

# %%
indice_ultima_camada = len(camadas_bfs_cfg1) - 2

ultima_camada = camadas_bfs_cfg1[indice_ultima_camada]

#Podemos pegar qualquer nó da última camada
no_maior_caminho_mais_curto = random.sample(ultima_camada,1)[0]

print("Nó com o maior caminho mais curto até cfg1 =>",no_maior_caminho_mais_curto)
print("Tamanho do caminho = %d"%indice_ultima_camada) #não sei se é esse valor ou se é ele +1

maior_caminho_mais_curto = [no_maior_caminho_mais_curto]
no_corrente = no_maior_caminho_mais_curto
for i in range(0,indice_ultima_camada):
    maior_caminho_mais_curto.append(parents[no_corrente])
    no_corrente = parents[no_corrente]

maior_caminho_mais_curto


