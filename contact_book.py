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

def adicionar_contato():
    #Pedir nome, contato, email
    #Verificar nomes iguais
    #Adiconar contato e voltar a tela inicial (Mensagem de contato adicionado, esperar, voltar)
    pass

def remover_contato():
    #Pedir nome para remoção
    #Mensagem de confirmação de exclusão
    #Remover contato e voltar a tela inicial (Mensagem de contato removido, esperar, voltar)
    pass

def atualizar_contato():
    #Pedir nome para atualização
    #Atualizar item específico ou todos? Receber novos dados, atualizar e voltar para tela inicial
    pass

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
        atualizar_contato()
    elif escolha == 5:
        listar_contatos(contatos)
    elif escolha == 6:
        fechar_agenda()
    else:
        limpar_tela()
        print(f"O comando {escolha} é inválido!")
        print("Voltando para tela inicial em 5s...")
        time.sleep(5)

