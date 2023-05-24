#importando bibliotecas para randomizar dados,e tempo de disposição do output.
import random
from time import sleep
#modulo contendo a lista de representação grafica usando o padrão ASCII,para representar o "Enforcado".
from forcaImgs import img_forca
#função para dar uma dica referente a palavra secreta usada na forca, e será reutilizada no loop.
def palavra_selec(palavra_secreta):
    if palavra_secreta=="osimandias":
        print("Dica: É considerado o faráo egípcio mais prestigiado")
    elif palavra_secreta=="corinthians":
        print("Dica: É um time de Futebol")
    else:
        print("Dica: É um reverente Dramaturgo da lingua inglesa")
#Função para caso o usuario queira jogar novamente.
def continuar_jogando():
    if fim_de_jogo==True:
        continuar=input("Quer continuar jogando?S ou N: ").lower()
        if continuar=="s":
            return True
        else:
            return False
#Engatilhando o primeiro loop.
continuar=True
print("Bem vindo a o Jogo Da Forca!!")
sleep(0.8)
print("Regras:Escolha uma letra que condiz com a palavra secreta.Mas caso erre, perderá uma vida :(")
sleep(0.8)
#Usando o loop com a condição Continuar caso o usuario queira continuar jogando e assim redefinindo as variaveis.
while continuar:
#variavel para iniciar segundo loop.
    fim_de_jogo=False
#Lista com as palavras secretas.
    palavras=["osimandias","corinthians","shakespeare"]
#aleatorizando a palavra secreta usando a função Random.Choice() usado em Listas.
    palavra_secreta = random.choice(palavras)
#inicializando palavra que ira conter o caracter "-" e será usada a ultima instancia da palavra secreta.
    palavras_final = []
    for i in palavra_secreta:
        palavras_final += "-"
#chances que o usuario ira ter.
    chances = 6
    palavra_selec(palavra_secreta)
#O segundo loop será desengatilhado caso o usuario perca ou ganhe no jogo.
    while not fim_de_jogo:

        adivinhe=input("Adivinhe a letra: ").lower()
#Expressão condicional usada para caso usuario já tenha acertado a letra e a tenha digitado novamente.
        if adivinhe in palavras_final:
            print(f"A letra '{adivinhe}' a foi digitado")

        for posicao in range(len(palavra_secreta)):
             letra = palavra_secreta[posicao]
             if letra == adivinhe:
                 palavras_final[posicao] = letra
#usando a expressão IF para caso o usuario não acerte, perca sua contagem de chances.
        if adivinhe not in palavra_secreta:
             chances-=1
             print(f"Voce tem {chances} chances")
#caso a contagem de chaces chegue a zero encerre o segundo loop.
        if chances==0:
            print("Você Perdeu :( ")
            fim_de_jogo=True
#concatenando e tipificando a palavra secreta numa string.
        print(f"{' '.join(palavras_final)}")
#caso não tenha mais espaços em branco o usuario ganhou o jogo.
        if "-" not in palavras_final:
             print("Parabéns voce ganhou!!!!")
             fim_de_jogo=True

        print(img_forca[chances])
#utilizando a função para questionar se o usuario queria continuar jogando.
    continuar=continuar_jogando()

