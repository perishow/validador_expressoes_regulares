#pega uma expressão regular definida pelo usuário e compara com uma palavra também fornecida pelo usuário
# 1 - compilar a expressão fornecida
# 2 - coletar palavra de teste
# 3 - compara, indica se é válida ou não
# 4 - recomeça (talvez a partir do ponto 2)

import re

def configurar_expressao(expressao):
    linguagem = re.compile(expressao)
    return linguagem

def checagem(linguagem, palavra):
    if linguagem.match(palavra):
        print("🐸válida🐸")
        return True
    else:
        print("❌inválida❌")
        return False

def execution_loop():
    linguagem = configurar_expressao(input("digite uma expressão:"))

    while True:
        palavra = input("digite uma palavra:")
        if palavra =='quit':
            break
        elif palavra == 'select':
            linguagem = configurar_expressao(input("digite uma expressão:"))
        else:    
            checagem(linguagem,palavra)

if __name__ == "__main__":
    execution_loop()
