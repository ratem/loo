from base import Base

class Disciplina(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, nome, creditos, curso):
		self.id = Disciplina.ultima_id = Base.inserir(self, Disciplina.coletivo, Disciplina.ultima_id)

