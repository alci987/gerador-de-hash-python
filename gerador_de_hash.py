import hashlib
import os

"""
OBS: No console do Pychame, o função os.system('cls') não está funcionando, apenas no terminal
se o texto for passado direto no método hashlib.md5, basta adicionr o b
Ex: hashlib.md5(b"texto")

Se for passado uma variável, deve-se usar a função encode
Ex: hashlib.md5(string.encode('utf-8'))
"""


def opcao1():
    resultado = hashlib.md5(string.encode('utf-8'))  # decodifica o hash e salva em resultado
    print('-' * 80)  # imprime os traços para separar a informação
    print()
    print('A Hash MD5 da frase é:', resultado.hexdigest())
    print()
    print('-' * 80)  # imprime os traços para separar a informação


def opcao2():
    resultado = hashlib.sha1(string.encode('utf-8'))  # decodifica o hash e salva em resultado
    print('-' * 80)  # imprime os traços para separar a informação
    print()
    print('A Hash SHA1 da frase é:', resultado.hexdigest())
    print()
    print('-' * 80)  # imprime os traços para separar a informação


def opcao3():
    resultado = hashlib.sha256(string.encode('utf-8'))  # decodifica o hash e salva em resultado
    print('-' * 80)  # imprime os traços para separar a informação
    print()
    print('A Hash SHA256 da frase é:', resultado.hexdigest())
    print()
    print('-' * 80)  # imprime os traços para separar a informação


def opcao4():
    resultado = hashlib.sha256(string.encode('utf-8'))  # decodifica o hash e salva em resultado
    print('-' * 80)  # imprime os traços para separar a informação
    print()
    print('A Hash SHA512 da frase é:', resultado.hexdigest())
    print()
    print('-' * 80)  # imprime os traços para separar a informação


def opcao5():
    resultado = hashlib.sha256(string.encode('utf-8'))  # decodifica o hash e salva em resultado
    print('-' * 80)  # imprime os traços para separar a informação
    print()
    print('MD5: ', hashlib.md5(string.encode('utf-8')).hexdigest())  # decodifica o hash e salva em resultado
    print('SHA1: ', hashlib.sha1(string.encode('utf-8')).hexdigest())  # decodifica o hash e salva em resultado
    print('SHA256: ', hashlib.sha256(string.encode('utf-8')).hexdigest())  # decodifica o hash e salva em resultado
    print('SHA512: ', hashlib.sha512(string.encode('utf-8')).hexdigest())  # decodifica o hash e salva em resultado
    print()
    print('-' * 80)  # imprime os traços para separar a informação


string = input('Digite o texto a ser encriptdo: ')

opcao = ''
while opcao != '6':
    print("""######### MENU - Escolha o tipo de hash #########
                    [1] - MD5
                    [2] - SHA1
                    [3] - SHA256
                    [4] - SHA512
                    [5] - Exbir todos os hash de uma vez
                    [6] - Sair""")
    opcao = input('>>>>>> Qual sua opção: ')
    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
        opcao1()

    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
        opcao2()

    elif opcao == '3':
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
        opcao3()

    elif opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
        opcao4()

    elif opcao == '5':
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
        opcao5()

    elif opcao == '6':
        print('Finalizando.....')

    else:
        print('Opçao incorreta. Tente novamente!!!')
        os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela
