class MenuBancario:
    def __init__(self):
        self.saldo = 2000.00
        self.limite = 500.00
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def menuInicial(self):
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Finalizar operação 

         """
        return menu

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def selecao_menu(self):
        while True:
            print(self.menuInicial())
            opcao = input("Escolha uma opção: ")

            if opcao == 'd':
                valor = float(input("Informe o valor do depósito: "))
                self.depositar(valor)
            elif opcao == 's':
                valor = float(input("Informe o valor do saque: "))
                self.sacar(valor)
            elif opcao == 'e':
                self.exibir_extrato()
            elif opcao == 'q':
                break
            else:
                print("Opção inválida, por favor selecione novamente!")


executar = MenuBancario()
executar.selecao_menu()