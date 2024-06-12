#Programa para gerenciar uma lista de contatos. Ele deve permitir adicionar, remover, buscar e atualizar informações de contato. Use um dicionário para armazenar os contatos, onde a chave é o nome e o valor é outro dicionário com detalhes como telefone e email.

import os
import time

def mostrar_tela_inicial():
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|     Pesquisar Contato - Digite 1      |")
    print("|     Adicionar Contato - Digite 2      |")
    print("|     Remover Contato   - Digite 3      |")
    print("|     Atualizar Contato - Digite 4      |")
    print("|     Listar Contatos   - Digite 5      |")
    print("|     Fechar Agenda     - Digite 6      |")
    print(" --------------------------------------- ")
    print("Digite sua escolha:")


def pesquisar_contato():
    #Por qual item vai pesquisar?
    #Receber item ou parte do item
    #Mostrar resultados encontrados
    #Oferecer opções da tela inicial e adicionar opção para voltar para tela inicial
    pass

def adicionar_contato(contatos, *args):
    if args:
        contatos[args[0]] = {'Telefone': args[1], 'E-mail': args[2]}
    else:
        nome = input("Digite o nome do novo contato: ")
        #Checar nome repetido
        telefone = input("Digite o telefone do novo contato: ")
        email = input("Digite o email do novo contato: ")
        contatos[nome] = {'Telefone': telefone, 'E-mail': email}
        print("Contato adicionado com sucesso!")
        print("Voltando para tela inicial em 3s...")
        time.sleep(3)

def remover_contato(contatos, *args):
    if args:
        del contatos[args[0]]
    else:
        nome = input("Digite o nome do contato a ser removido: ")
        #Checar se nome existe
        #Mensagem de confirmação ("Tem certeza?")
        del contatos[nome]
        print("Contato removido com sucesso!")
        print("Voltando para tela inicial em 3s...")
        time.sleep(3)

def atualizar_contato(contatos):
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|       Atualização de um contato       |")
    print("|---------------------------------------|")
    nome_antigo = input("Digite o nome do contato que deseja atualizar: ")
    if nome_antigo in contatos:
        novo_nome = input("Digite o novo nome para o contato: ")
        #Checar se nome já não está na agenda
        novo_tel = input("Digite o novo telefone para o contato: ")
        novo_email = input("Digite o novo email para o contato: ")
        adicionar_contato(contatos, novo_nome, novo_tel, novo_email)
        #Remover apenas se o nome_antigo != do novo ou sempre? Pode remover o nome criado talvez
        remover_contato(contatos, nome_antigo)
        print("Contato atualizado com sucesso!")
        print("Voltando para tela inicial em 3s...")
    else:
        print("Contato não encontrado!")
        print("Voltando para tela inicial em 3s...")
    time.sleep(3)

def listar_contatos(contatos):
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|  Lista de contatos salvos na agenda   |")
    print("|---------------------------------------|")

    for nome, info in contatos.items():
        escolha_lista = 0
        print(f"Nome: {nome} \nTelefone: {info['Telefone']} \nE-mail: {info['E-mail']}")
        print("---------------------------------------")
    
    voltar_tela_inicial = 0
    while voltar_tela_inicial != 1:
        voltar_tela_inicial = int(input("Digite 1 para voltar para tela inicial da agenda: "))
    
    print("Voltando para tela inicial em 3s...")
    time.sleep(3)

def fechar_agenda():
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|  Agenda salva e fechada com sucesso!  |")
    print(" --------------------------------------- ")

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


contatos = ({'Leonardo Maioli': {'Telefone': '27997723646', 'E-mail': 'leo.severgnine@gmail.com'}, 'Julyano': {'Telefone': '00000000000', 'E-mail': 'ju@gmail.com'}})

escolha = 0

while escolha != 6:
    mostrar_tela_inicial()
    escolha = int(input())
    if escolha == 1:
        pesquisar_contato()
    elif escolha == 2:
        adicionar_contato()
    elif escolha == 3:
        remover_contato()
    elif escolha == 4:
        atualizar_contato(contatos)
    elif escolha == 5:
        listar_contatos(contatos)
    elif escolha == 6:
        fechar_agenda()
    else:
        limpar_tela()
        print(f"O comando {escolha} é inválido!")
        print("Voltando para tela inicial em 5s...")
        time.sleep(5)

