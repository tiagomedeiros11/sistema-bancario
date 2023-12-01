menu = """
###########################
#   Selecione uma opção:  #
#                         #
# [1] - DEPÓSITO          #
# [2] - SAQUE             #
# [3] - EXTRATO           #
# [4] - CRIAR USUARIO     #
# [5] - CRIAR CONTA       #
# [6] - LISTAR CONTA      #
# [7] - SAIR              #
###########################
"""


saldo = 0
extrato = ""
numero_saques = 0
lista_usuarios = []
AGENCIA = "0001"
contas = []

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

def criar_usuario(nome,data_nascimento,cpf,endereco):
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereço": endereco
    }
    return usuario
    
def filtrar_usuario(lista, cpf):
    '''Função para verificar se existe usuario com o cpf inserido, baseado em uma lista de dicionarios'''
    return [d for d in lista if d.get("cpf") == cpf]

def adicionar_usuario_a_lista(usuario, lista_usuarios):
    '''Função para adicionar os usuários cadastrados na lista de usuários'''
    cpf = usuario['cpf']
    if cpf not in [u['cpf'] for u in lista_usuarios]:
        lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("Erro: Já existe um usuário com o CPF fornecido.")

    return lista_usuarios    
    

def criar_conta(agencia, numero_da_conta, lista_usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_usuario(lista_usuarios, cpf)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario[0]}
    
    print("Usuário não encontrado, encerrando o cadastro da conta")

def listar_contas(contas):
    
    for conta in contas:
       titular = conta['usuario']['nome']
       linha = f""" 
    Agencia: {conta['agencia']}
    CC: {conta['numero_da_conta']}
    Titular da conta: {conta['usuario']['nome']}
        """
       print(linha)



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
        nome = str(input("Digite seu nome: "))
        data_nascimento = (input("Digite a data de nascimento (DD/MM/AAAA): "))
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")

        usuario_cadastrado = criar_usuario(nome,data_nascimento,cpf,endereco)
        lista_usuarios = adicionar_usuario_a_lista(usuario_cadastrado,lista_usuarios)
        
    elif opcao == "5":
        numero_conta = len(contas) + 1 
        conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

        if conta:
            contas.append(conta) 
        
    elif opcao == "6":
        listar_contas(contas)
        

    elif opcao == "7":
        print("Obrigado por usar essa bosta!")
        break
    
    else:
        print("Opção inválida, selecione novamente a operação desejada")

