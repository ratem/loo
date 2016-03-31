from base import Base

class Veiculo:
	coletivo = {}
	ultima_id = 0

	def __init__(self, chassi):
		self.chassi = chassi
		Veiculo.ultima_id = Base.inserir(self, Veiculo.coletivo, Veiculo.ultima_id)
		self.id = Veiculo.ultima_id
