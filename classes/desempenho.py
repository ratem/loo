from base import Base

class Desempenho(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, aluno, disciplina, nota, faltas):
		if(aluno.__class__.__name__ != 'Aluno'): 
			raise TypeError('Deveria ser aluno!')
		if(disciplina.__class__.__name__ != 'Disciplina'): 
			raise TypeError('Deveria ser disciplina!')
		self.id = Desempenho.ultima_id = Base.inserir(self, Desempenho.coletivo, Desempenho.ultima_id)
		self.aluno = aluno
		self.disciplina = disciplina
		aluno.incluir_desempenho(self)
		disciplina.incluir_desempenho(self)
		self.nota = nota
		self.faltas = faltas

