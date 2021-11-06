# Limpa Tela (CTRL+L) ou (CLEAR) ou 
import os
os.system('cls' if os.name == 'nt' else 'clear')

import pandas as pd
import numpy as np


#Dando nomes aos bois
u_user_col = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
u_data_col = ['user_id', 'movie_id', 'rating', 'timestamp']
u_item_col = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']

#Carregando os dados
u_user = pd.read_csv('dados/ml-100k/u.user', sep='|',  names=u_user_col, encoding='latin-1')
u_data = pd.read_csv('dados/ml-100k/u.data', sep='\t', names=u_data_col, encoding='latin-1')
u_item = pd.read_csv('dados/ml-100k/u.item', sep='|',  names=u_item_col, usecols=range(5), encoding='latin-1')

print('#'*80)
print('u_user.head()')
print(u_user.head())

print('#'*80)
print('u_data.head()')
print(u_data.head())

print('#'*80)
print('u_item.head()')
print(u_item.head())

# Juntando as informações de filmes e avaliações
filmes = u_user.join(u_data.set_index('user_id'), on='user_id')

print('#'*80)
print('filmes')
print(filmes.head())

# create one merged DataFrame
movie_ratings = pd.merge(u_item, u_data)
lens = pd.merge(movie_ratings, u_user)

print('#'*80)
print('movie_ratings')
print(movie_ratings.head())

print('#'*80)
print('lens')
print(lens.head())

most_rated = lens.groupby('title').size().sort_values(ascending=False)[:25]
print('#'*80)
print('most_rated')
print(most_rated.head())

#Quais filmes são mais bem avaliados?
movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
print('#'*80)
print('Quais filmes são mais bem avaliados?\n')
print(movie_stats.head())

"""
Podemos usar o método agg para passar um dicionário especificando 
as colunas a agregar (como chaves) e uma lista de funções que gostaríamos de aplicar.

Vamos classificar o DataFrame resultante para que possamos ver quais 
filmes têm a pontuação média mais alta.
"""

# sort by rating average

print('movie_stats\n')
print(movie_stats.sort_values([('rating', 'mean')], ascending=False).head())

"""
Como movie_stats é um DataFrame, usamos o método de classificação - 
apenas objetos Series usam ordem. Além disso, como nossas colunas 
agora são um MultiIndex, precisamos passar uma tupla especificando como classificar.
"""

#### Considerando os dados de avaliação dos usuários
"""
1. Cálculo da média, desvio padrão e variância para o dataset de avaliações
   completo;
"""
print('#'*80)
print('Quais filmes são mais bem avaliados?\n')
atleast_100 = movie_stats['rating']['size'] >= 100
print(movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)[:15])
print(movie_stats[atleast_100].sort_values([('rating', 'std')], ascending=False)[:15])
