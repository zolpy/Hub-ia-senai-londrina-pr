# vivendo no seculo XXI utilizando ferramentas do século XVII: tudo no braço

# Entenda-se: leia-se os dados 
db_data = open('dados/ml-100k/u.data')
dados = db_data.read().splitlines()

# O método splitlines () divide uma string em uma lista. A divisão é feita nas quebras de linha.
#print(dados)

# dando nomes aos bois (colunas)
# De acordo com (https://github.com/virtualvector/Advanced-Movie-Recommender-System)
# E também (https://towardsdatascience.com/build-your-own-recommender-system-within-5-minutes-30dd40388fbf)

u_data_col = ['user_id', 'celula_id', 'rating', 'timestamp']

# a ideia aqui não é formar uma especie de tabela como nesse exemplo 
#(https://github.com/virtualvector/Advanced-Movie-Recommender-System)
# mas sim criar um dicionário

vetorD = [] #vetor com um dicionario dentro
    
#cria-se um dicionario 
d = {}

#Faz-se percorrer linha x coluna
for linha in dados:
    for coluna in u_data_col:

        # O método split () converte a string em outros tipos de dados, como listas, 
        # quebrando uma string em pedaços. Python nos fornece dois métodos: .split () e .rsplit ().
        celula = linha.split('\t')

        d[u_data_col[0]] = celula[0]
        #print(celula[0])
        d[u_data_col[1]] = celula[1]
        #print(celula[1])
        d[u_data_col[2]] = int(celula[2])
        #print(celula[2])
        d[u_data_col[3]] = celula[3]
        #print(celula[3])  
    vetorD.append(d.copy())
    #print(d)
    d.clear()
#print(vetorD)

# media de todas as avaliações:
soma = 0
data_user_avaliacoes_por_id = []
data_user_rating =[]
data_user_celula_id =[]

for linha in vetorD:
    data_user_avaliacoes_por_id.append(linha['user_id'])
    data_user_celula_id.append(linha['celula_id'])
    data_user_rating.append(linha['rating'])
  
#print(data_user_avaliacoes_por_id)
#print(data_user_celula_id)
#print(data_user_rating)

media_rating = sum(data_user_rating)/len(vetorD)

print(f'\nA quantidade de usuários é: {len(data_user_avaliacoes_por_id)}\n')
print(f'Rating máximo: {max(data_user_rating)} \n')
print(f'Rating Mínimo: {min(data_user_rating)} \n')
print(f'Média dos Ratings: {media_rating} \n')
print(f'Soma tabela_ratings: {sum(data_user_rating)} \n')
print(f'Tamanho dos dados: {len(dados)} \n')

################################################################################
## Encontrar:
#1. O(s) usuário(s) mais crítico(s) na avaliação de filmes.
# Encontrar aquele id cujas notas são, em média, as menores;
# Para saber isso é necessário carregar a base de dados dos usuarios

db_user = open('dados/ml-100k/u.user')
user = db_user.read().splitlines()

u_user_id = []

for linha in user:
    celula = linha.split("|")
    u_user_id.append(celula[0])
    
print(f'Quantidade de usuarios na base de dados: {len(u_user_id)} \n')
#print(f'u_user_id:')
#print(u_user_id)
print('\n')


# Vamos calcular a média por ID:
soma = 0
quant_votos = 0
u_user_media_rating = []
u_user_tabela_rating = []

u_user_col = ['user_id', 'media', 'votos']
u_user_dicionario = {}

for user in u_user_id:
    for celula in vetorD:
        if celula['user_id'] == user:
            #u_user_tabela_rating.append(celula['rating'])
            soma += celula['rating']
            quant_votos += 1
    
    #u_user_media_rating.append(celula[0])
    u_user_dicionario[u_user_col[0]] = user
    u_user_dicionario[u_user_col[1]] = (soma/quant_votos)
    u_user_dicionario[u_user_col[2]] = quant_votos
    u_user_media_rating.append(u_user_dicionario.copy())
    u_user_dicionario.clear()
    soma = 0
    quant_votos = 0
        
#print(u_user_media_rating[:6])     

#Respondendo a pergunta
u_user_media_por_usuario = []
menor_que_a_media_geral=[]

for linha in u_user_media_rating:
    med = linha['media']
    u_user_media_por_usuario.append(med)
    if linha['media'] < media_rating:
       menor_que_a_media_geral.append(med)

menor_que_a_media_geral.sort()
###print(f'\nMédia por usuário dos 12: \n {menor_que_a_media_geral[:len(menor_que_a_media_geral)]}\n')
print(f'\nMédia por usuário dos 12: \n {menor_que_a_media_geral[:12]}\n')

print ('Encontrar aquele id cujas notas são, em média, as menores: \n', end=' ')
for item in range(0,5):
        for linha in u_user_media_rating:
            if u_user_media_por_usuario[item] == linha['media']:
                print(linha['user_id'], end=' ')

#print(u_user_media_rating)
#print(u_user_media_por_usuario)
################################################################################
# Encontrar
# 2. O(s) filme(s) mais mal avaliado(s) pelos usuários.

# leitura do arquivo u.item

u_item = open('dados/ml-100k/u.item', encoding='iso-8859-1') 
u_item_filmes = u_item.read().splitlines()
print(f'\n\nu_item_filmes\n{u_item_filmes[0]} \n')

u_item_col = ['movies_id', 'name', 'years','genre']
u_genre_col = ['Unknown', 'Action', 'Adventure', 'Animation', 'Children','Comedy','Crime',
               'Documentary', 'Drama','Fantasy','Film-Noir', 'Horror','Musical','Mystery',
               'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'] 

u_item_ids_filmes = [] 
u_item_names = []  
u_item_years = []   
u_item_genre = []

d = {}

for linha in u_item_filmes:
    celula = linha.split("|")
    date = celula[2].split("-")
    u_item_ids_filmes.append(celula[0])
    u_item_names.append(celula[1])
    u_item_years.append(date[len(date)-1])

    for coluna in u_genre_col:
        d[u_genre_col[0]] = celula[5]
        d[u_genre_col[1]] = celula[6]
        d[u_genre_col[2]] = celula[7]
        d[u_genre_col[3]] = celula[8]
        d[u_genre_col[4]] = celula[9]
        d[u_genre_col[5]] = celula[10]
        d[u_genre_col[6]] = celula[11]
        d[u_genre_col[7]] = celula[12]
        d[u_genre_col[8]] = celula[13]
        d[u_genre_col[9]] = celula[14]
        d[u_genre_col[10]] = celula[15]
        d[u_genre_col[11]] = celula[16]
        d[u_genre_col[12]] = celula[17]
        d[u_genre_col[13]] = celula[18]
        d[u_genre_col[14]] = celula[19]
        d[u_genre_col[15]] = celula[20]
        d[u_genre_col[16]] = celula[21]
        d[u_genre_col[17]] = celula[22]
        d[u_genre_col[18]] = celula[23]
        
        u_item_genre.append(d.copy())
print(f'\n\nprintln(d)\n{d} \n')
d.clear()
    
print(f'Quantidade de filmes: {len(u_item_ids_filmes)} \n')
#print(f'\nPrimeiros 5 titulos da lista: {u_item_names[:len(menor_que_a_media_geral)]} \n')
print(f'\nPrimeiros 5 generos da lista: {u_item_genre[:5]} \n')
print(f'\nPrimeiros 5 titulos da lista: {u_item_names[:5]} \n')


u_item_media_rating = []

soma = 0
cont = 0
d = {}

#u_item_col2 = ['item_id', 'name', 'years','genre']

for user in u_item_ids_filmes: 
    for item in vetorD:
        if item['celula_id'] == user:
            soma += item['rating']
            cont += 1
    d['celula_id'] = user
    d['média'] = (soma / cont)
    u_item_media_rating.append(d.copy())
    d.clear()
    soma = 0
    cont = 0

print(f'u_item_media_rating: \n {u_item_media_rating[:5]} \n')

#colocando em apenas um vetor as médias
u_item_vetor_de_medias = []

for i in u_item_media_rating:
    md = i['média']
    u_item_vetor_de_medias.append(md)
print(f'u_item_vetor_de_medias: \n {u_item_vetor_de_medias[:5]} \n')


#isso nao acaba
u_item_vetor_de_medias.sort()
print(f'u_item_vetor_de_medias: \n {u_item_vetor_de_medias[:5]} \n')
print('#'*105)
print('O(s) filme(s) mais mal avaliado(s) pelos usuários: \n', end=' ')

for i in u_item_media_rating:
    if u_item_vetor_de_medias[0] == i['média']:
        num = int(i['celula_id'])
        print(u_item_names[num-1], end = '; ')

################################################################################
# Encontrar
# 3. O(s) filme(s) mais bem avaliado(s) pelos usuários.
u_item_vetor_de_medias.sort(reverse = True)

print(u_item_vetor_de_medias[:5])

print('#'*105)
print('Filmes mais bem avaliados')
print('#'*105)

for i in u_item_vetor_de_medias:
    if 4.4 < i < 5.0:
        for vaiPorra in u_item_media_rating:
            if i == vaiPorra['média']:
                num = int(vaiPorra['celula_id'])
                print(u_item_names[num-1], end='; ')

################################################################################
# Encontrar
# 4. Média de avaliação para cada gênero de filmes;
print('#'*105)
print(f'u_item_filmes[len(u_item_filmes)-1] \n {u_item_filmes[len(u_item_filmes)-1]}')    
print('#'*105)

itemid = []
genero_itemid = {}

for i, genero in enumerate(u_genre_col):
    for linha in u_item_filmes:
        l = linha.split('|')
        if l[i+5] == '1':
            itemid.append(l[0])
    genero_itemid[genero] = itemid[:]
    itemid.clear()

print(f'\ngenero_itemid {genero_itemid}\n')
print('#'*105)

soma = cont = 0

u_genre_medias = {}

for key, value in genero_itemid.items():
    for i in u_item_media_rating:
        for v in value:
            if v == i['celula_id']:
                soma += i['média']
                cont += 1
    media = soma/cont
    u_genre_medias[key] = media
    soma = cont = 0

print('Valor Apurado\n')
for k, v in u_genre_medias.items():
    print(f'{k:<20} {v:.2f}')

################################################################################
# Encontrar
# 5. Avaliação média de filmes por ano.
# Listar qual o ano com a melhor média de avaliação de filmes;
u_item_id_year = []


for linha in u_item_filmes:
    celula = linha.split("|")
    date_full = celula[2].split("-")
    year = date_full[len(date_full)-1]
    d['celula_id'] = celula[0]
    d['ano'] = year
    u_item_id_year.append(d.copy())
    d.clear()

print('#'*105)
print(f'\nu_item_id_year[:5] \n {(u_item_id_year[:5])} \n')
print(f'\nu_item_years[:5] \n{(u_item_years[:5])} \n')

item = []
acaba_por_favor = {}

for u in u_item_years:
    for i in u_item_id_year:
        if i['ano'] == u:
            item.append(i['celula_id'])
    acaba_por_favor[u] = item[:]
    item.clear()

print('#'*105)
print(f'acaba_por_favor: \n {acaba_por_favor}')

md_ano = {}

for key, value in acaba_por_favor.items():
    for par in u_item_media_rating:
        for i in value:
            if i == par['celula_id']:
                soma += par['média']
                cont += 1
    media = soma / cont
    md_ano[key] = media
    soma = cont = 0

print('#'*105)
print(f'md_ano \n {md_ano}\n')

max_key = max(md_ano, key=lambda key: md_ano[key])

print('Listar qual o ano com a melhor média de avaliação de filmes')
print('#'*20)
print(f'Ano: {max_key} \n')
print('#'*20)

################################################################################
# Encontrar
# 6. Qual a ocupação mais propensa a dar más avaliações a filmes;
db_user = open('dados/ml-100k/u.user')
usuarios = db_user.read().splitlines()

db_occupation = open('dados/ml-100k/u.occupation')
d_occupation = db_occupation.read().splitlines()

print('#'*105)
print(usuarios[:5])
print(d_occupation)

u_occupation = []
vetor = []
for linha in usuarios:
    celula = linha.split('|')
    usr = celula[0]
    ocp = celula[3]
    vetor.append(usr)
    vetor.append(ocp)
    u_occupation.append(vetor[:])
    vetor.clear()

print(f'u_occupation[:6] {u_occupation[:6]}\n')


occupation_users = {}

for i in d_occupation: 
    for j in u_occupation:
        if i == j[1]:
            vetor.append(j[0])
    occupation_users[i] = vetor[:]
    vetor.clear()


print(occupation_users)

u_occupation_medias = {}

for key, value in occupation_users.items(): 
    for i in u_user_media_rating:
        for v in value:
            if v == i['user_id']:
                soma += i['media']
                cont += 1
    media = soma / cont
    u_occupation_medias[key] = media
    soma = cont = 0 

print(f'u_occupation_medias:\n {u_occupation_medias}\n')

print('#'*105)
print('\n6. Qual a ocupação mais propensa a dar más avaliações a filmes')
print('Encontrar a média de avaliação para cada ocupação de usuário e mostrar os menores e maiores valores')

from operator import itemgetter
ano = sorted(md_ano.items(), key=itemgetter(1))
trampo = sorted(u_occupation_medias.items(), key=itemgetter(1))


print(f'ano:({ano[len(ano)-1][0]} ) ')
print(f'rating para este ano ({ano[len(ano)-1][1]:.2f})')
print('#'*10)
print(f'{trampo[len(trampo)-1][0]:<15}    {trampo[len(trampo)-1][1]:.2f}')
print(f'{trampo[0][0]:<15}    {ano[0][1]:.2f}')