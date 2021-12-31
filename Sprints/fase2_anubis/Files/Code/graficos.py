import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.ar_model import AR

############################################################
#Função para plotar os gráfico da decomposição
def chamaDecomposicao(decomposicao,NOME_COLUNA):

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(20, 10))
    decomposicao.observed.plot(ax=ax1, title="Observado para " + NOME_COLUNA)
    decomposicao.trend.plot(ax=ax2, title="Tendência para " + NOME_COLUNA)
    decomposicao.seasonal.plot(ax=ax3, title="Sazonal para " + NOME_COLUNA)
    decomposicao.resid.plot(ax=ax4, title="Resisual para " + NOME_COLUNA)

    # ajusta o layout
    plt.tight_layout()
    st.pyplot()
############################################################
def chamaCompara(papelao,padronizado):
    st.markdown("""
        ---
        #### Compare os gráficos melhores avaliados no mapa de calor

        >> Escolha a opção para os gráficos
        """)
    op1 = st.selectbox("Opção 1", papelao.columns)
    op2 = st.selectbox("Opção 2", papelao.columns)

    NOME_GRAFICO = ''

    # Radio
    chute = st.radio(
        "Escolha para ver a comparação dos gráficos Observados ou Padronizados",
        ('Opção 1: Observados',
         'Opção 2: Padronizados')
    )
    if chute == 'Opção 1: Observados':
        NOME_GRAFICO = 'Observados'
        papelao[op1].plot(subplots=True, figsize=(12, 8), color='red', legend=op1);
        papelao[op2].plot(subplots=True, figsize=(12, 8), color='blue', legend=op2);

    elif chute == 'Opção 2: Padronizados':
        NOME_GRAFICO = 'Padronizados'
        padronizado[op1].plot(subplots=True, figsize=(12, 8), color='red', legend=op1);
        padronizado[op2].plot(subplots=True, figsize=(12, 8), color='blue', legend=op2);


    plt.suptitle('Gráficos ' + NOME_GRAFICO +': ' + op1 + ' com ' + op2, fontsize=20)
    plt.grid()
    st.pyplot()

############################################################
def chamaHeatmap(padronizado):
    st.markdown("""
        ---
        ### Heatmap
        Ao observar o gráfico abaixo verá que a escala varia de -1 a +1 isso indica que quanto mais perto de um ou outro as grandezas serão mais ou menos correlacionadas. Se estiver próximo de -1 indica que a relação é inversamente proporcional, ou seja, se uma grandeza aumenta, outra, diminui. E quanto mais próximo de +1 mais elas estão relacionadas. Em outras palavras, se uma aumenta a outra também aumenta. 
        
        > O gráfico abaixo mostra que o índice Anguti tem correlação direta com quase todos os outros índices, com exceção com a Energia Elétrica e o Ativo RANI3.SA que mostra que quase não há correlação, pois o valor fica em torno de zero. 

        > As cores aqui são muito importante, uma vez que, mostra o quão correlacionado uma grandeza está da outra, verificando qual quandeza tem maior ou menor correlação com a outra fica interessante fazer predições em uma delas e compara com a outra.   
       
        """)
    st.markdown(
        'Para saber mais sobre Heatmaps [clique aqui](https://www.guiadoexcel.com.br/grafico-heat-map-grafico-de-calor-no-excel/)',
        False)

    ax, fig = plt.subplots(figsize=(20, 5))
    sns.heatmap(padronizado.corr(), annot=True, vmax=1, vmin=-1, cmap='coolwarm');
    st.pyplot()
############################################################

############################################################
# BoxPlot dos dados

def chamaBoxplot(papelao):
    st.markdown("""
    ---
    ### BoxPlot dos dados
    """)
    st.markdown(
        'Para saber mais sobre BoxPlot [clique aqui](https://www.alura.com.br/artigos/melhorando-a-analise-com-o-boxplot)',
        False)
    ax = sns.boxplot(data=papelao, orient='v')
    ax.figure.set_size_inches(20, 5)
    ax.set_title('Boxplots', fontsize=18)
    ax.set_xlabel('Índices', fontsize=14)
    ax.set_ylabel('Valores', fontsize=14)
    ax.grid()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
###################################################################

###################################################################
def chamaObservado(papelao):
    st.markdown("""
            ---
            ### Gráficos Observados
             > Esses gráficos simplesmente plotam os valores contidos na tabela
            """)
    st.markdown('Para saber mais sobre gráficos observados [clique aqui](http://www.de.ufpb.br/~tarciana/CPEI/Aula2)', False)

    st.line_chart(papelao, width=600, height=500)
###################################################################

def chamaMediaMovel(retornos,op,intervalo):
    st.markdown("""
        ---
        ### Médias Móveis
        """)
    st.markdown('[Para saber mais acesse: ](https://www.tororadar.com.br/investimento/analise-tecnica/medias-moveis)', False)
    op1 = st.selectbox("Selecione a primeira coluna para visualizar as médias móveis", retornos.columns)
    op2 = st.selectbox("Selecione a segunda coluna para visualizar as médias móveis", retornos.columns)
    op3 = st.selectbox("Dias observados da média movel", [7,30,60,90,180,252])

    retornos[op1].rolling(op3).corr(retornos[op2]).plot(figsize=(22, 8),  title= op);

    plt.suptitle('Categorical Plotting')
    plt.grid()
    st.pyplot()
############################################################

def chamaPrevisaoPapelao(papelao,padronizado):
    st.markdown("""
        ---
        ### Aqui plota os gráficos observados e previstos
        """)
    NOME_COLUNA = ''
    if ('Anguti' in papelao.columns) and ('Risi' in papelao.columns):
        # Radio
        chute = st.radio(
            "Escolha uma das colunas para ver os gráficos de tendências",
            ('Opção A: Anguti',
             'Opção B: Risi')
        )

        if chute == 'Opção A: Anguti':
            NOME_COLUNA = 'Anguti'

        elif chute == 'Opção B: Risi':
            NOME_COLUNA = 'Risi'

    elif ('Anguti' in papelao.columns) and ('Risi' not in papelao.columns):
        NOME_COLUNA = 'Anguti'

    elif ('Anguti' not in papelao.columns) and ('Risi' in papelao.columns):
        NOME_COLUNA = 'Risi'

    sarima = SARIMAX(papelao[NOME_COLUNA], freq='MS', order=(2, 1, 2), seasonal_order=(2, 1, 2, 7)).fit()
    # sarima = SARIMAX(self.retorno[NOME_COLUNA], freq='MS', order=(2, 1, 2), seasonal_order=(2, 1, 2, 7)).fit()

    plt.figure(figsize=(15, 6))
    plt.plot(papelao[NOME_COLUNA], color='blue', label=NOME_COLUNA)
    # plt.plot(self.retorno[NOME_COLUNA], color='blue', label = NOME_COLUNA)
    plt.suptitle('Gráfico de predição para os dados Observados: ' + NOME_COLUNA, fontsize=20)
    plt.plot(sarima.predict(typ='levels'), color='red', label="Predição")
    plt.grid()
    plt.legend()
    plt.show()
    st.pyplot()

    ############################################################
    # esse lib foi descontinuada, pórem no google colab ela funciona
    # st.markdown("""
    #     ---
    #     ### Aqui plota outros gráficos de predição
    #     """)
    # train_size = int(len(padronizado[NOME_COLUNA]) * 2 / 3)
    #
    # train_set = papelao[NOME_COLUNA][:train_size]
    # test_set = papelao[NOME_COLUNA][train_size:]
    #
    # plt.figure(figsize=(15, 8))
    # plt.plot(train_set)
    # plt.plot(test_set)
    # plt.suptitle('Gráfico: ' + NOME_COLUNA, fontsize=20)
    # plt.legend()
    # plt.show()
    # st.pyplot()
    #
    # constante = AR(train_set, freq='MS').fit(2)
    # print(constante.params)
    #
    # previsoes = constante.params[0]
    # for i, param in enumerate(constante.params[1:]):
    #     previsoes += test_set.shift(i + 1) * param
    # print(previsoes)
    # plt.figure(figsize=(15, 8))
    # plt.plot(train_set)  # azul
    # plt.plot(test_set)  # laranja
    # plt.plot(previsoes)  # verde
    # plt.suptitle('Gráfico: ' + NOME_COLUNA, fontsize=20)
    # st.pyplot()
