menu = """
    [d]: Depositar
    [s]: Sacar
    [e]: Extrato
    [q]: Sair
"""

LIMITE_SAQUE = 3
limite = 500
saldo = 0
extrato = ""
numero_saques = 0


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que quer depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f}\n"

        else:
            print("Operação falhou, valor invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_limite = valor > limite
        maior_que_saldo = valor > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_limite:
            print("Operação invalida. Máximo permitido é R$500,00")
        elif maior_que_saldo:
            print("Saldo insuficiente!")
        elif excedeu_saques:
            print("Limite de 3 saques diario atingindo. Tente novamente amanhã")
        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque realizado no valor de {valor}\n"
        else:
            print("Operação falhou, valor invalido")

    elif opcao == "e":
        print("       Extrato       ")
        print("Sem movimentações na conta" if not extrato else extrato)
        print(f"Saldo total: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida!")
