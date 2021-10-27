#!/bin/bash

#Esse programa foi feito em shell e se refere a como passar paramêtros ao programa pela linha de comandos (Paramêtros posicionais)
#./ftab.sh p1 p2 p3 pn
#    ^     ^  ^  ^  ^
#    $0    $1 $2 $3 $n
# Preferiu-se fazer uso da estrutura condicional case para gerar um menu de opções em Shell Script

#export PATH=$PATH:pwd"/"

AJUDA="
*****************************************
Software FTAB v1.0

-h   --help       Exibe ajuda e sai
-v   --version    Exibe versão e sai
-s   --sigla      Exibe o siginificado da SIGLA FTAB 
-l   --linhas     Quantidade de linhas do arquivo (2006-sample.csv)
-c   --colunas    Quantidade de colunas do arquivo (2006-sample.csv)
-e1  --exerc1     Descobrir a quantiade de atrasos de uma dada companhia passada como parâmetro. 
-e2  --ArrDelay   Descobrir o vôo com maior atraso na chegada (ArrDelay) registrado.
-e3  --DepDelay   Descobrir o vôo com maior atraso na saída (DepDelay) registrado.
-e4  --VooLongo   Descobrir o vôo mais longo (Distância).
-e5  --Diverted   Contar quantos vôos precisaram ser redirecionados (Diverted).
-e6  --calc       Calcular o tempo de atraso total para a companhia Delta Air Lines
-e7  --jfk        Mostrar o tempo total de atrasos para a decolagem de vôos no aeroporto JFK, de Nova Iorque.
-e8  --lax        Mostrar o tempo total de atrasos para pousos no Aeroporto Internacional de Los Angeles (LAX).
-b1  --bonus1     Listar qual companhia teve o maior tempo total de atrasos (atrasos somente na decolagem).
-b2  --bonus2     Listar qual aeroporto teve o maior tempo total de atrasos (atrasos somente na decolagem).
*****************************************
"

VERSAO="Versão 1.0"

case "$1" in
-h | --help)
       echo "$AJUDA"
;;

-v | --version)
       echo "$VERSAO"
;;
-t | --teste)
       echo "****************************"

       echo "****************************"
;;


-s | --sigla)
       echo "****************************"
       echo "FTAB significa Força Tarefa Afrânio e Brandão"
       echo -e "\nPara resolver alguns problemas precisamos sim de uma Força Tarefla, afinal,\ntrabalhar em equipe é melhor do que sozinho."
       echo "****************************"
;;

-l | --linhas)
       echo "****************************"
       echo "Quantidade de linhas do arquivo (2006-sample.csv)"
       echo "cat 2006-sample.csv | wc -l"
       cat  2006-sample.csv | wc -l
       echo "****************************"
;;

-c | --colunas)
       echo "****************************"
       echo "Quantidade de Colunas"
       echo "head -2 2006-sample.csv | tail -1 | tr ',' '\n' | wc -l"
       head -2 2006-sample.csv | tail -1 | tr ',' '\n' | wc -l
       echo "****************************"
;;

-e1 | --exerc1)
       echo "****************************(ok)" #DL 2277
       echo -e "Descobrir a quantiade de atrasos de uma dada companhia passada como parâmetro, em minutos.\n"
       echo "  AA      AQ      AS      B6      CO      DL      EV      F9     FL      HA"
       echo "  MQ      NW      OH      OO      TZ      UA      US      WN     XE      YV"
       read -p "Which company are you interested in? " companyname
       #cat 2006-sample.csv | cut -d, -f9,15,16 | cut -d, -f2,3 | grep '.,.' | wc -l
       echo "The company $companyname had a total of $(grep $companyname 2006-sample.csv | cut -d, -f9,15 | cut -d, -f2 | tail -n +2| grep -v '-'| grep -v '^$'| grep -v '0.0'| wc -l) late minutes."
       echo "****************************"
;;

-e2 | --ArrDelay)
       echo "****************************(ok)"
       echo "Descobrir o vôo com maior atraso na chegada (ArrDelay) registrado."
       #tail -n +2 2006-sample.csv | sort -t, -k15,15n | cut -d ',' -f10 | tail -n1
       bash e2.sh 2006-sample.csv
       echo "****************************"
;;

-e3 | --DepDelay)
       echo "****************************(ok)"
       echo "Descobrir o vôo com maior atraso na saída (DepDelay) registrado."
       echo -e "cat 2006-sample.csv | sort -n -t, -k16 | cut -d, -f10 | tail -1 \n"
       #tail -n +2 2006-sample.csv | sort -t, -k16,15n | cut -d ',' -f10 | tail -n1
       cat 2006-sample.csv | sort -n -t, -k16 | cut -d, -f10 | tail -1
       echo "****************************"
;;

-e4 | --VooLongo)
       echo "****************************4)"
       echo "Descobrir o vôo mais longo (Distância)."
       echo -e "Número $(tail -n +2 2006-sample.csv | sort -t, -k14,14n | cut -d ',' -f10 | tail -n1).\n"
       echo "Com um total de $(tail -n +2 2006-sample.csv | sort -t, -k14,14n | cut -d ',' -f14 | tail -n1) minutos de atraso."
       echo "****************************"
;;

-e5 | --Diverted)
       echo "****************************(ok)"
       echo "Contar quantos vôos precisaram ser redirecionados (Diverted)."
       echo -e "cat 2006-sample.csv | cut -d, -f24 | grep 1 | wc -l \n"
       cat 2006-sample.csv | cut -d, -f24 | grep 1 | wc -l
       echo "****************************"
;;

-e6 | --calc)
       echo "****************************(ok)"
       echo -e "Calcular o tempo de atraso total para a companhia Delta Air Lines (DL).\n"
       bash e6.sh 2006-sample.csv 
       echo "****************************"
;;

-e7 | --jfk)
       echo "****************************(ok)"
       echo -e "Mostrar o tempo total de atrasos para a decolagem (DepDelay) de vôos no aeroporto JFK, de Nova Iorque.\n"
       echo -e "sort -nk18 2006-sample.csv | grep 'JFK' | wc -l"
       echo -e "Número total de atrasos de vôos no aeroporto JFK:"
       sort -nk18 2006-sample.csv | grep 'JFK' | wc -l #(2198 JFK)
       #echo -e "\nawk -F\",\" '\$17==\"JFK\" {SUM+=\$16}END {print SUM}' 2006-sample.csv"
       echo -e "\nTempo total de atrasos para a decolagem (DepDelay) de vôos no aeroporto JFK, em minutos."
       #awk -F "," '$17=="JFK" {SUM+=$16}END {print SUM}' 2006-sample.csv 
       cat 2006-sample.csv | cut -d ',' -f16,17 | grep -w JFK | cut -d ',' -f1 | grep -v '-'| grep -v '^$' | paste -sd+ | bc 
       #cat 2006-sample.csv  |grep JFK |cut -d, -f16 |grep -v '-'| grep -v '^$' | paste -sd+ | bc
       echo "****************************"
;;

-e8 | --lax)
       echo "****************************(ok)"
       echo -e "Mostrar o tempo total de atrasos para pousos no Aeroporto Internacional de Los Angeles (LAX).\n"
       echo -e "sort -nk17 2006-sample.csv | grep 'LAX' | wc -l"
       echo -e "Número total de atrasos de vôos no aeroporto no Aeroporto Internacional de Los Angeles (LAX):"
       sort -nk17 2006-sample.csv | grep 'LAX' | wc -l #(4729 LAX)
       #echo -e "\nawk -F\",\" '\$17==\"LAX\" {SUM+=\$15}END {print SUM}' 2006-sample.csv"
       echo -e "Tempo total de atrasos para pousos no Aeroporto Internacional de Los Angeles (LAX), em minutos."
       cat 2006-sample.csv | cut -d ',' -f15,18 | grep -w LAX | cut -d ',' -f1 | grep -v '-'| grep -v '^$' | paste -sd+ | bc 
       #awk -F "," '$17=="LAX" {SUM+=$15}END {print SUM}' 2006-sample.csv 
       echo "****************************"
;;

-b1 | --bonus1)
       echo "****************************"
       echo "Listar qual companhia teve o maior tempo total de atrasos (atrasos somente na decolagem)."
       #bash b1.sh 2006-sample.csv 
       export A=9
       export B=9,16
       export C=2
       bash b1_b2.sh 2006-sample.csv 
       echo "A cia com a maior soma nos atrasos foi a $(sort -t, -k2 -n resposta3.csv | cut -d ',' -f1 | tail -n1)"
       echo "Com um total de $(sort -t, -k2 -n resposta3.csv | tail -n1 | cut -d ',' -f2) minutos."
       echo "****************************"
;;

-b2 | --bonus2)
       echo "****************************"
       echo "Listar qual aeroporto teve o maior tempo total de atrasos (atrasos somente na decolagem)."
       #bash b2.sh 2006-sample.csv
       export A=17
       export B=16,17
       export C=1
       bash b1_b2.sh 2006-sample.csv 
       echo "O aeroporto com maior atraso foi o $(sort -t, -k2 -n resposta3.csv | cut -d ',' -f1 | tail -n1)."
       echo "Com um total de $(sort -t, -k2 -n resposta3.csv | tail -n1 | cut -d ',' -f2) minutos."
       echo "****************************"
;;

*) 
  echo "****************************"
  echo "software FTAB v1.0"
  echo ""
  echo "Opção invalida"
  echo "Para maiores informações digite:"
  echo ""
  echo -e "./ftab.sh --h\n./ftab.sh  -help\n"
  echo -e "bash ftab.sh --h\nbash ftab.sh  -help"
  echo "****************************"
;;

esac



