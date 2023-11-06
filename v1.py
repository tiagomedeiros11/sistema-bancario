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
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = int(input("Qual o valor do depósito?"))
        if valor_deposito > 0:        
            print(f"Foi realizado um depósito de {valor_deposito:.2f} R$ ")
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("O valor do deposito precisa ser maior que Zero")    
    elif opcao == "2":
        valor_saque = float(input("Qual o valor do saque?"))
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques atingidos!")
        elif valor_saque > limite:
            print("Limite por saque superior ao permitido")
        elif valor_saque <= saldo:
            print(f"Foi realizado um saque de {valor_saque:.2f} R$ ")
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        else:
            print("Valor indisponivel para saque!")

    elif opcao == "3":
        print(" Extrato ".center(35,"#",))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Seu saldo atual é de R$ {saldo:.2f}")
        print(" Fim ".center(35,"#"))

    elif opcao == "4":
        print("Obrigado por usar essa bosta!")
        break
    
    else:
        print("Opção inválida, selecione novamente a operação desejada")

        





