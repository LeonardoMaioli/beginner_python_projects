import os
import time

def deposito(saldo, extrato):
    limpar_tela()
    valor_deposito = float(input(menu_deposito))
    if valor_deposito == 0:
        print("0peração de depósito cancelada!")
    elif valor_deposito > 0:
        saldo += valor_deposito
        extrato += "d" + str(valor_deposito) + " "
        print("Depósito realizado com sucesso. Cheque seu extrato!")
    else:
        print("Operação inválida -> Depósito não pode ser negativo!")
    print("Voltando ao menu inicial em 3s...")
    time.sleep(3)   
    return extrato, saldo

def saque(saldo, extrato, limite_saque, numero_saques_dia):
    limpar_tela()
    valor_saque = float(input(menu_saque))
    if valor_saque == 0:
        print("0peração de saque cancelada!")
    elif valor_saque > limite_saque:
        print("Operação de saque cancelada -> Limite de saque ultrapassado!")
    elif valor_saque > 0:
        if valor_saque <= saldo:
            saldo -= valor_saque
            extrato += "s" + str(valor_saque) + " "
            numero_saques_dia += 1
            print("Saque realizado com sucesso. Cheque seu extrato!")
        else:
            print("Operação de saque cancelada -> Saldo insuficiente!")
    else:
        print("Operação inválida -> Saque não pode ser negativo!")
    print("Voltando ao menu inicial em 3s...")
    time.sleep(3)   
    return extrato, saldo, numero_saques_dia

def mostrar_extrato(extrato, saldo):
    limpar_tela()
    print(menu_extrato)
    if extrato == "":
        print("Não foram realizadas movimentações na sua conta!")
    else:
        posicao = 0
        while posicao < len(extrato):
            operacao = extrato[posicao]
            posicao += 1 
            valor = ""
            
            while extrato[posicao] != " ":
                valor += extrato[posicao]
                posicao += 1
            
            if operacao == 'd':
                print(f"+ Depósito de: R${valor}")
            elif operacao == 's':
                print(f"- Saque de: R${valor}")
            posicao += 1
    print(f"> Saldo atual: R${saldo}")
    voltar = 0
    while voltar != "1":
        voltar = input("\nPara voltar para a tela inicial, digite 1: \n=>")

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

menu_inicial = """
----------------------------------------
|           SISTEMA BANCÁRIO           |
|     Qual serviço deseja realizar?    |                   
----------------------------------------                 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
----------------------------------------
Digite aqui:
=> """

menu_deposito = """
----------------------------------------
|           SISTEMA BANCÁRIO           |
|    Operação selecionada: Depósito    |                   
----------------------------------------                 
Digite o valor de depósito ou 0 para cancelar a operação:
=> """

menu_saque = """
----------------------------------------
|           SISTEMA BANCÁRIO           |
|     Operação selecionada: Saque      |                   
----------------------------------------                 
Digite o valor de saque ou 0 para cancelar a operação:
=> """

menu_extrato = """
----------------------------------------
|           SISTEMA BANCÁRIO           |
|    Operação selecionada: Extrato     |                   
----------------------------------------                 
Segue os depósitos e saques realizados na sua conta:
"""

menu_saida = """
----------------------------------------
|      SISTEMA BANCÁRIO ENCERRADO      |                   
----------------------------------------                 
"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques_dia = 0
LIMITE_SAQUES_DIA = 3

while True:
    limpar_tela()
    opcao = input(menu_inicial)

    if opcao == "d":
        extrato, saldo = deposito(saldo, extrato)

    elif opcao == "s":
        if numero_saques_dia >= LIMITE_SAQUES_DIA:
            print("Limite de saque diário atingido -> Máximo de 3 saques por dia!")
            print("Voltando ao menu inicial em 3s...")
            time.sleep(3)
        else:
            extrato, saldo, numero_saques_dia = saque(saldo, extrato, limite_saque, numero_saques_dia)

    elif opcao == "e":
        mostrar_extrato(extrato, saldo)

    elif opcao == "q":
        limpar_tela()
        print(menu_saida)
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        print("Voltando ao menu inicial em 3s...")
        time.sleep(3)    
        