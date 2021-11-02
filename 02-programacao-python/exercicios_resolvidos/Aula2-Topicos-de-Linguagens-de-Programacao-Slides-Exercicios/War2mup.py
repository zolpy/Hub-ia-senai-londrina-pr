#Para esse exercicio foi usado como referencia os sites:
#https://dadosaocubo.com/sistemas-de-recomendacoes-com-surprise/
#https://movile.blog/sistemas-de-recomendacao-com-filtros-colaborativos/
#https://www.alura.com.br/conteudo/introducao-a-sistemas-de-recomendacao-com-python
#https://minerandodados.com.br/cafe-com-codigo-tratando-valores-faltantes-pandas-python/
# https://gutx.com.br/item/ppmrrDr8ecf9.html

# Limpa Tela (CTRL+L) ou (CLEAR) ou 
import os
os.system('cls' if os.name == 'nt' else 'clear')

# importa a lib pandas
import pandas as pd

# Dataset com o detalhe dos Filmes
movies = pd.read_csv('dados/ml-latest-small/movies.csv')

# Dataset com as avaliações
ratings = pd.read_csv('dados/ml-latest-small/ratings.csv')

# Juntando as informações de filmes e avaliações
filmes = ratings.join(movies.set_index('movieId'), on='movieId')

# Números dos datasets
print('#'*105)
print('\n#INFORMACÕES DOS DATASETS\n')
print('#Quantidade de Filmes Avaliados: ',
filmes['movieId'].value_counts().shape[0])
 
print('#Quantidade de Usuários Avaliando: ',
filmes['userId'].value_counts().shape[0])
 
print('#Quantidade de Avaliações: ',
ratings.shape[0])
print('#'*105)

# Quantidade de Avaliações TOP5 Filmes
print('\n#Quantidade de Avaliações TOP5 Filmes:\n\n',filmes['title'].value_counts().head())
print('#'*105)

# Quantidade de Avaliações TOP5 por Usuários
print('\n#Quantidade de Avaliações TOP5 por Usuários:\n\n',filmes['userId'].value_counts().head())
print('#'*105)

#Usuários ID
print('\n#Tabela de ID dos Usuarios:\n\n',filmes['userId'].unique())
print('#'*105)

# Tamanho 
print('\n#Quantidade de usuarios: ',len(filmes['userId'].unique()))
print('#'*105)

# Filmes ID
print('\n#Filmes_ID:\n\n',filmes['movieId'].unique())
print('#'*105)

# Quantidade de filmes ID
print('\n#Quantidade de Filmes_ID: ',len(filmes['movieId'].unique()))
print('#'*105)

# Rating Minimo 
print('\n#Rating Minimo: ',filmes['rating'].min() )

# Rating Máximo 
print('\n#Rating Máximo: ',filmes['rating'].max() )
print('#'*105)

# Quais são os filmes avaliados por um determinado usuário?
# Avaliações do usuário 414
print('\n#Avaliações do usuário 414:\n\n',filmes.query('userId == 414').head())
print('#'*105)

print('\n#filmes.head \n\n',filmes.head ())
print('#'*105)

# Quantidade de Dados Vazios
print('\n#Quantidade de Dados Vazios:\n\n',filmes.isnull().sum())
print('#'*105)

# Dados Vazios
#print('\n#Dados Vazios:\n\n',filmes.isnull().head())

# Tipos dos dados
print('\n#Tipos dos dados\n\n',filmes.dtypes)
print('#'*105)

# Linhas x Colunas
print('\n#filmes.shape\n Linhas x Colunas\n',filmes.shape) 
print('#'*105)

# Criando uma Matriz de Utilidade
index=list(filmes['userId'].unique())
columns=list(filmes['movieId'].unique())
index=sorted(index)
columns=sorted(columns)
 
# Construindo uma tabela de pivoteamento: 
pivotei=filmes.pivot_table(values='rating',index='userId',columns='movieId')
print('\n#Construindo uma tabela de pivoteamento:\n',pivotei) 
print('#'*105)

# Nan implica que o usuário não classificou o filme correspondente.
# (1) Esta é a matriz de utilidade; para cada um dos 610 usuários dispostos em linha; 
# cada coluna mostra a avaliação do filme dada por um determinado usuário.
# 
# (2) Observe que a maioria da matriz é preenchida com 'Nan', o que mostra que a maioria 
# dos filmes não é classificada por muitos usuários.
#
# (3) Para cada par filme-usuário, se a entrada NÃO for 'Nan', o valor indica a classificação 
# dada pelo usuário ao filme correspondente.
#
# (4) Por enquanto, irei preencher o valor 'Nan' com o valor '0'. 
# Mas observe que isso é apenas indicativo, um 0 significa SEM AVALIAÇÃO e não significa que o 
# usuário classificou 0 para aquele filme. Não representa nenhuma classificação.


# Quantidade de dados nulos/coluna:
print('\n#Quantidade de dados nulos/coluna (Pivotei):\n\n',pivotei.isnull().sum()) 
print('#'*105)

# value_counts:
print('\n#value_counts:\n\n',filmes['userId'].value_counts(ascending=True)) 
print('#'*105)

# dropna elimina os dados nulos, vai usar como parametro as colunas ( axis = 1 ) 
# que tem menos de 20 valores sem ser nulos e prenche com zero os NaN (fillna)
dropei = pivotei.dropna(thresh=20, axis=1).fillna(0)
print('\n#Elimina os nulos (dropei):\n\n',dropei.head())
print('#'*105)

#https://movile.blog/sistemas-de-recomendacao-com-filtros-colaborativos/
#https://linux.ime.usp.br/~dududcbier/mac0499/monografia.pdf
# Similaridade do Cosseno
# Para medir a similaridade, basta calcular o ângulo entre os vetores.
# Quanto menor o ângulo maior a similaridade.
# Para verificar, basta lembrar das propriedades da função cosseno:
# Cos(0°) = 1
# Cos(90°) = 0
# Cos(180°) = -1

def standardize(linha):
    normalizacao = (linha - linha.mean()) / (linha.max() - linha.min())
    return normalizacao

padronizados = dropei.apply(standardize)

print('\n#Dados Padronizados:\n\n',padronizados.head())
print('#'*105)

#Professor do céu, não sei fazer isso no braço vou usar uma biblioteca
#chamada sklearn
from sklearn.metrics.pairwise import cosine_similarity
similaridade= cosine_similarity(padronizados.T) # o T aqui no final é transposta
print('\n#Similaridade do Cosseno (Transposta): \n\n',similaridade)

# Construindo uma matriz com os dados da similaridade
matrix = pd.DataFrame(data=similaridade, columns = padronizados.columns, index = padronizados.columns)

# a patir da transposta, cria-se um Banco de Dados com os filmes, já similarizados
print('\n#matrix.head(): \n\n',matrix.head())

#Coloque a ID do seu filme (movie_id) e a nota para ele (user_rating)
movie_id= 10
user_rating=5

print('\n#Para esse filme cuja ID é ({}) temos essas informações: \n\n'.format(movie_id),filmes.query('movieId == {}'.format(movie_id)).head())
print('#'*105)

# realizar o calculo da similaridade
# Fazer recomendação com a ID do filme e uma determinada avaliação
# Buscar o Filme pela ID
  
similar_score = matrix[movie_id]*(user_rating)
similar_score = similar_score.sort_values(ascending=False)
    
print('\n#O sistema recomendou esses filmes: \n\n', similar_score)