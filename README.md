# gerador-de-hash-python
Gerador básico de hashs em python.

A nova versão foi refatorada com o uso de funções para melhorar a leitura do código, bem como
foram feitas melhorias para na tela.

OBS: No console do Pychame, o função os.system('cls') não está funcionando, apenas no terminal
se o texto for passado direto no método hashlib.md5, basta adicionr o b
Ex: hashlib.md5(b"texto")

Se for passado uma variável, deve-se usar a função encode
Ex: hashlib.md5(string.encode('utf-8'))
