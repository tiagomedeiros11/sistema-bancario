class ContaBancaria:
    def __init__(self, agencia, numero_conta, usuario, saldo=0, extrato="", numero_saques=0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = saldo
        self.extrato = extrato
        self.numero_saques = numero_saques

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Foi realizado um depósito de {valor:.2f} R$ ")
        else:
            print("O valor do depósito precisa ser maior que Zero")

    def saque(self, valor):
        limite_saques = 3
        limite_por_saque = 500

        if self.numero_saques == limite_saques:
            print("Limite de saques atingidos!")
        elif valor > limite_por_saque:
            print("Limite por saque superior ao permitido")
        elif valor <= self.saldo:
            print(f"Foi realizado um saque de {valor:.2f} R$ ")
            self.saldo -= valor
            self.numero_saques += 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Valor indisponível para saque!")

    def exibir_extrato(self):
        print(" Extrato ".center(35, "#"))
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"Seu saldo atual é de R$ {self.saldo:.2f}")
        print(" Fim ".center(35, "#"))

    def __str__(self):
        return f"Agencia: {self.agencia}\nCC: {self.numero_conta}\nTitular da conta: {self.usuario['nome']}"


class Banco:
    def __init__(self):
        self.contas = []
        self.lista_usuarios = []
        self.AGENCIA = "0001"

    def criar_usuario(self, nome, data_nascimento, cpf, endereco):
        usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
        self.lista_usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    def criar_conta(self, usuario):
        numero_conta = len(self.contas) + 1
        conta = ContaBancaria(self.AGENCIA, numero_conta, usuario)
        self.contas.append(conta)
        print("Conta criada com sucesso")
        return conta

    def listar_contas(self):
        for conta in self.contas:
            print(conta)

    def filtrar_usuario(self, cpf):
        return [d for d in self.lista_usuarios if d.get("cpf") == cpf]


# Uso da classe Banco
banco = Banco()
conta = None

while True:
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

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Qual o valor do depósito?"))
        conta.deposito(valor)

    elif opcao == "2":
        valor = float(input("Qual o valor do saque?"))
        conta.saque(valor)

    elif opcao == "3":
        conta.exibir_extrato()

    elif opcao == "4":
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço: ")

        banco.criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "5":
        cpf = input("Digite seu CPF: ")
        usuario = banco.filtrar_usuario(cpf)

        if usuario:
            conta = banco.criar_conta(usuario[0])

    elif opcao == "6":
        banco.listar_contas()

    elif opcao == "7":
        print("Obrigado por usar este programa!")
        break

    else:
        print("Opção inválida, selecione novamente a operação desejada")