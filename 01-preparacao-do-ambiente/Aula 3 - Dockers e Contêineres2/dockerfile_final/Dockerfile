#Imagem que serve como base
FROM node:latest

#Pessoa que criou a imagem
LABEL manteiner = "uflaniano"

#Especificando o local da imagem (.) Ponto é o diretorio atual (corrente)
COPY . /var/www

#Flag -w para WorkDir
WORKDIR /var/www 

#Comando para executar
RUN npm install

#Quando o container iniciar
ENTRYPOINT [ "npm", "start" ]

#definindo a porta
EXPOSE 3000