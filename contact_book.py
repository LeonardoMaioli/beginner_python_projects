#Programa para gerenciar uma lista de contatos. Ele deve permitir adicionar, remover, buscar e atualizar informações de contato. Use um dicionário para armazenar os contatos, onde a chave é o nome e o valor é outro dicionário com detalhes como telefone e email.

import os

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

def listar_contatos():
    #Listar todos os contatos da agenda
    #Oferecer opções da tela inicial aqui também, com exceção de listar. Adicionar opção de voltar a tela inicial
    pass

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


escolha = 0

while escolha != 6:
    mostrar_tela_inicial()
    escolha = int(input())
    if escolha == 6:
        fechar_agenda()

