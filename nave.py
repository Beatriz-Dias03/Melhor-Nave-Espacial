#definir as váriavéis

combustivel = 100
tribulantes = []

#definir funções

def viajar():
    #aqui fica o código
    global combustivel # avisa a função que vamos modificar um variavel externa
    if combustivel>=30:
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você não possui combustível suficiente para viajar. Abasteça!!")
    

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! 🛸")

def status_nave():
    #mostre a quantidade de combustível e os tripulantes
    print("\n-------------🧑‍🚀STATUS DA NAVE🧑‍🚀-------------")
    print(f"\nAtualmente, temos {combustivel} litros no tanque!")
    print(f"\nNossa tripulação é composta por: {tribulantes}\n")
    print("----------------------------------------\n")

def registrar_Tripulantes():
    novotripulante = input("qual é o nome do novo tripulante?")
    tribulantes.append(novotripulante)
    print("Novo tripulante inserido com sucesso!🚀")

#criar um menu
print("Bem vindo ao menu interativo da nave. Por favor, selecione uma opçâo:")
while True:
    print("\n 1- Mostrar status da nave 💻 | 2- Viajar 🚀 | 3- Abastecer ⛽ | 4- Novo tribulante 🧑‍🚀 | 5- Sair ❌")
    opção = input("Escolha: ")
    
    if opção == "1":
        status_nave()
    elif opção == "2":
        viajar()
    elif opção == "3":
     abastecer()
    elif opção == "4":
        registrar_Tripulantes()
    else:
        print("Viagem encerrada!")
        break


# viajar()
# viajar()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave() 