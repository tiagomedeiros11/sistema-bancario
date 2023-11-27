menu = """
###########################
#   Selecione uma opção:  #
#                         #
# [1] - DEPÓSITO          #
# [2] - SAQUE             #
# [3] - EXTRATO           #
# [4] - SAIR              #
#                         #
###########################
"""



def deposito(saldo, valor, extrato,/):
    if valor > 0:        
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Foi realizado um depósito de {valor:.2f} R$ ")
    else:
        print("O valor do deposito precisa ser maior que Zero")    
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(" Extrato ".center(35,"#",))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Seu saldo atual é de R$ {saldo:.2f}")
    print(" Fim ".center(35,"#"))

def saque(valor,saldo,numero_saques,extrato):
    limite_saques = 3
    limite_por_saque = 500
    if numero_saques == limite_saques:
        print("Limite de saques atingidos!")
    elif valor > limite_por_saque:
        print("Limite por saque superior ao permitido")
    elif valor <= saldo:
        print(f"Foi realizado um saque de {valor:.2f} R$ ")
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
    else:
        print("Valor indisponivel para saque!")

    return saldo, extrato, numero_saques


saldo = 0
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor do depósito?"))

        saldo, extrato = deposito(saldo, valor, extrato)
            
    elif opcao == "2":
        valor = float(input("Qual o valor do saque?"))
        
        saldo, extrato, numero_saques = saque(valor,saldo,numero_saques,extrato)
        

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        print("Obrigado por usar essa bosta!")
        break
    
    else:
        print("Opção inválida, selecione novamente a operação desejada")

        





