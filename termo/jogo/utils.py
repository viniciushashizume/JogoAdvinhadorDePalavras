import random

def gerarFeedback(palavra, tentativa):
    resultado = []
    for i, letra in enumerate(tentativa):
        if letra == palavra[i]:
            resultado.append({"letra": letra, "cor": "green"})
        elif letra in palavra:
            resultado.append({"letra": letra, "cor": "yellow"})
        else:
            resultado.append({"letra": letra, "cor": "gray"})
    return resultado

def obterPalavraAleatoria():
    palavras = ["porta", "janta", "calvo"]
    return random.choice(palavras)