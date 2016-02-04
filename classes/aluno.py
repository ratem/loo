from base import Base
from pessoa import Pessoa

class Aluno(Pessoa):
	coletivo = {}
	ultima_id = 0

	def gerar_matricula(self):
		return 'A' + str(self.id)

	def __init__(self, nome, data_nascimento):
		Pessoa.__init__(self, nome, data_nascimento)
		self.id = Aluno.ultima_id = Base.inserir(self, Aluno.coletivo, Aluno.ultima_id)
		self.matricula = self.gerar_matricula()
