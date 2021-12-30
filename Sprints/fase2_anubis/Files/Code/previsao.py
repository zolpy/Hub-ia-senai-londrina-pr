# !pip install yfinance --upgrade --no-cache-dir
import streamlit as st

#importando as libs
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def chamaPrevisaoHexano(hexano):
    st.markdown(""" ### Aqui começa os dados da previsão do Hexano""")
    coluna_hexano = hexano[['RB=F']]
    coluna_hexano_dropado = coluna_hexano.dropna()
    st.markdown(""" > Tabela do hexano .dropna()""")
    st.table(coluna_hexano_dropado.head())
    ############################################################
    # plotar informação
    plt.figure(figsize=(16, 8))
    plt.title('Valores coluna_hexano_dropado')
    plt.plot(coluna_hexano_dropado)
    plt.grid()
    plt.xlabel('Data')
    plt.ylabel('Valores')
    st.pyplot()
    ############################################################
    # verifica a quantidade de linhas

    qtd_linhas = len(coluna_hexano_dropado)

    qtd_linhas_treino = round(.67 * qtd_linhas)

    qtd_linhas_teste = qtd_linhas - qtd_linhas_treino

    info = (
        f"qtd_linhas: {qtd_linhas} | "
        f"Linhas treino vai da 0:{qtd_linhas_treino} | "
        f"Linhas teste vai da {qtd_linhas_treino}:{qtd_linhas_treino + qtd_linhas_teste} | "
        f"Total de linhas:  {qtd_linhas}"
    )
    # st.write(info)
    ############################################################
    # separa em treino e teste
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(coluna_hexano_dropado)

    train = df_scaled[:qtd_linhas_treino]
    test = df_scaled[qtd_linhas_treino: qtd_linhas_treino + qtd_linhas_teste]

    # print(len(train), len(test))
    ############################################################
    # convert an array of values into a df matrix

    def create_df(df, steps=1):
        dataX, dataY = [], []
        for i in range(len(df) - steps - 1):
            a = df[i:(i + steps), 0]
            dataX.append(a)
            dataY.append(df[i + steps, 0])
        return np.array(dataX), np.array(dataY)

        # gerando dados de treino e teste

    steps = 15
    X_train, Y_train = create_df(train, steps)
    X_teste, Y_teste = create_df(test, steps)

    print(X_train.shape)
    print(Y_train.shape)
    print(X_teste.shape)
    print(Y_teste.shape)
    ############################################################
    # gerando os dados que o modelo espera

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_teste = X_teste.reshape(X_teste.shape[0], X_teste.shape[1], 1)
    # print(X_train,X_teste)

    # Montando a rede
    model = Sequential()
    model.add(LSTM(35, return_sequences=True, input_shape=(steps, 1)))
    model.add(LSTM(35, return_sequences=True))
    model.add(LSTM(35))
    model.add(Dropout(0.2))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    # st.write(model.summary())
    ############################################################
    # Treinamento do modelo

    validation = model.fit(X_train, Y_train, validation_data=(X_teste, Y_teste), epochs=100, batch_size=steps,verbose=2)
    # st.write(validation)
    ############################################################
    plt.plot(validation.history['loss'], label='Training loss')
    plt.plot(validation.history['val_loss'], label='Validation loss')
    plt.grid()
    plt.legend()
    st.pyplot()
    ############################################################
    # Fazendo a previsão
    prev = model.predict(X_teste)
    prev = scaler.inverse_transform(prev)
    # st.write(prev)
    ############################################################
    ############################################################
    plt.figure(figsize=(16, 8))
    # plt.plot(df_papelao['Anguti'][30:40])
    # plt.plot(coluna_hexano_dropado)
    plt.plot(prev)
    plt.legend(['preco do hexano', 'preço previsto'])
    plt.grid()
    st.pyplot()
    ############################################################
    # previsão para os proximos dias
    tamanho_teste = len(test)
    # st.write(tamanho_teste)
    ############################################################
    # Pegar os ultimos dias que sao o tamanho do meu step
    days_input_steps = tamanho_teste - steps
    # st.write(days_input_steps)
    ############################################################
    # transforma em array
    input_steps = test[days_input_steps:]
    input_steps = np.array(input_steps).reshape(1, -1)
    # st.write(input_steps)
    ############################################################
    # Transformar em lista
    list_output_steps = list(input_steps)
    list_output_steps = list_output_steps[0].tolist()
    # st.write(list_output_steps)
    ############################################################
    # loop para prever os proximos dias
    pred_output = []
    i = 0
    n_future = 10
    while (i < n_future):
        if (len(list_output_steps) > steps):
            input_steps = np.array(list_output_steps[1:])
            print("{} dia. Valores de entrada -> {}".format(i, input_steps))
            input_steps = input_steps.reshape(1, -1)
            input_steps = input_steps.reshape((1, steps, 1))
            # print(input_steps)
            pred = model.predict(input_steps, verbose=0)
            print("{} dia. Valor previsto -> {}".format(i, pred))
            list_output_steps.extend(pred[0].tolist())
            list_output_steps = list_output_steps[1:]
            # print(list_output_steps)
            pred_output.extend(pred.tolist())
            i = i + 1

        else:
            input_steps = input_steps.reshape((1, steps, 1))
            pred = model.predict(input_steps, verbose=0)
            print(pred[0])
            list_output_steps.extend(pred[0].tolist())
            print(len(list_output_steps))
            pred_output.extend(pred.tolist())
            i = i + 1

    # print(pred_output)
    # st.write(pred_output)
    ############################################################
    # Transforma a saida
    prev = scaler.inverse_transform(pred_output)
    prev = np.array(prev).reshape(1, -1)
    list_output_prev = list(prev)
    list_output_prev = list_output_prev[0].tolist()
    # st.write(list_output_prev)
    ############################################################
    # pegar as datas de previsão
    dates = pd.to_datetime(hexano.index)
    predict_dates = pd.date_range(list(dates)[-1] + pd.DateOffset(1), periods=10, freq='b').tolist()
    # st.write(predict_dates)
    ############################################################
    # criar dataframe de previsão

    forecast_dates = []
    for i in predict_dates:
        forecast_dates.append(i.date())

    df_forecast = pd.DataFrame({'data_pregao': np.array(forecast_dates), 'RB=F': list_output_prev})
    df_forecast['data_pregao'] = pd.to_datetime(df_forecast['data_pregao'])

    df_forecast = df_forecast.set_index(pd.DatetimeIndex(df_forecast['data_pregao'].values))
    df_forecast.drop('data_pregao', axis=1, inplace=True)

    st.write(df_forecast)
    ############################################################
    plt.figure(figsize=(16, 8))
    # plt.plot(df_papelao['Anguti'][30:40])
    plt.plot(hexano['RB=F'])
    plt.plot(df_forecast['RB=F'])
    plt.legend(['preco do hexano', 'preço previsto'])
    plt.grid()
    st.pyplot()
    # plt.show()
    ############################################################

    ############################################################

    ############################################################

    ############################################################

    ############################################################

    ############################################################