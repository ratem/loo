from base import Base

class Pessoa(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, nome, data_nascimento):
		self.nome = nome
		self.data_nascimento = data_nascimento
		self.id = Pessoa.ultima_id = Base.inserir(self, Pessoa.coletivo, Pessoa.ultima_id)
