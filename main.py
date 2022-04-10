#!/usr/bin/python3
from sys import argv

from send_email import send
from create_email import create, attach_app
from set_data import data
from tools import get_mime_type

def help_menu():
    """ dic string """
    menu = """
    this is a help menu
    """
    print(menu)


def main(parametros):
    """ doc string """
    to = parametros['-to']
    subject = parametros['-subject']
    body = parametros['-body']
    print('criando email')
    msg = create(to, body, subject, 'plain')

    if '-attachs' in parametros:
        attachments = parametros['-attachs'].split(',')
        for item in attachments:
            mime_type, _ = get_mime_type(item)
            if mime_type == 'application':
                msg = attach_app(msg, item)
    print('email criado com sucesso')

    print('dando inicio ao envio do email')
    send(msg)

def config(parametros):
    """ doc string """
    email = parametros['-email']
    password = parametros['-password']
    server = parametros['-server']
    port = parametros['-port']

    data(email, password, server, port)

if __name__ == '__main__':
    # retira o nome do arquivo executado
    argv.pop(0)
    # o comando a ser executado
    command = argv.pop(0)
    # parametros do comando
    params = dict(zip(argv[::2], argv[1::2]))
    if command == 'send':
        main(params)
    elif command == 'setdata':
        config(params)
    else:
        help_menu()
