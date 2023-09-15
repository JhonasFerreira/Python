############### Blackjack Project #################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints ######################
# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this
# #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
from art import logo

def escolha_carta():
    """Retorna um carta aleatória do baralho"""
    cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    carta_aleatoria = random.choice(cartas)
    return carta_aleatoria
def calcule_pontuacao(cards):
    """Retorna a soma ou o Blackack -21 na soma,e fim de jogo- das cartas"""
    if 10 in cards and 11 in cards and len(cards) == 2:
        return 0
    # se tiver o 11(ace) no baralho e a soma for maior que 21 remova e adicione 1 no lugar
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#iniciado as variaveis para somar O resultado final da partida
empate=0
vitorias=0
perdeu=0
def compare(ptsJogador,ptsBot):
    """Compare a pontuação dos jogadores"""
#Iniciando globalmente as variaveis para reutilizar do escopo de bloco da funcao
    global vitorias
    global empate
    global perdeu
    if ptsJogador==ptsBot:
        empate+=1
        return "Draw 😒"
    elif ptsBot==0:
        perdeu+=1
        return "O Oponente tinha um Blackjack, Voce Perdeu 🤦‍"
    elif ptsJogador==0:
        vitorias+=1
        return "Voce Ganhou com um Blackjack"
    elif ptsJogador>21:
        perdeu+=1
        return "Voce estrapolou o limite,Voce Perdeu!!!!"
    elif ptsBot>21:
        vitorias+=1
        return "O oponente extrapolou,Voce Ganhou!!"
    elif ptsJogador>ptsBot:
        vitorias+=1
        return "Voce Ganhou😁👌"
    else:
        perdeu+=1
        return "Voce Perdeu 👌😵‍💫"
def jogar_jogo():
    print(logo)
    cartas_bot = []
    cartas_jogador = []
    fimDeJogo = False
    # adiciona 2 cartas iniciais ao barai kkk tapoha
    for i in range(2):
        nova_carta = escolha_carta()
        cartas_jogador.append(nova_carta)
        cartas_bot.append(nova_carta)
    while not fimDeJogo:
        ptsJogador = calcule_pontuacao(cartas_jogador)
        ptsBot = calcule_pontuacao(cartas_bot)

        print(f"Suas Cartas:{cartas_jogador} e Pontuação Geral:{ptsJogador}")
        print(f"Cartas do seu Oponente {cartas_bot[0]}")
        if ptsJogador == 0 or ptsBot == 0 or ptsJogador > 21:
            fimDeJogo = True
        else:
            puxar_carta = input("'S' para puxar uma Carta ou 'N' para passar: ").lower()
            if puxar_carta == "s":
                cartas_jogador.append(escolha_carta())
            else:
                fimDeJogo = True
    while ptsBot!=0 and ptsBot<17:
        cartas_bot.append(escolha_carta())
        ptsBot=calcule_pontuacao(cartas_bot)
    print(f" Seu baralho final:{cartas_jogador}, Pontução final: {ptsJogador}")
    print(f" baralho finao do Computador: {cartas_bot}, Pontuação final: {ptsBot}")
    print(compare(ptsJogador,ptsBot),"\n")

while input("Quer Jogar o jogo de BlackJack (S/N) : ").lower()=='s':
   jogar_jogo()
else:
    print(f"V {vitorias}, D {perdeu}, E{empate}")
    print("Espero que Tenha Gostado do jogo, Volte Sempre!!")