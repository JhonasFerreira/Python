from time import sleep
from art import logo,vs
from dados import data
import random


def acertou_chute(advinhe, contagem1, contagem2):
    """Adivinhe qual pessoa possui mais seguidores,sempre que o usuario acertar a função ira retorar Verdadeira"""
    if contagem1>contagem2:
        return advinhe=='a'
    else:
        return advinhe=="b"


def jogo():
    continuar=True
    pontuacao=0
    print(logo)
    conta2= random.choice(data)
    while continuar:
        conta1= conta2
        conta2=random.choice(data)

        while conta1==conta2:
            conta2=random.choice(data)

        print(f"Compare A:{conta1['name']} a {conta1['description']} from {conta1['country']}")
        print(vs)
        print(f"Contra B: {conta2['name']} a {conta2['description']} from {conta2['country']}")

        contagem1=conta1['follower_count']
        contagem2=conta2['follower_count']
        advinhe = input("Escolha qual Entidade possui mais seguidores(A/B): ").lower()
        resp_correta=acertou_chute(advinhe, contagem1, contagem2)
        if resp_correta:

            pontuacao+=1
            print(f"Voce Acertou!, Pontuação Atual: {pontuacao}")
        else:
            sleep(0.5)
            print(f"Voce Errou! Pontuação Final:{pontuacao}")
            continuar=False
        print(f" {conta1['name']} {contagem1},{conta2['name']} {contagem2}")
jogo()

while input("Quer Continuar Jogando?: ")=='s':
    jogo()
else:
    print("Espero que tenha se Divertido!!!")

