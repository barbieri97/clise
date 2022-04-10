""" Módulo de testes """

import unittest
import os
from set_data import data
from create_email import create, attach_app, MIMEApplication, MIMEMultipart, MIMEText

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
        expected_msg['From'] = 'barbieride507@gmail.com'
        expected_msg['To'] = 'andrepb636@gmail.com'
        expected_msg['Subject'] = 'ola sou um email de teste'
        msg_create = create('andrepb636@gmail.com', 'ola tudo bem', 'ola sou um email de teste',
                            email_from='barbieride507@gmail.com', boundary_type='12345')
        self.assertEqual(str(msg_create), str(expected_msg))

    def teste_attach_app(self):
        with open('project.md', 'rb') as file:
            app = file.read()
        msg_expected = create('andrepb636@gmail.com', 'ola tudo bem', 'ola sou um email de teste',
                                 boundary_type='12345')
        msg_create = create('andrepb636@gmail.com', 'ola tudo bem', 'ola sou um email de teste',
                                 boundary_type='12345')
        msg_expected.attach(MIMEApplication(app, 'octet-stream'))
        self.assertEqual(str(msg_expected), str(attach_app(msg_create, ['project.md'])))


if __name__ == '__main__':
    unittest.main()
