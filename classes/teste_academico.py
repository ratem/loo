from curso import Curso
from aluno import Aluno
from disciplina import Disciplina
from desempenho import Desempenho

def testar():
	c = Curso('Info')
	a = Aluno('Joao','01/01/01')
	d = Disciplina('Loo', 4, c)
	e = Disciplina('ED', 4, c)
	f = Disciplina('TE', 4, c)
	a.matricular(c)
	d1 = Desempenho(a,d, 5,1)
	d2 = Desempenho(a,e, 6,2)
	d3 = Desempenho(a,f, 7,3)
	a.listar_desempenhos()

if __name__ == "__main__":
    testar()
