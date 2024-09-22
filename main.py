# Importa a classe Livro do arquivo livraria.py
from livraria import adicionarLivro, atualizarEstoque, buscarLivros, listarLivros, removerLivro

# Lista de livros
livros = []

# Introdução ao aplicativo
print("Aplicativo de biblioteca.")
print("Bem vindo!")

# Loop de execução principal
while True:
    
    # Opções do menu principal
    print("Selecione uma opçao:")
    print("1 - Adicionar livro")
    print("2 - Lista livros")
    print("3 - Buscar livros")
    print("4 - Atualizar estoque")
    print("5 - Remover livro")
    print("6 - Encerrar o programa")

    # Input do usuário pra fazer uma ação
    # Out: ->
    opcao = input("-> ")

    # Primeiro coisa: Fechar o programa
    # Pq? Sla, sempre fiz assim e vou fazer assim
    if opcao == "6":
        print("Encerrando aplicação...")
        from time import sleep
        sleep(5)
        break

    # Cria um livro novo
    elif opcao == "1":
        adicionarLivro(livros)
    
    # Listando livros existentes
    elif opcao == "2":
        listarLivros(livros)

    # Busca de livro através do título ou ISBN
    elif opcao == "3":
        buscarLivros(livros)

    # Atualiza o estoque de um livro
    elif opcao == "4":
        atualizarEstoque(livros)

    # Remove um livro da lista de livros            
    elif opcao == "5":
        removerLivro(livros)

    # Qualquer outra coisa que não for as opções do programa
    else:
        print("Opção inválida.")