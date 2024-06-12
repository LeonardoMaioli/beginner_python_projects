#Programa para gerenciar uma lista de contatos. Ele deve permitir adicionar, remover, buscar e atualizar informações de contato. Use um dicionário para armazenar os contatos, onde a chave é o nome e o valor é outro dicionário com detalhes como telefone e email.

def mostrar_tela_inicial():
    """colocar título
    colocar opções
        - pesquisar contato por nome ou número
        - adicionar contato
        - remover contato
        - atualizar contato
        - listar todos os contatos
        - fechar agenda
        """
    pass

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
    #Encerrar o programa
    pass


escolha = 0

while escolha != 6:
    mostrar_tela_inicial()    
