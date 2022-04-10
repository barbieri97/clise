# Command Line Interface to Send E-mails

O programa consistem em criar uma interface de lina de comando para enviar emails

A principio será desenvolvidos dois comandos:

`send`:

para enviar os emails

`setserver`

para setar sua conta no servidor de email

## Tecnologias a serem utilizadas

### SMTP

Esse programa utiliza o protocolo **SMTP** para transferência de emails e irá utilizar o servidor SMTP do google para enviar emails

para isso será utilizada a biblioteca **smtplib** nativa do python

### MIME

Os emails serão construidos no formato **MIME**

Para contruir esses emails será utilizada a biblioteca **email.mime** nativa do python

## Bibliotecas a serem criadas:

1. set_data.py

    Módulo para setar os dados que serão utilizados para conectar ao servidor.

2. create_email.py

    Módulo para constriur os emails no formato MIME.

3. send_email.py

    Módulo para enviar os emails craidos.

4. main.py

    Módulo para integrar as bibliotecas.


5. testes.py

    Módulo com os testes do programa

## Outros arquivos a serem criados

1. config.json

    Arquivo que armazenará os dados para realizar a conexão com o servidor SMTP.

## Atualizações a serem feitas

1. criar função para identificar o tipo de arquivo para adicionar os anexos (verificar o mimetypes)

2. criar o programa main que ira receber os comandos da linha de comando