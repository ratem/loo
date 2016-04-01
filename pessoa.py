from base import Base

class Pessoa(Base):
	coletivo = {}
	ultima_id = 0
	
	def __init__(self, nome, endereco):
		self.id = Base.inserir(self, Pessoa.coletivo, Pessoa.ultima_id)
		Pessoa.ultima_id = self.id
		self.nome = nome
		self.endereco = endereco

