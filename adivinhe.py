# -*- coding: utf-8 -*-
from random import randint
p = input('Digite um numero!: ') #Palpite
babaca = input('Digite o numero de randomizaçoes!: ') #Randomizacoes
tentativas = 1 #Tentativas
numero = randint(1, babaca) #Numero certo
while p != numero and tentativas <= 10: #enquanto o palpite for diferente do numero e tentativas for menor que 10
	print "errou"
	print tentativas, " Tentativas! só restam", 10 - tentativas + 1
	p = input('Digite um numero!: ') #Renova o valor do numero
	tentativas += 1
	if p == numero:
		print "Acertou mizeravi!, Fim do jogo!", tentativas,"Tentivas!"
	elif p < numero:
		print "Digite um valor maior abiguinhu!"
	elif p > numero:
		print "Digite um valor menor abiguinhu!"
	else:
		print ""				