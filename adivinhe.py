from random import randint
import platform
import os

resp = "s"
while resp == "s" or "S" or "Sim" or "sim":
    print('Bem vindo ao meu jogo em python :), você tem 10 tentativas! \n aproveite!! \n github.com/DaniiB0y')
    tentativas = 10
    numeros = int(input('Deseja randomizar entre quantos numeros? ~> '))
    numero_certo = randint(1, numeros)
    numero = 0 
    while tentativas > 1 and numero != numero_certo:
        numero = int(input('Acha que é qual numero? ~> '))
        tentativas -= 1
        if numero < numero_certo:
            print('É maior! só restam %s tentativas' % tentativas)
        elif numero > numero_certo:
            print('É menor! só restam %s tentativas' % tentativas)
        elif numero == numero_certo:
            print('Parabéns! você acertou com %s tentativas!' % tentativas)
            resp = input('Você deseja continuar? Digite s se sim! ~>')
            if platform.system() == 'Windows':
                os.system('cls')
            elif platform.system() == 'Linux':
                os.system('clear')
            else:
                os.system('clear')
            
