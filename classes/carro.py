class Carro:
	def __init__(self, fabricante):
		self.fabricante = fabricante
		self.acessorios = []

	def revisar(self, data_revisao):
		self.revisao = data_revisao

	def instalar_acessorio(self, novo_acessorio):
		self.acessorios.append(novo_acessorio)
