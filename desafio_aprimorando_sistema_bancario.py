usuarios_cadastrados = {}
numero_contas = [0]
contas_cadastradas = {}

def cadastrar_usuario():
   
   while True:
       cpf = input("Para cadastrar um usuário, digite seu CPF, contendo somente números: ")
       
       if "." in cpf:
            cpf = input("Valor inválido, digite somente os números do seu CPF: ")
       
       elif cpf in usuarios_cadastrados:
            conta = input("Usuário já cadastrado. Deseja cadastrar uma nova conta? (s/n)")
            while True:
                if conta == "s":
                    cadastrar_conta(cpf=cpf)
                    break
                elif conta == "n":
                    break
                else:
                    print("Opção inválida.")
                    break  
       else:
            nome = input("Digite seu nome completo: ")
            data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
            endereco = input("Digite o seu endereço, seguindo o formato (logradouro, número - bairro - cidade/sigla estado): ")
            usuarios_cadastrados[cpf] = {"Nome" : nome, "Data de nascimento": data_nasc, "Endereço": endereco}
            
            print("Usuário cadastrado com sucesso!")
            break
       
   return usuarios_cadastrados

def cadastrar_conta(cpf, numero_contas=numero_contas):
    if cpf in usuarios_cadastrados:
        agencia = "0001"
        cc = numero_contas[-1] + 1
        numero_contas.append(cc)
        contas_cadastradas[cpf] = {"agência:": agencia, "cc": cc, "saldo": 0, "extrato":"", \
                                    "limite": 500, "numero_saques":3}
        print(f"Conta cadastrada com sucesso! Seguem os dados da sua conta:\n Agência: {agencia}\n Conta corrente: {cc}\n")
    
    else:
        usuario = input("Usuário não cadastrado. Deseja realizar cadastrar um novo usuário? (s/n)")
        while True:
                if usuario == "s":
                    usuarios_cadastrados[cpf] = cadastrar_usuario()
                    break
                elif usuario == "n":
                    break
                else:
                    print("Opção inválida.")
                    break
    
    return contas_cadastradas


def depositar(saldo, valor, extrato, /):
     if valor > 0:
            saldo += valor
            extrato += f"\nDepósito no valor de: R${valor_deposito:.2f}.\n"
            print(f"Depósito no valor de R${valor_deposito:.2f} realizado com sucesso.\n")
     else:    
         print("Valor inválido! Retornando para o menu principal\n")
     return saldo, extrato
     

def sacar(*,saldo,numero,valor,extrato,limite):
     if numero <= 0:
         print("Você excedeu o limite de saques diários.\n")
     else:
          if valor > saldo:
               print("Não há saldo suficiente em conta para realizador o saque no valor solicitado. Consulte seu extrato\n")
          elif valor > limite:
               print(f"Valor solicitado é maior que o seu limite por saque.\n")
          else:
               saldo -= valor
               numero -= 1
               extrato += f"Saque no valor de: R${valor_saque:.2f}.\n"
               print(f"Saque no valor de R${valor_saque:.2f} foi realizado em sua conta.\n")
     return saldo, extrato, numero
               
def exibir_extrato(saldo,/,*,extrato):
     if not extrato:
            print("Não foram realizadas operações em sua conta.\n")
     else:
            extrato += f"Saldo em conta: R$ {saldo:.2f}\n"
            print("============EXTRATO============\n")
            print(extrato)
            print("===============================")


menu_inicial = """"
Bem vindo ao sistema bancário. Digite a opção desejada:

[1] Cadastrar novo usuário
[2] Cadastrar nova conta
[3] Acessar conta
[4] Sair

"""

menu_conta = """"
Digite a opção desejada:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""


while True:
    opcao = input(menu_inicial)
    if opcao == "1":
         cadastrar_usuario()
    elif opcao == "2":
         cpf = input("Para cadastrar uma nova conta digite seu CPF (somente números): ")
         cadastrar_conta(cpf=cpf)
    elif opcao == "3":
         cpf = input("Para acessar sua conta digite seu CPF (somente dígitos): ")
         if cpf in contas_cadastradas:
            opcao2 = input(menu_conta)
            if opcao2 == "1":
                valor_deposito = float(input("Por favor, digite o valor que deseja depositar: "))
                contas_cadastradas[cpf]["saldo"], contas_cadastradas[cpf]["extrato"] = depositar(contas_cadastradas[cpf]["saldo"], valor_deposito, contas_cadastradas[cpf]["extrato"])       
                
            elif opcao2 == "2":
                valor_saque = float(input("Por favor, digite o valor que deseja sacar: ")) 
                contas_cadastradas[cpf]["saldo"], contas_cadastradas[cpf]["extrato"], \
                    contas_cadastradas[cpf]["numero_saques"] = sacar(valor=valor_saque, \
                                                                   numero=contas_cadastradas[cpf]["numero_saques"],\
                                                                      extrato=contas_cadastradas[cpf]["extrato"], \
                                                                        limite=contas_cadastradas[cpf]["limite"], \
                                                                            saldo=contas_cadastradas[cpf]["saldo"])

            elif opcao2 == "3":
                exibir_extrato(contas_cadastradas[cpf]["saldo"],extrato=contas_cadastradas[cpf]["extrato"])         

            elif opcao2 == "4":
                break
            else:
                print("Usuário não possui conta cadastrada.")
        
         else:
            print("Usuário não possui conta cadastrada.")
    
    elif opcao == "4":
        break
    else:
         print("Opção inválida.")
         break   

print(contas_cadastradas)
