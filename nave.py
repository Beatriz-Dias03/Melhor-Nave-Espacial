#definir as váriavéis

combustivel = 100
tripulantes = []

#definir funções

def viajar():
    #aqui fica o código
    global combustivel # avisa a função que vamos modificar um variavel externa
    print("----------------------------------------\n")
    if combustivel>=30 and tripulantes != []:
        combustivel = combustivel - 30
        print("A nave viajou")

    elif tripulantes == []:
        print("Você não possui tribulantes! Como quer viajar assim? Adicione alguém!")
    
    else:
        print("Você não possui combustível suficiente para viajar. Abasteça!!")

    travarMenu()
    print("----------------------------------------\n")

def abastecer():
    print("----------------------------------------\n")
    global combustivel
    combustivel = 100
    print("Tanque cheio! 🛸")
    travarMenu()
    print("----------------------------------------\n")

def status_nave():
    #mostre a quantidade de combustível e os tripulantes
    print("\n-------------🧑‍🚀STATUS DA NAVE🧑‍🚀-------------")
    print(f"\nAtualmente, temos {combustivel} litros no tanque!")
    print(f"\nNossa tripulação é composta por: {tripulantes}\n")
    travarMenu()
    print("----------------------------------------\n")

def registrar_Tripulantes():
    print("----------------------------------------\n")
    novotripulante = input("qual é o nome do novo tripulante?:\n")
    tripulantes.append(novotripulante)
    print("Novo tripulante inserido com sucesso!🚀")
    travarMenu()
    print("----------------------------------------\n")

#Cria uma função que tira o ultimo tripulante
def retirar_tripulantes():
    print("----------------------------------------\n")
    print(f"Atualmente nossos passageiros são: {tripulantes}")
    retirar =input("Gostaria que retirar o ultimo tripulante registrado? Essa ação não poderá ser desfeita! \n")
    if retirar == "sim" and tripulantes != []:
        print(f"Certo! Eramos {tripulantes}. Agora, temos:")
        tripulantes.pop()
        print(f"\n {tripulantes}!")
    elif retirar == "sim" and tripulantes == []:
        print("Ei! Como você quer tirar uma pessoa se nem temos nenhuma? Adicione para retirar!")

    else:
        print("Certo! Interaçâo encerrada.")
    travarMenu()
    print("----------------------------------------\n")

#Criar uma função para pausar o código entre as interações do usuário

def travarMenu():
    #o codigo
    input("\n Pressione <ENTER> para continuar....")

#criar um menu
print("----------------------------------------\n")
print("Bem vindo ao menu interativo da nave. Por favor, selecione uma opçâo:")
while True:
    print("\n 1- Mostrar status da nave 💻 | 2- Viajar 🚀 | 3- Abastecer ⛽ | 4- Novo tribulante 🧑‍🚀 | 5- Retirar tripulantes 🚶‍➡️ | 6- Sair ❌")
    opção = input("Escolha: ")
    
    if opção == "1":
        status_nave()
    elif opção == "2":
        viajar()
    elif opção == "3":
     abastecer()
    elif opção == "4":
        registrar_Tripulantes()
    elif opção == "5":
        retirar_tripulantes()
    else:
        print("Viagem encerrada!")
        break
print("----------------------------------------\n")

# viajar()
# viajar()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave() 