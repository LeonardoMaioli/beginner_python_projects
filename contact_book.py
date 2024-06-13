#Programa para gerenciar uma lista de contatos. Ele permite adicionar, remover, buscar e atualizar informações de um contato. Os contatos são armazenados em um dicionário, onde a chave é o nome e o valor é outro dicionário com detalhes como telefone e email.

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


def pesquisar_contato(contatos):
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|         Pesquisa de um contato        |")
    print("|---------------------------------------|")
    nome = input("Digite o nome do contato para pesquisa: ")
    if nome in contatos:
        print("\nInformações do contato:\n")
        print("|---------------------------------------|")
        print(f"|  Nome: {nome} \n|  Telefone: {contatos[nome]['Telefone']} \n|  E-mail: {contatos[nome]['E-mail']}")
        print("|---------------------------------------|")
        voltar_tela_inicial = 0
        while voltar_tela_inicial != 1:
            voltar_tela_inicial = int(input("Digite 1 para voltar para tela inicial da agenda: "))
    else:
        print("Nome de contato não encontrado na sua agenda telefônica!")
        time.sleep(1)
        contatos_com_nome = [chave for chave in contatos if nome in chave]
        if contatos_com_nome:
            print(f"\nSegue a lista de contatos que possuem a sequência {nome} em seu nome:\n")
            print("|---------------------------------------|")
            for chave in contatos_com_nome:
                print(f"|  Nome: {chave} \n|  Telefone: {contatos[chave]['Telefone']} \n|  E-mail: {contatos[chave]['E-mail']}")
                print("|---------------------------------------|")
            voltar_tela_inicial = 0
            while voltar_tela_inicial != 1:
                voltar_tela_inicial = int(input("Digite 1 para voltar para tela inicial da agenda: "))
        else:
            print(f"Nenhum contato possui a sequência {nome} em seu nome!")
    print("Voltando para tela inicial em 3s...")
    time.sleep(3)


def adicionar_contato(contatos, *args):
    if args:
        contatos[args[0]] = {'Telefone': args[1], 'E-mail': args[2]}
    else:
        limpar_tela()
        print(" --------------------------------------- ")
        print("|          AGENDA DE CONTATOS           |")
        print("|---------------------------------------|")
        print("|      Adicionando um novo contato      |")
        print("|---------------------------------------|")
        nome = input("Digite o nome do novo contato: ")
        if nome in contatos:
            limpar_tela()
            print("Esse nome já está sendo usado em outro contato!")
        else:
            telefone = input("Digite o telefone do novo contato: ")
            email = input("Digite o email do novo contato: ")
            contatos[nome] = {'Telefone': telefone, 'E-mail': email}
            limpar_tela()
            print("Contato adicionado com sucesso!")
        print("Voltando para tela inicial em 3s...")
        time.sleep(3)


def remover_contato(contatos, *args):
    if args:
        del contatos[args[0]]
    else:
        limpar_tela()
        print(" --------------------------------------- ")
        print("|          AGENDA DE CONTATOS           |")
        print("|---------------------------------------|")
        print("|         Remoção de um contato         |")
        print("|---------------------------------------|")
        nome = input("Digite o nome do contato a ser removido: ")
        if nome in contatos:
            resposta = input(f"Tem certeza que deseja excluir {nome} dos contatos? (S/N): ")
            limpar_tela()
            if resposta == 'S':
                del contatos[nome]
                print("Contato removido com sucesso!")
            else:
                print("Cancelamento de contato abortado!")
        else:
            limpar_tela()
            print(f"O nome {nome} não está na lista de contatos!")
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
        novo_nome = input("Digite o novo nome para o contato. Se quiser manter o mesmo, digite 1: ")
        if novo_nome != 1 and novo_nome in contatos:
            limpar_tela()
            print("Esse nome já está sendo utilizado para outro contato!")
            print("Voltando para tela inicial em 3s...")
        else:
            remove = 1
            if novo_nome == '1': 
                novo_nome = nome_antigo
                remove = 0
            novo_tel = input("Digite o novo telefone para o contato: ")
            novo_email = input("Digite o novo email para o contato: ")
            adicionar_contato(contatos, novo_nome, novo_tel, novo_email)
            if remove == 1:
                remover_contato(contatos, nome_antigo)
            limpar_tela()
            print("Contato atualizado com sucesso!")
            print("Voltando para tela inicial em 3s...")
    else:
        limpar_tela()
        print("Contato não encontrado!")
        print("Voltando para tela inicial em 3s...")
    time.sleep(3)


def listar_contatos(contatos):
    limpar_tela()
    print(" --------------------------------------- ")
    print("|          AGENDA DE CONTATOS           |")
    print("|---------------------------------------|")
    print("|  Lista de contatos salvos na agenda   |")
    print(" --------------------------------------- ")

    for nome, info in contatos.items():
        escolha_lista = 0
        print(f"|  Nome: {nome} \n|  Telefone: {info['Telefone']} \n|  E-mail: {info['E-mail']}")
        print("|---------------------------------------|")
    
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


contatos = ({'Leonardo': {'Telefone': '11995847145', 'E-mail': 'leo@gmail.com'}, 'Julyano': {'Telefone': '81990000000', 'E-mail': 'ju@gmail.com'}})

escolha = 0

while escolha != 6:
    mostrar_tela_inicial()
    escolha = int(input())
    if escolha == 1:
        pesquisar_contato(contatos)
    elif escolha == 2:
        adicionar_contato(contatos)
    elif escolha == 3:
        remover_contato(contatos)
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
