from base import Base

class Desempenho(Base):
	coletivo = {}
	ultima_id = 0

	def __init__(self, aluno, disciplina, nota, faltas):
		self.id = Desempenho.ultima_id = Base.inserir(self, Desempenho.coletivo, Desempenho.ultima_id)
		#solucao inicial, fazer verificacao de tipos
		self.aluno = aluno
		self.disciplina = disciplina
		#solucao inicial, idealmente notas e faltas deveriam ser lancadas fora do construtor
		self.nota = nota
		self.faltas = faltas

