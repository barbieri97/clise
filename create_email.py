""" Esse módulo cria o email a ser enviado """

from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import sys

from data_config import EMAIL
from tools import is_path, file_name, get_mime_type


def create(email_to: str, body: str, subject: str, subtype: str='plain',
           boundary_type: str=False) -> MIMEMultipart:
    """
    Essa função cria o email a ser enviado
    :`param to`: str - enderço de email pra qum sera enviado
    :param body: str - texto que estará no corpo do email
    :param email: str - enderço de email de quem esta enviado
    :param body_arq: bool - se o texto do corpo de email será lido de um arquivo
    :return: MIMEMultipart - objeto MIMEmultipart para ser enviado como email
    """
    # Implementado para poder realizar os testes da função
    if boundary_type:
        msg = MIMEMultipart(boundary=boundary_type)
    else:
        msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = email_to
    msg['Subject'] = subject

    if is_path(body):
        with open(body, 'r', encoding='utf-8') as file_body:
            texto = file_body.read()
        _, subtype = get_mime_type(body)
    else:
        texto = body

    msg.attach(MIMEText(texto, subtype))
    print('Corpo da mensagem criado com sucesso')

    return msg

def attach_app(msg_app: MIMEMultipart, path_arq: str) -> MIMEMultipart:
    """ anexa arquivos binarios ao email """
    try:
        with open(path_arq, 'rb') as file_attachment:
            app = file_attachment.read()
        atta = MIMEApplication(app, 'octet-stream')
        atta['Content-Disposition'] = f"attachment; filename= {file_name(path_arq)}"
        msg_app.attach(atta)
        print(f'arquivo {file_name(path_arq)} anexado!')
    except FileNotFoundError:
        print(f"\nNão foi possivél encontrar o arquivo {path_arq}")
        sys.exit()
    return msg_app

