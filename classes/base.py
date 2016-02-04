class Base:
	@classmethod
	def inserir(cls, objeto, coletivo, ultima_id):
		ultima_id = ultima_id + 1
		coletivo[ultima_id] = objeto
		return ultima_id

	@classmethod
	def remover(cls, objeto, coletivo):
		try:
			del coletivo[objeto.id]
		except KeyError:
			print 'Chave nao encontrada'


