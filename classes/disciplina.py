from base import Base

class Disciplina(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, nome, creditos, curso):
		if(curso.__class__.__name__ != 'Curso'): 
			raise TypeError('Deveria ser curso!')
		self.id = Disciplina.ultima_id = Base.inserir(self, Disciplina.coletivo, Disciplina.ultima_id)
		self.curso = curso
		curso.incluir_disciplina(self)
		self.nome = nome
		self.creditos = creditos
		self.desempenhos = {}

	def incluir_desempenho(self, desempenho):
		self.desempenhos[desempenho.aluno.id] = desempenho

