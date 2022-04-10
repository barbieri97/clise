""" Esse módulo é responsável por fazer a conexão com o servidor e enviar o email """

from email.mime.multipart import MIMEMultipart

from smtplib import SMTP

from data_config import EMAIL, PASSWORD, PORT, SERVER



def send(msg: MIMEMultipart):
    """
    Essa função é responsável por fazer a conexão com o servidor smtp e enviar as o email
    :param msg: MIMEMultipart - Email no formato MIME a ser enviado
    os demais variaveis para fazer a conexão é importado do módulo data_config
    """
    print(f'Conectando ao servidor SMTP {SERVER}, na porta {PORT}')
    server = SMTP(SERVER, PORT)
    print('Criptografando a conexão com tls')
    server.starttls()
    print(f'fazendo o login no servidor com o email {EMAIL}')
    server.login(EMAIL, PASSWORD)
    print(f"enviado a mensagem {msg['Subject']} para {msg['To']}")
    server.send_message(msg)
    print('Mensagem enviada!')
    print('desconectando do servidor')
    server.quit()
