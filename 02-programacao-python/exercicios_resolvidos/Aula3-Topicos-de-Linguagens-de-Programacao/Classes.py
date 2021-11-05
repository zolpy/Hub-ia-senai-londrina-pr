# Limpa Tela (CTRL+L) ou (CLEAR) ou 
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Usuario:
    def metodo_u_data2(self):
        # vivendo no seculo XXI utilizando ferramentas do século XVII: tudo no braço
        # https://advancedinstitute.ai/ai2-fiep-turma4
        # Entenda-se: leia-se os dados 
        self.db_data = open('dados/ml-100k/u.data')
        self.dados = self.db_data.read().splitlines()

        # O método splitlines () divide uma string em uma lista. A divisão é feita nas quebras de linha.
        #print(dados)

        # dando nomes aos bois (colunas)
        # De acordo com (https://github.com/virtualvector/Advanced-Movie-Recommender-System)
        # E também (https://towardsdatascience.com/build-your-own-recommender-system-within-5-minutes-30dd40388fbf)

        self.u_data_col = ['user_id', 'idade', 'rating', 'timestamp']

        # a ideia aqui não é formar uma especie de tabela como nesse exemplo 
        #(https://github.com/virtualvector/Advanced-Movie-Recommender-System)
        # mas sim criar um dicionário

        self.vetorD = [] #vetor com um dicionario dentro
            
        #cria-se um dicionario 
        self.d = {}

        #Faz-se percorrer linha x coluna
        for linha in self.dados:
            for coluna in self.u_data_col:

                # O método split () converte a string em outros tipos de dados, como listas, 
                # quebrando uma string em pedaços. Python nos fornece dois métodos: .split () e .rsplit ().
                self.celula = linha.split('\t')

                self.d[self.u_data_col[0]] = self.celula[0]
                #print(celula[0])
                self.d[self.u_data_col[1]] = self.celula[1]
                #print(celula[1])
                self.d[self.u_data_col[2]] = int(self.celula[2])
                #print(celula[2])
                self.d[self.u_data_col[3]] = self.celula[3]
                #print(celula[3])  
            self.vetorD.append(self.d.copy())
            #print(d)
            self.d.clear()
        #print(self.vetorD)
        return self.vetorD

    def metodo_u_data(self) -> None:
        vetorD = self.metodo_u_data2();
       # media de todas as avaliações:
        self.soma = 0
        self.data_user_avaliacoes_por_id = []
        self.data_user_rating =[]
        self.data_user_idade =[]

        for linha in vetorD:
            self.data_user_avaliacoes_por_id.append(linha['user_id'])
            self.data_user_idade.append(linha['idade'])
            self.data_user_rating.append(linha['rating'])
        
        #print(data_user_avaliacoes_por_id)
        #print(data_user_idade)
        #print(data_user_rating)

        self.media_rating = sum(self.data_user_rating)/len(self.vetorD)
        print('#'*80)
        print(f'Tamanho dos dados: {len(self.dados)} \n')
        print(f'Rating máximo: {max(self.data_user_rating)} \n')
        print(f'Rating Mínimo: {min(self.data_user_rating)} \n')
        print(f'Média dos Ratings: {self.media_rating} \n')
        print(f'Soma tabela_ratings: {sum(self.data_user_rating)} \n')
        print('#'*80)

        ################################################################################
        ## Encontrar:
        #1. O(s) usuário(s) mais crítico(s) na avaliação de filmes.
        # Encontrar aquele id cujas notas são, em média, as menores;
        # Para saber isso é necessário carregar a base de dados dos usuarios
        vetorD = self.metodo_u_data2();
   
        self.db_user = open('dados/ml-100k/u.user')
        self.user = self.db_user.read().splitlines()

        self.u_user_id = []

        for linha in self.user:
            self.celula = linha.split("|")
            self.u_user_id.append(self.celula[0])
            
        print(f'Quantidade de usuarios na base de dados: {len(self.u_user_id)} \n')
        #print(f'u_user_id:')
        #print(u_user_id)
        print('\n')


        # Vamos calcular a média por ID:
        soma = 0
        quant_votos = 0
        self.u_user_media_rating = []
        self.u_user_tabela_rating = []

        self.u_user_col = ['user_id', 'media', 'votos']
        self.u_user_dicionario = {}

        for user in self.u_user_id:
            for celula in vetorD:
                if celula['user_id'] == user:
                    #u_user_tabela_rating.append(celula['rating'])
                    soma += celula['rating']
                    quant_votos += 1
            
            #u_user_media_rating.append(celula[0])
            self.u_user_dicionario[self.u_user_col[0]] = user
            self.u_user_dicionario[self.u_user_col[1]] = (soma/quant_votos)
            self.u_user_dicionario[self.u_user_col[2]] = quant_votos
            self.u_user_media_rating.append(self.u_user_dicionario.copy())
            self.u_user_dicionario.clear()
            soma = 0
            quant_votos = 0
                
        #print(u_user_media_rating[:6])     

        #Respondendo a pergunta
        self.u_user_media_por_usuario = []
        self.menor_que_a_media_geral=[]

        for linha in self.u_user_media_rating:
            med = linha['media']
            self.u_user_media_por_usuario.append(med)
            if linha['media'] < self.media_rating:
                self.menor_que_a_media_geral.append(med)

        self.menor_que_a_media_geral.sort()
        ###print(f'\nMédia por usuário dos 12: \n {menor_que_a_media_geral[:len(menor_que_a_media_geral)]}\n')
        print(f'\nMédia por usuário dos 12: \n {self.menor_que_a_media_geral[:12]}\n')     

        print ('Encontrar aquele id cujas notas são, em média, as menores: \n', end=' ')
        for item in range(0,5):
            for linha in self.u_user_media_rating:
                if self.u_user_media_por_usuario[item] == linha['media']:
                    print(linha['user_id'], end=' ')


################################################################################
# 1. Classe `Filme` contendo os dados relativos ao filme (arquivo `u.item`) e com as seguintes responsabilidades:
#  * Cálculo da avaliação média;
# leitura do arquivo u.item
    def metodo_u_item(self) -> None:
        vetorD = self.metodo_u_data2;
        self.u_item = open('dados/ml-100k/u.item', encoding='iso-8859-1') 
        self.u_item_filmes = self.u_item.read().splitlines()
        print(f'\n\nu_item_filmes\n{self.u_item_filmes[0]} \n')

        self.u_item_col = ['movies_id', 'name', 'years','genre']
        self.u_genre_col = ['Unknown', 'Action', 'Adventure', 'Animation', 'Children','Comedy','Crime',
                    'Documentary', 'Drama','Fantasy','Film-Noir', 'Horror','Musical','Mystery',
                    'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'] 

        self.u_item_ids_filmes = [] 
        self.u_item_names = []  
        self.u_item_years = []   
        self.u_item_genre = []

        self.d = {}

        for linha in self.u_item_filmes:
            celula = linha.split("|")
            date = celula[2].split("-")
            self.u_item_ids_filmes.append(celula[0])
            self.u_item_names.append(celula[1])
            self.u_item_years.append(date[len(date)-1])

            for coluna in self.u_genre_col:
                self.d[self.u_genre_col[0]] = celula[5]
                self.d[self.u_genre_col[1]] = celula[6]
                self.d[self.u_genre_col[2]] = celula[7]
                self.d[self.u_genre_col[3]] = celula[8]
                self.d[self.u_genre_col[4]] = celula[9]
                self.d[self.u_genre_col[5]] = celula[10]
                self.d[self.u_genre_col[6]] = celula[11]
                self.d[self.u_genre_col[7]] = celula[12]
                self.d[self.u_genre_col[8]] = celula[13]
                self.d[self.u_genre_col[9]] = celula[14]
                self.d[self.u_genre_col[10]] = celula[15]
                self.d[self.u_genre_col[11]] = celula[16]
                self.d[self.u_genre_col[12]] = celula[17]
                self.d[self.u_genre_col[13]] = celula[18]
                self.d[self.u_genre_col[14]] = celula[19]
                self.d[self.u_genre_col[15]] = celula[20]
                self.d[self.u_genre_col[16]] = celula[21]
                self.d[self.u_genre_col[17]] = celula[22]
                self.d[self.u_genre_col[18]] = celula[23]
                
                self.u_item_genre.append(self.d.copy())
        print(f'\n\nprintln(d)\n{self.d} \n')
        self.d.clear()
            
        print(f'Quantidade de filmes: {len(self.u_item_ids_filmes)} \n')
        #print(f'\nPrimeiros 5 titulos da lista: {u_item_names[:len(menor_que_a_media_geral)]} \n')
        print(f'\nPrimeiros 5 generos da lista: {self.u_item_genre[:5]} \n')
        print(f'\nPrimeiros 5 titulos da lista: {self.u_item_names[:5]} \n')


        u_item_media_rating = []

        soma = 0
        cont = 0
        d = {}

        #u_item_col2 = ['item_id', 'name', 'years','genre']

        for user in self.u_item_ids_filmes: 
            for item in self.vetorD:
                if item['idade'] == user:
                    soma += item['rating']
                    cont += 1
            self.d['idade'] = user
            self.d['média'] = (soma / cont)
            self.u_item_media_rating.append(d.copy())
            self.d.clear()
            soma = 0
            cont = 0

        print(f'u_item_media_rating: \n {self.u_item_media_rating[:5]} \n')

        #colocando em apenas um vetor as médias
        self.u_item_vetor_de_medias = []

        for i in self.u_item_media_rating:
            md = i['média']
            self.u_item_vetor_de_medias.append(md)
        print(f'u_item_vetor_de_medias: \n {self.u_item_vetor_de_medias[:5]} \n')


        #isso nao acaba
        self.u_item_vetor_de_medias.sort()
        print(f'u_item_vetor_de_medias: \n {self.u_item_vetor_de_medias[:5]} \n')
        print('#'*105)
        print('O(s) filme(s) mais mal avaliado(s) pelos usuários: \n', end=' ')

        for i in u_item_media_rating:
            if self.u_item_vetor_de_medias[0] == i['média']:
                num = int(i['idade'])
                print(self.u_item_names[num-1], end = '; ')

#print(Usuario().metodo_u_data())
#print(Usuario().metodo_u_item())

if __name__ == '__main__':
    user = Usuario()

    #print(user.metodo_u_data2())
    print(user.metodo_u_data())


