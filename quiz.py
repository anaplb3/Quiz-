from random import *
from bibQuiz import *
import time

mary = '\033[34m'+'QUIZ DA MARY'+'\033[0;0m'
sim = '\033[31m'+'❥'*100+'\033[0;0m'
print(sim.center(170))
print("\n")
print(mary.center(175))
print("\n")
print(sim.center(170))

apresentacao()

perguntas = ["Qual o líder da equipe dos Jovens Titãs? ", "Quantos integrantes tem os titãs? ", "Qual a cor do Mutano? ", "Qual o nome do amigo rosa do Bob Esponja? ", "Qual a cor do vestido da Mônica? ", "Qual a letra que o Cebolinha não sabe falar? ", "Do que o Cascão tem mais medo? ", "Qual o nome do irmão da Peppa Pig? ", "Qual o nome do dono do Scooby-Doo? ", "Qual a cor da roupa da Velma? ", "Qual é a cor dos Smurfs? ", "Jerry é o nome do rato, qual o nome do gato? ", "Qual o nome do restaurante em que o Bob Esponja trabalha? ", "O que a Cinderela perdeu na escada? ", "O que a madrasta da Branca de Neve usa pra envenená-la? ", "Qual o nome da Bela Adormecida? ", "Qual o nome da Pequena Sereia? ", "Qual o nome do macaco da Dora Aventureira? ", "O que faz o nariz do pinóquio crescer? ", "Qual o nome do vizinho do Pica Pau? "]
respostas = ["robin", "5", "verde", "patrick", "vermelho", "r", "água", "george", "salsicha", "laranja", "azul", "tom", "siri cascudo", "sapato", "maçã", "aurora", "ariel", "botas", "mentira", "leoncio"]
opcoes = [["Robin", "Ravena", "Mutano"],["5", "9", "3"], ["Laranja", "Azul", "Verde"], ["Patrick", "Lula Molusco", "Sandy"], ["Verde", "Vermelho", "Amarelo"], ["T", "H", "R"], ["Raios", "Água", "Cachorros"], ["George", "Peter", "João"], ["João", "Salsicha", "Bob"], ["Azul", "Rosa", "Laranja"], ["Cinza", "Rosa", "Azul"], ["Tim", "Tom", "José"], ["Balde de Lixo", "Siri Cascudo", "Novo Mar"], ["Colar", "Sapato", "Tênis"], ["Laranja", "Chocolate", "Maçã"], ["Isabela", "Aurora", "Jasmin"], ["Ariel", "Suzane", "Mulan"], ["Botas", "Monkey", "Bob"], ["Espirro", "Mentira", "Doces"], ["Leoncio", "Bingo", "Patúncio"]]
indice = 17
certas = 0
erradas = 0
vezes = randint(1,17)

for i in range(vezes):
	ind = randint(0,indice)
	
	print("\n")
	print(("{}".format('\033[37m'+perguntas[ind].center(160)+'\033[0;0m')))
	print("\n")
	
	resp = op(opcoes, ind)
	x = checandoResposta(ind, respostas, resp)
	
	if x == True:
		certas += 1
	else:
		erradas += 1
	
	indice -= 1
	del perguntas[ind]
	del respostas[ind]
	del opcoes[ind]

fim(certas, erradas)
