import hashlib

"""
hashlib consiste em um módulo que implementa muitos algoritmos de hash seguro 
e de resumo de mensagem chamados. Também pode incluir algoritmos adicionais disponíveis, 
dependendo da biblioteca OpenSSL que o Python usa em sua plataforma.
"""

string = input('Digite o texto a ser encriptdo: ')  # obtem a frase que o usuário quer encriptar

"""
se o texto for passado direto no método hashlib, basta adicionr o b
Ex: hashlib.md5(b"texto")

Se for passado uma variável, deve-se usar a função encode
Ex: hashlib.md5(string.encode('utf-8'))
"""
opcao = 0
while opcao != 6:
    print("""######### MENU - Escolha o tipo de hash #########
                    [1] - MD5
                    [2] - SHA1
                    [3] - SHA256
                    [4] - SHA512
                    [5] - Exbir todos os hash de uma vez
                    [6] - Sair""")
    opcao = int(input('>>>>>> Qual sua opção: '))
    if opcao == 1:
        resultado = hashlib.md5(string.encode('utf-8'))
        print('A Hash MD5 da frase é:', resultado.hexdigest())
    elif opcao == 2:
        resultado = hashlib.sha1(string.encode('utf-8'))
        print('A Hash SHA1 da frase é:', resultado.hexdigest())
    elif opcao == 3:
        resultado = hashlib.sha256(string.encode('utf-8'))
        print('A Hash SHA256 da frase é:', resultado.hexdigest())
    elif opcao == 4:
        resultado = hashlib.sha512(string.encode('utf-8'))
        print('A Hash SHA512 da frase é:', resultado.hexdigest())
    elif opcao == 5:

        print('MD5: ', hashlib.md5(string.encode('utf-8')).hexdigest())
        print('SHA1: ', hashlib.sha1(string.encode('utf-8')).hexdigest())
        print('SHA256: ', hashlib.sha256(string.encode('utf-8')).hexdigest())
        print('SHA512: ', hashlib.sha512(string.encode('utf-8')).hexdigest())
    elif opcao == 6:
        print('Finalizando.....')
    else:
        print('Opçao incorreta. Tente novamente!!!')
    print('=-=' * 10)
