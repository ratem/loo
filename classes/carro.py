from veiculo import Veiculo

class Carro(Veiculo):
	rodas = 4

	@classmethod
	def lista_rodas(cls):
		print cls.rodas

	def __init__(self, chassi, fabricante):
		Veiculo.__init__(self, chassi)	#chamada explicita ao construtor da super classe
		self.fabricante = fabricante
		self.acessorios = []

	def revisar(self, data_revisao):
		self.revisao = data_revisao

	def instalar_acessorio(self, novo_acessorio):
		self.acessorios.append(novo_acessorio)
