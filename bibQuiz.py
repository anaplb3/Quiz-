import time
def checandoResposta(ind, respostas, resp):
	 if resp == respostas[ind]:
	 	return True
	 else:
	 	return False

def apresentacao():
	lista = ["Bem vinda Mary!", "Eu sou a Jasmine, e estou aqui pra jogar um quiz com você.", "Então, está pronta?", "Vamos começar!"]
	print("\n")
	for i in lista:
		print(i.center(160))
		print("\n")
		time.sleep(1)

def perguntas(perguntas, indice):
	ind = randint(0,indice)
	indice -= 1
	return perguntas[ind]

def op(opcoes, ind):
	quest = '\033[37m'+'❀ Sua resposta: ❀ '+'\033[0;0m'
	for i in opcoes[ind]:
		print("                                ", '\033[37m'+'❀'+'\033[0;0m','\033[34m'+i+'\033[0;0m','\033[37m'+'❀'+'\033[0;0m', "   ", end="")
	print("\n")
	res = str.lower(input("                                                                {} ".format(quest)))
	return res

def fim(certas, erradas):
	listt = ["Opa, o jogo acabou!", "Você acertou {} perguntas :)".format(certas), "E errou {} :/".format(erradas), "Foi muito bom jogar com você, Mary :D", "Mais tarde você volta, ok? ", "Tchaaaaaaaaaaaaaaaaaaaaau!!"]
	print("\n")
	for i in listt:
		print("                                                                  ",'\033[34m'+i+'\033[0;0m')
		print("\n")
		time.sleep(1)