import streamlit as st
import Files.Code.graficos as graficos
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

def chamaPapelao():
    st.image('https://res.cloudinary.com/dmbamuk26/image/upload/v1640886908/Images/head_hub.png')
    st.title("File Upload Excel")
    st.subheader("File Upload Excel")
    excel_file = st.file_uploader("Upload file Excel", type=['xlsx', 'xls'])
    if excel_file is not None:
        # To See Details
        file_details = {"Filename": excel_file.name, "FileType": excel_file.type, "FileSize": excel_file.size}
        st.write(file_details)

        df_papelao = pd.read_excel(excel_file)
        data_reserva = df_papelao['Date']
        df_papelao.set_index('Date', inplace=True)
        st.markdown('### Filename: ***' + excel_file.name + '***')
        ############################################################
        # Mostra na tela o dataframe (df_papelao)
        st.dataframe(df_papelao)
        ############################################################

        ############################################################
        #Mostra o Dropna
        papelao = df_papelao.dropna()
        st.markdown("""
                ---
                ### Retirando os NaN com: "***.dropna()***
                """)
        # Utilização para guardar html
        # st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)', False)
        st.dataframe(papelao)
        ############################################################
        # Gráficos
        graficos.chamaObservado(papelao)
        ############################################################
        # padronizado
        padronizado = papelao.pct_change()[1:]
        st.markdown("""
                ---
                ### Padronização dos dados
                """)
        st.dataframe(padronizado)
        ############################################################
        # BoxPlot dos dados
        graficos.chamaBoxplot(papelao)
        ###################################################################
        # Analisando tendencias

        st.markdown("""
                ---
                ### Analisando tendências
                """)
        # Radio
        chute = st.radio(
            "Escolha uma das colunas para ver os gráficos de tendências",
            ('Opção 1: Anguti',
             'Opção 2: Risi')
        )
        if chute == 'Opção 1: Anguti':
            NOME_COLUNA = 'Anguti'
            decomposicao = seasonal_decompose(papelao[NOME_COLUNA], model='additive', extrapolate_trend='freq')
            graficos.chamaDecomposicao(decomposicao, NOME_COLUNA)

        elif chute == 'Opção 2: Risi':
            NOME_COLUNA = 'Risi'
            decomposicao = seasonal_decompose(papelao[NOME_COLUNA], model='additive', extrapolate_trend='freq')
            graficos.chamaDecomposicao(decomposicao, NOME_COLUNA)

        ############################################################
        # chama a função Heatmap
        st.markdown("""
            > O gráfico abaixo mostra que o índice Anguti tem correlação direta com quase todos os outros índices, com exceção com a Energia Elétrica e o Ativo RANI3.SA que mostra que quase não há correlação, pois o valor fica em torno de zero. 

            > As cores aqui são muito importante, uma vez que, mostra o quão correlacionado uma grandeza está da outra, sendo que o Anguti tem uma correlação de (0.6) com o IGP-m.   

            > O Risi se relaciona com o IPCA15 e também com o IPCA-E (0.5).""")
        graficos.chamaHeatmap(padronizado)
        ############################################################

        ############################################################
        # Comparação dos gráficos de observação dos melhores avaliados no mapa de calor
        st.markdown("""
                ---
                ### Escolha a opção para os gráficos
                """)
        op1 = st.selectbox("Opção 1", papelao.columns)
        op2 = st.selectbox("Opção 2", papelao.columns)
        graficos.chamaCompara(papelao, op1, op2,padronizado)
        ############################################################
