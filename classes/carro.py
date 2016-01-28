from veiculo import Veiculo

class Carro(Veiculo):
	def __init__(self, rodas, fabricante):
		Veiculo.__init__(self, rodas)	#chamada explicita ao construtor da super classe
		self.fabricante = fabricante
		self.acessorios = []

	def revisar(self, data_revisao):
		self.revisao = data_revisao

	def instalar_acessorio(self, novo_acessorio):
		self.acessorios.append(novo_acessorio)
