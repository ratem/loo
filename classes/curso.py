from base import Base

class Curso(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, nome):
		self.id = Curso.ultima_id = Base.inserir(self, Curso.coletivo, Curso.ultima_id)

