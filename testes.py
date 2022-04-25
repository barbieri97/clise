""" Módulo de testes """

import unittest
import os
from set_data import data
from create_email import create, attach_app, MIMEApplication, MIMEMultipart, MIMEText
from tools import is_path, get_mime_type, file_name

class TestSetData(unittest.TestCase):
    """ class para testar as funções do módulo set_data """
    def teste_func_data(self):
        """ Testa se a função data está criando o json como esperado  """
        data('andrepb636@gmail.com', '123', 'smtp.gmail.com', '293', name_arq='testeconfig.json')
        json_expected = """{"email": "andrepb636@gmail.com", "password": "123", "server": "smtp.gmail.com", "port": "293"}"""
        with open('testeconfig.json', 'r', encoding='utf-8') as file:
            json_file = file.read()
        os.remove('testeconfig.json')
        self.assertEqual(json_file, json_expected)

class TestCreateEMail(unittest.TestCase):
    """ classe para realizar os testes do módulo create_email """
    def teste_create(self):
        """ testa se a função create cria um objeto MIMEMutipart sem anexos"""
        expected_msg = MIMEMultipart(boundary='12345')
        expected_msg.attach(MIMEText('ola tudo bem'))
        expected_msg['From'] = 'andrepb636@gmail.com'
        expected_msg['To'] = 'barbieride507@gmail.com'
        expected_msg['Subject'] = 'ola sou um email de teste'
        msg_create = create('barbieride507@gmail.com', 'ola tudo bem', 'ola sou um email de teste',
        'plain', boundary_type='12345')
        self.assertEqual(str(msg_create), str(expected_msg))

    def teste_attach_app(self):
        """ doc string """
        self.maxDiff = None
        with open('config.json', 'rb') as file:
            app = file.read()
        msg_expected = create('andrepb636@gmail.com', 'ola tudo bem', 'ola sou um email de teste', 
        'plain', boundary_type='12345')
        msg_create = create('andrepb636@gmail.com', 'ola tudo bem', 'ola sou um email de teste', 
        'plain', boundary_type='12345')
        atta = MIMEApplication(app, 'json')
        atta['Content-Disposition'] = "attachment; filename= config.json"
        msg_expected.attach(atta)
        self.assertEqual(str(msg_expected), str(attach_app(msg_create, 'config.json')))

class TestTools(unittest.TestCase):
    """ classe para testar as funções do modulo tools """
    def teste_is_path_com_path(self):
        path = '/path/to/file.extension'
        self.assertEqual(is_path(path), True)
    def teste_is_path_sem_path(self):
        file = 'filename.extension'
        self.assertEqual(is_path(file), True)
    def teste_is_path_com_str(self):
        file = 'esse é o nome do arquivo filename.extension'
        self.assertEqual(is_path(file), False)
    def teste_file_name_just_file(self):
        file = 'file.name'
        self.assertEqual(file_name(file), file)
    def teste_file_name_path(self):
        file = '/path/to/file.name' 
        self.assertEqual(file_name(file), 'file.name')
    def teste_get_mime_type_plain(self):
        file = 'file.txt'
        self.assertEqual(get_mime_type(file), ('text', 'plain'))
    def teste_get_mime_type_html(self):
        file = 'file.html'
        self.assertEqual(get_mime_type(file), ('text', 'html'))
    def teste_get_mime_type_pdf(self):
        file = 'file.pdf'
        self.assertEqual(get_mime_type(file), ('application', 'pdf'))
    def teste_get_mime_type_json(self):
        file = 'file.json'
        self.assertEqual(get_mime_type(file), ('application', 'json'))


if __name__ == '__main__':
    unittest.main()
