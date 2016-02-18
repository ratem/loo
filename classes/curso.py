from base import Base

class Curso(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, nome):
		self.id = Curso.ultima_id = Base.inserir(self, Curso.coletivo, Curso.ultima_id)
		self.alunos = {}

	def matricular_aluno(self, aluno):
		if(aluno.__class__.__name__ != 'Aluno'): #Nao emprega isinstance para nao importar Aluno, o que criaria referencia cruzada
			raise TypeError('Deveria ser aluno!')		
		self.alunos[aluno.id] = aluno

