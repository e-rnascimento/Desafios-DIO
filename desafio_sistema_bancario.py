menu = """"
Digite a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

deposito = """"
Por favor, digite o valor que deseja depositar
"""

saque = """"
Por favor, digite o valor que deseja sacar
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 3
limite_saque = 500

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input(deposito))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito no valor de: R${valor_deposito:.2f}.\n"
            print(f"Depósito no valor de R${valor_deposito:.2f} realizado com sucesso.\n")
        else:    
            print("Valor inválido! Retornando para o menu principal\n")

    elif opcao == "s":

        if numero_saques <= 0:
            print("Você excedeu o limite de saques diários.\n")
        
        elif numero_saques > 0:
            valor_saque = float(input(saque)) 

            if valor_saque > saldo:
                print("Não há saldo suficiente em conta para realizador o saque no valor solicitado. Consulte seu extrato\n")
            elif valor_saque > limite_saque:
                print(f"Valor solicitado é maior que o seu limite por saque.\n")

            else:
                saldo -= valor_saque
                numero_saques -= 1
                extrato += f"Saque no valor de: R${valor_saque:.2f}.\n"
                print(f"Saque no valor de R${valor_saque:.2f} foi realizado em sua conta.\n")
    
    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas operações.\n")
        else:
            extrato += f"Saldo em conta: R$ {saldo:.2f}\n"
            print("============EXTRATO============\n")
            print(extrato)
            print("===============================")

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente.\n")