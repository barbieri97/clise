""" Módulo com ferramentas uteis para o software """

from re import fullmatch
from mimetypes import guess_type

def is_path(data: str) -> bool:
    """ essa função retorna True se a string passada corresponder a um path """
    pattern1 = r'[a-zA-Z0-9-_]+\.[a-z0-9]+|[\.\~]*/[\w\W]*/[\w\W]*\.[a-z0-9]+'
    result = fullmatch(pattern1, data)
    if result:
        return True
    return False

def file_name(data: str):
    """ Essa função recebe uma string e confere se é um path
    caso verdadeiro retorna no nome do arquivo"""
    if is_path(data):
        file = data.split('/')
        return file[-1]
    return None

def get_mime_type(path):
    """ essa função devolve o type e subtype do mime """
    type_mime, _ = guess_type(path)
    type_mime, subtype = type_mime.split('/')
    return type_mime, subtype
