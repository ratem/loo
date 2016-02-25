from base import Base
from pessoa import Pessoa
from curso import Curso

class Aluno(Pessoa):
	coletivo = {}
	ultima_id = 0

	def gerar_matricula(self):
		return 'A' + str(self.id)

	def __init__(self, nome, data_nascimento):
		Pessoa.__init__(self, nome, data_nascimento)
		self.id = Aluno.ultima_id = Base.inserir(self, Aluno.coletivo, Aluno.ultima_id)

	def matricular(self, curso):
		self.matricula = self.gerar_matricula()
		if(not isinstance(curso, Curso)):
			raise TypeError('Deveria ser curso!')		
		self.curso = curso
		curso.matricular_aluno(self)
		self.desempenhos = {}

	def incluir_desempenho(self, desempenho):
		self.desempenhos[desempenho.disciplina.id] = desempenho
