import yfinance as yf
import streamlit as st
import Files.Code.graficos as graficos
import Files.Code.previsao as prev_hexano


def chamaHexano():
    st.image('https://github.com/zolpy/Hub-ia-senai-londrina-pr/blob/main/Sprints/fase2_anubis/Files/Images/head.png')
    st.title("Dados caregados do Yahoo Finance")
    st.subheader("Hexano")
    menu = ["1 - Índices do petroleo", "2 - Principais moedas do mundo", "3 - Commodites", "4 - Proteína animal", "5 - Bolsa internacionais"]
    # tickers2 = ['RB=F', 'USD', 'BHDEUR=X', 'GBPEUR=X', 'KYDEUR=X', 'EURUSD=X', 'CHFEUR=X', 'BTC-USD']
    # op1 = st.selectbox("Opção 1", tickers1)
    op = st.radio("Escolha a base", menu)
    tickers =['']
    if (op == "1 - Índices do petroleo"):
        # choice = st.radio("Menu", menu)
        tickers = ['RB=F', 'BNO', 'NFTA.TA', 'UCO', 'CL=F', 'BZ=F', '^BVSP']
        siglas = ['# RB=F => Indice RBOB',
                  '# BNO => Indice United States Brent Oil Fund (BNO)',
                  '# NAFTA.TA => Indice do petróleo de Israel',
                  '# CL=F => Indice do Petróleo Cru da Bolsa de NY mercantille'
                  '# BZ=F => Brent Crude Oil Last Day Finance',
                  '# UCO => Nasdaq real time price Crude Oil'
                  ]
        st.dataframe(siglas)
    ############################################################
    elif (op == "2 - Principais moedas do mundo"):  #moedas
      tickers = ['RB=F', 'USD', 'BHDEUR=X', 'GBPEUR=X', 'KYDEUR=X', 'EURUSD=X', 'CHFEUR=X', 'BTC-USD']
      siglas = ['# RB=F => indice RBOB',
                  '# BHDEUR=X => Dinar do bahrein',
                  '# OMRQAR=X => Rial de Omã',
                  '# JODEUR=X => Dinar da Jordânia',
                  '# GBPEUR=X => Libra Esterlina',
                  '# KYDEUR=X => Dólar das Ilhas Cayman',
                  '# EURUSD=X => Euro',
                  '# CHFEUR=X => Franco Suíço',
                  '# BTC-USD => Bitcoin'
                  ]
      st.table(siglas)
    ############################################################
    elif (op == "3 - Commodites"):  # commodites
      tickers = ['RB=F', 'SOJA3.SA', 'SOJA3F.SA', 'FEFAX', 'WTI', 'PETR3.SA', 'SUZB3.SA', 'SUZB3F.SA']
      siglas = ['# RBOB Gasoline Jan 22 (RB=F)',
                '# Boa Safra Sementes S.A. (SOJA3.SA)',
                '# BOA SAFRA ON NM (SOJA3F.SA)',
                '# First Eagle Fund of America Class A (FEFAX)',
                '# W&T Offshore, Inc. (WTI)',
                '# Petróleo Brasileiro S.A. - Petrobras (PETR3.SA)',
                '# Suzano S.A. (SUZB3.SA)',
                '# SUZANO S.A. ON NM (SUZB3F.SA)'
                ]
      st.table(siglas)
    ############################################################
    elif (op == "4 - Proteína animal"):  # Proteina animal
        tickers = ['RB=F', 'BRFS3.SA', 'JBSS3.SA', 'BEEF3.SA', 'MRFG3.SA', '^BVSP']
        siglas = ['# RB=F => indice RBOB',
                  '# BRFS3.SA => ativo da Brazilians food',
                  '# JBSS3.SA => ativo da JBSS',
                  '# BEEF3.SA => ativo da Minerva Food',
                  '# MRFG3.SA => ativo da Marfrig',
                  '# BVSP => indice BOVESPA',
                  ]
        st.table(siglas)
    ############################################################
    elif (op == "5 - Bolsa internacionais"):  # Bolsa internacionais
        tickers = ['RB=F', '^NDX', '^IXIC', 'ENX.PA', 'JPXGY', '000001.SS', '^BVSP']
        siglas = ['# RB=F => indice RBOB',
                  '# ^NDX => NASDAQ 100 bolsa norte americana das 100 maiores empresas',
                  '# ^IXIC => NASDAQ composite bolsa norte americana',
                  '# ENX.PA => EURONEXT, bolsas de Paris, Amsterda e Bruxelas',
                  '# JPXGY => Japan exchange group',
                  '# 000001.SS => Shangai Composite index',
                  '# BVSP => indice BOVESPA'
                  ]
        st.table(siglas)
    ############################################################
    start = st.date_input('A partir de qual data você quer puxar a base de dados?')
    fim = st.date_input('E vai até quando?')
    intervalo = fim - start
    st.markdown('Quantiade de dias: ')
    intervalo = intervalo.days
    st.write((intervalo))
    hexano = yf.download(tickers, start=start, end=fim)["Close"]
    st.dataframe(hexano)
    ############################################################
    st.markdown('### Realizando a dropagem: retira NaN')
    hexano = hexano.dropna()
    st.dataframe(hexano)
    ############################################################
    #Padronização dos dados
    st.markdown('### Padronização dos dados')
    retornos = hexano.pct_change()[1:]
    st.dataframe(retornos)
    ############################################################
    # Gráfico Boxplot
    # st.markdown('### Gráfico Boxplot')
    graficos.chamaBoxplot(hexano)
    ############################################################
    st.markdown('### Matriz de correlação')
    st.markdown('[Para saber mais clique aqui](https://www.delftstack.com/pt/howto/python-pandas/pandas-correlation-matrix/)', False)
    st.dataframe(retornos.corr())
    ############################################################
    #Plota mapa de calor
    st.markdown('[Para saber mais sobre correlação ***clique aqui***](http://2engenheiros.com/2020/12/08/mapa-de-calor-r/)', False)
    graficos.chamaHeatmap(retornos)
    graficos.chamaMediaMovel(retornos, op,intervalo)

    ############################################################
    ##Aqui chama a função de previsao
    prev_hexano.chamaPrevisaoHexano(hexano)


