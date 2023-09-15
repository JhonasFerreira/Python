MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
lucro=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def tem_recursos(ingredientes):
    """Verifica se a quantidade atual de recursos e suficiente.
    True se possui e False caso nao possua recursos na maquina"""
    for item in ingredientes:
       if ingredientes[item]>=resources[item]:
            print(f"Desculpe,voce não possui recursos suficientes de {item}")
            return False
    return True

def total_moedas():
    """Retorna o valor total de moedas inseridas."""
    print("Insira moedas.")
    total =  int(input("quantos Quartes?(0.25): ")) * 0.25
    total += int(input("quantos Dimes?(0.10): ")) * 0.10
    total += int(input("quantos Nickels?(0.05): ")) * 0.05
    total += int(input("quantos Pennies?(0.01): ")) * 0.01
    return total

def transacao_sucesso(valor_recebido,valor_bebida):
    """Retorna True quando o pagamento for bem sucedido e Falso quando nao possuir Valores suficientes"""
    if valor_recebido>=valor_bebida:
        change = round(valor_recebido-valor_bebida,2)
        print(f"Mudança no Saldo:{change}")
        global lucro
        lucro+=valor_bebida
        return True
    else:
        print("Saldo insuficiente,Dinheiro retornado.")


def fazer_cafe(nomeBebida,ingredientes_pedido):
    """Reduzir recursos apartir do tipo de Drink"""
    for item in ingredientes_pedido:
        resources[item]-=ingredientes_pedido[item]
    print(f"Aqui está seu {nomeBebida} ☕")

water=resources["water"]
milk=resources["milk"]
coffee=resources["coffee"]
ligado=True
while ligado:
    opcao=input("What you would like?(cappuccino,latte,espresso):")
    if opcao=="off":
        ligado=False
    elif opcao=="report":
        print(f"Agua: {resources['water']}")
        print(f"Leite: {resources['milk']}")
        print(f"Cafe: {resources['coffee']}")
        print(f"Dinheiro: {lucro}")
    else:
        bebida=MENU[opcao]
        if tem_recursos(bebida["ingredients"]):
            pagamento=total_moedas()
            if transacao_sucesso(pagamento,bebida["cost"]):
                fazer_cafe(opcao,bebida["ingredients"])