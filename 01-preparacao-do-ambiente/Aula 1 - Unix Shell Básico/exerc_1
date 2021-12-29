#!/bin/bash

#echo $SHELL
#echo $CLEAR
#ls -l executavel.sh

#- n classifica um arquivo com dados numericos
# -k classifica uma determinada coluna

echo "Clear" > Respostas.txt
echo "#####################################################" >> Respostas.txt
echo 'cat echo.txt | tail -n+2 >>  Respostas.txt'  >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1a). Exibir o conteúdo de echo.txt sem a primeira linha de cabeçalho ' >> Respostas.txt
echo " - " >> Respostas.txt
cat echo.txt | tail -n+2 >>  Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "cat echo.txt | tail -n+2 | sort" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1b) Exibir o conteúdo de echo.txt classificado pelo nome (não exibir a primeira linha).' >> Respostas.txt
echo " - " >> Respostas.txt
cat echo.txt | tail -n+2 | sort >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "grep 'John' echo.txt" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1c) Exibir apenas linhas que contenham (John)'  >> Respostas.txt
echo " - " >> Respostas.txt
grep 'John' echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "grep -v 'John' echo.txt" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1d) Exibir apenas linhas que não contenham (John)'  >> Respostas.txt
echo " - " >> Respostas.txt
grep -v 'John' echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "grep '^J' echo.txt | grep -wE '\w{4}'" >> Respostas.txt
echo " - "  >> Respostas.txt
echo '(1e) Exibir apenas linhas que contenham palavras de 4 letras começando com (j)'  >> Respostas.txt
echo " - " >> Respostas.txt
grep '^J' echo.txt | grep -wE '\w{4}' >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "sort -nk4 echo.txt" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1f) Ordenar as linhas pela idade'  >> Respostas.txt
echo " - " >> Respostas.txt
sort -nk4 echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "sort -nk4 echo.txt | sed -n -e '2p;$p'" >> Respostas.txt
echo " - "  >> Respostas.txt
echo '(1g) Descobrir a pessoa mais velha e mais jovem no dataset'  >> Respostas.txt
echo " - " >> Respostas.txt
sort -nk4 echo.txt | sed -n -e '2p;$p' >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "cut -d ',' -f6 echo.txt" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1h) Listar as cidades presentes no dataset'  >> Respostas.txt
echo " - " >> Respostas.txt
cut -d ',' -f6 echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
echo "sort -nk4 echo.txt | grep 'Nova Iorque'  | tail -n-1" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(1i) Encontrar a pessoa mais velha que mora em Nova Iorque'  >> Respostas.txt
echo " - " >> Respostas.txt
sort -nk4 echo.txt |grep 'Nova Iorque'|tail -n-1 >> Respostas.txt
echo "#####################################################" >> Respostas.txt
#echo "cat echo.txt |wc -l"  >> Respostas.txt
echo "wc -l echo.txt"  >> Respostas.txt
echo " - " >> Respostas.txt
echo '(2a) Quantidade de linhas do arquivo (echo.txt)'  >> Respostas.txt
echo " - " >> Respostas.txt
#cat echo.txt | wc -l  >> Respostas.txt
wc -l echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
#echo "cat echo.txt |wc -w"  >> Respostas.txt
echo "wc -w  echo.txt" >> Respostas.txt
echo " - " >> Respostas.txt
echo '(2b) Quantidade de palavras' >> Respostas.txt
echo " - " >> Respostas.txt
#cat echo.txt | wc -w  >> Respostas.txt
wc -w echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt
#echo "cat  echo.txt | wc -m" >> Respostas.txt
echo "wc -m  echo.txt"  >>  Respostas.txt
echo " - " >> Respostas.txt
echo '(2c) Quantidade de Bytes'  >> Respostas.txt
echo " - " >> Respostas.txt
#cat echo.txt | wc -m  >> Respostas.txt
wc -m echo.txt >> Respostas.txt
echo "#####################################################" >> Respostas.txt

#(3a) O diretorio corrente (atual)
#(3b) Seu nome completo e sua idade
#(3c) Momento de execução do arquivo
#(3d) Grave uma frase que você acredita ser importante (rs)

echo " " > Log.txt
echo "3. Crie um script de log que apresente" >> Log.txt
echo "(3a) O diretório corrente (atual)" >> Log.txt
echo "(3b) Seu nome completo e sua idade" >> Log.txt
echo "(3c) Momento de execução do arquivo" >> Log.txt
echo "(3d) Grave uma frase que você acredita ser importante (rs)" >> Log.txt
echo " - " >> Log.txt

hora_sistema='%d/%m/%y_(%H:%M:%S)'
PWD=`pwd` #acento miseravel 
nome='Luiz Carlos Brandão Junior'
idade='42'
frase='Programar não é dificil, ela só não é fácil, mas dificil né não!'

for (( counter=10; counter>0; counter-- ))
do
echo "$PWD | $nome | $idade | $(date +$hora_sistema) | $frase" >>  Log.txt
done
printf "\n"