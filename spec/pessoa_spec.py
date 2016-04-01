import unittest
from should_dsl import should
from pessoa import Pessoa

class PessoaSpec(unittest.TestCase):
	def setUp(self):
		Pessoa.coletivo = {}
		Pessoa.ultima_id = 0
	
	def test_criar_pessoa(self):
		p = Pessoa('Fafendriades', 'Rua dos Bobos, 0')
		Pessoa.coletivo |should| include_keys(1)
		Pessoa.coletivo |should| include_values(p)
		p.nome |should| equal_to('Fafendriades')
		p.endereco |should| equal_to('Rua dos Bobos, 0')



