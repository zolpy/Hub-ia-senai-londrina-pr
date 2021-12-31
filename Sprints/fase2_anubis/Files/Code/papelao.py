import streamlit as st
import Files.Code.graficos as graficos
from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd

def chamaPapelao():
    st.image('https://res.cloudinary.com/dmbamuk26/image/upload/v1640886908/Images/head_hub')
    st.title("File Upload Excel")
    st.subheader("File Upload Excel")
    excel_file = st.file_uploader("Upload file Excel", type=['xlsx', 'xls'])
    if excel_file is not None:
        # To See Details
        file_details = {"Filename": excel_file.name, "FileType": excel_file.type, "FileSize": excel_file.size}
        st.write(file_details)
        df_papelao = pd.read_excel(excel_file)
        if ('Anguti' in df_papelao.columns) or ('Risi' in df_papelao.columns):
            # data_reserva = df_papelao['Date']
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
            st.markdown(
                'Para saber mais sobre dropna() [clique aqui](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)',False)
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
            st.markdown(
                'Para saber mais sobre normalização ou padronização [clique aqui](https://medium.com/ipnet-growth-partner/padronizacao-normalizacao-dados-machine-learning-f8f29246c12)',
                False)
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
            st.markdown(
                'Para saber mais sobre tendências [clique aqui](https://support.minitab.com/pt-br/minitab/18/help-and-how-to/modeling-statistics/time-series/how-to/trend-analysis/interpret-the-results/all-statistics-and-graphs/)',
                False)
            # st.markdown('> Nomes das colunas do arquivo')
            # st.markdown(papelao.columns)
            # st.markdown('> O Anguti está aí?')
            # st.markdown(('Anguti' in papelao.columns) ==True)
            # st.markdown('> O Risi está aí?')
            # st.markdown(('Risi' in papelao.columns) ==True)

            if ('Anguti' in papelao.columns) and ('Risi' in papelao.columns):
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

            elif ('Anguti' in papelao.columns) and ('Risi' not in papelao.columns):
                decomposicao = seasonal_decompose(papelao['Anguti'], model='additive', extrapolate_trend='freq')
                graficos.chamaDecomposicao(decomposicao, 'Anguti')

            elif ('Anguti' not in papelao.columns) and ('Risi' in papelao.columns):
                decomposicao = seasonal_decompose(papelao['Risi'], model='additive', extrapolate_trend='freq')
                graficos.chamaDecomposicao(decomposicao, 'Risi')
            ############################################################
            # chama a função Heatmap
            graficos.chamaHeatmap(padronizado)
            ############################################################
            # Comparação dos gráficos de observação dos melhores avaliados no mapa de calor
            graficos.chamaCompara(papelao, padronizado)
            ############################################################
            graficos.chamaPrevisaoPapelao(papelao,padronizado)
        else:
            st.markdown("## Arquivo não tem as colunas do Risi e/ou Anguti")
            st.dataframe(df_papelao)