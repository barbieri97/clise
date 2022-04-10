""" Nesse modulo será criado o arquivo de configuração do programa """
from json import dumps

def data(email: str, password: str, server: str, port: str, name_arq: str='config.json') -> None:
    """
    Essa função recebe os dados essencial para realizar a conexão com o servidor SMTP
    e cria um arquivo json que será consultado por outra biblioteca para realizar a conexão
    :param email: str - email ao qual será conectado
    :param password: str - senha da conta
    :param server: str - dominio do servidor a ser conectado
    :param port: str - porta do servidor para conexão SMTP
    """
    # cria o objto python que será transformado para json
    datas =  {
        'email': email,
        'password': password,
        'server': server,
        'port': port
    }
    # Transforma o objeto python em json
    json_data = dumps(datas)

    # escreve o objeto python no arquivo json
    with open(name_arq, 'w', encoding='utf-8') as file:
        file.write(json_data)
