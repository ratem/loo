if __name__ == "__main__":
	#lista deve declarada antes
	numeros = []
	numeros.append(1)
	numeros.append(2)
	numeros.append(3)
	print numeros
	numeros.append("isso eh horrivel, mas eh possivel!")
	print numeros
	print numeros[0]
	del numeros[3]
	print numeros
	#dicionarios devem ser declarados antes
	coisas = {}
	coisas["Maria"] = ["couve", 22]
	coisas[1] = 5
	print coisas
	print coisas["Maria"]
	print coisas.keys()
	print coisas.values()
	print coisas.items()
	del coisas[1]
	print coisas
	coisas["Maria"][0] = "espinafre"
	print coisas["Maria"]
