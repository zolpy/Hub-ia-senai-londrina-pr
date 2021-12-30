import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


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
def chamaCompara(papelao,op1,op2,padronizado):
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


    plt.suptitle('Gráficos ' + NOME_GRAFICO +' da/do: ' + op1 + ' com ' + op2, fontsize=20)
    plt.grid()
    st.pyplot()

############################################################
def chamaHeatmap(padronizado):
    st.markdown("""
        ---
        ### Heatmap
        Ao observar o gráfico abaixo verá que a escala varia de -1 a +1 isso indica que quanto mais perto de um ou outro as grandezas serão mais ou menos correlacionadas. Se estiver próximo de -1 indica que a relação é inversamente proporcional, ou seja, se uma grandeza aumenta, outra, diminui. E quanto mais próximo de +1 mais elas estão relacionadas. Em outras palavras, se uma aumenta a outra também aumenta. 
        """)
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
    ax = sns.boxplot(data=papelao, orient='v')
    ax.figure.set_size_inches(20, 5)
    ax.set_title('Boxplots', fontsize=18)
    ax.set_xlabel('Índices', fontsize=14)
    ax.set_ylabel('Valores', fontsize=14)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
###################################################################

###################################################################
def chamaObservado(papelao):
    st.markdown("""
            ---
            ### Gráficos Observados
            """)

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