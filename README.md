# Projetos simples para iniciantes em Python

> Status: em andamento

## _índice_

- <a href="#resumo">Resumo</a>
- <a href="#agenda-contatos">Projeto 1 - Agenda de Contatos</a>
- <a href="#">Projeto 2 - Sistema Bancário</a>

## _Resumo_

Este repositório contém projetos simples e de nível iniciante para pessoas que estejam iniciando os estudos em Python e desejam aplicar os conceitos estudados em algumas tarefas interessantes, para fixar e melhorar o aprendizado. Cada um dos tópicos seguintes traz informações de um projeto, como o objetivo, o que deve ser realizado, assim como um código criado como uma possível solução do projeto. Alguns dos conceitos explorados nesses projeto são:

* Entrada e saída de dados
* Variáveis
* Tipos de dados
* Estruturas lógicas
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Manipulação de Strings
* Estruturas de Coleção

## _Projeto 1 - Agenda de Contatos_

O primeiro projeto tem o objetivo da criação de um programa para gerenciar uma agenda de contatos. O programa deve permitir ações como adicionar um novo contato, remover um contato existente, buscar informações de um contato e atualizar informações de um contato. Os contatos devem ser armazenados em um dicionário, onde a chave é o nome do contato e o valor é outro dicionário com detalhes como telefone e email. Quando solicitada, a lista de contatos deve ser exibida em ordem alfabética pelo nome do contato.

O arquivo pronto, com um exemplo de código que atende o projeto, pode ser acessado [clicando aqui](https://github.com/LeonardoMaioli/beginner_python_projects/blob/main/projects/contact_book.py)

## _Projeto 2 - Sistema Bancário_

Esse segundo projeto tem como objetivo a criação de um sistema bancário simples, que permita as operações de depósito, saque e visualização de extrato bancário. A ideia desse projeto foi introduzida durante um bootcamp da [DIO](https://www.dio.me/) como um desafio para os participantes. O conteúdo da triha de Python da DIO em que esse desafio foi proposto pode ser [acessada por aqui!](https://github.com/digitalinnovationone/trilha-python-dio)
Para cada uma dessas operações do sistema bancário também foram impostas algumas restrições:

- **Operação de Depósito:** Deve ser possível depositar apenas valores positivos para conta bancária. Além disso, essa versão do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Por fim, todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.
- **Operação de Saque:** O sistema deve permitir realizar no máximo 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato
- **Operação de Extrato:** Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45.

O arquivo com uma solução para esse projeto, pode ser acessado [clicando aqui](https://github.com/LeonardoMaioli/beginner_python_projects/blob/main/projects/banking_system.py)
