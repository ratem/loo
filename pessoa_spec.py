import unittest
from should_dsl import should
from pessoa import Pessoa

class PessoaSpec(unittest.TestCase):
	def setUp(self):
		Pessoa.coletivo = {}
		Pessoa.ultima_id = 0
		#Usar objetos "globais" tem a vantagem de economizar codigo e a desvantagem de 
		#diminuir o isolamento entre os testes e consequentemente a seguranca dos mesmos
		self.p = Pessoa('Fafendriades', 'Rua dos Bobos, 0')
	
	def test_criar_pessoa(self):
		Pessoa.coletivo |should| include_keys(1)
		Pessoa.coletivo |should| include_values(self.p)
		self.p.nome |should| equal_to('Fafendriades')
		self.p.endereco |should| equal_to('Rua dos Bobos, 0')

	def test_alterar_endereco(self):
		self.p.alterar_endereco('Rua dos Jecas, 1')
		self.p.endereco |should| equal_to('Rua dos Jecas, ')

#Alternativa para problemas de instalacao:
#Nao usar Makefile, acrescentar as linhas abaixo e chamar diretamente com o python
if __name__ == "__main__":
    unittest.main()
