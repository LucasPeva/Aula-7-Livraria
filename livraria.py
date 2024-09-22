# Classe livro para organizar os livros
class Livro():

    # Constructor da classe Livro
    def __init__(self, titulo: str, autor: str, isbn: int, preco: float, quantidadeEmEstoque: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco
        self.quantidadeEmEstoque = quantidadeEmEstoque

    # Método para adionar ao estoque
    # TODO: fazer tudo aqui de estoque usar banco de dados, sqlite?
    def adicionarAoEstoque(self, quantidade: int):
        self.quantidadeEmEstoque += quantidade
    
    # Método para remover do estoque
    def removerDoEstoque(self, quantidade: int):
        if quantidade > self.quantidadeEmEstoque:
            print("Erro: Não há quantidade suficiente em estoque")
        else:
            self.quantidadeEmEstoque -= quantidade
            print("Estoque atualizado")

    
    # Método para exibir as informações do objeto Livro
    def exibirInformacoes(self): 
        print(30*"-")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Preço: {self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidadeEmEstoque}")

# Funções para o aplicativo

def adicionarLivro(livros):
    # Input do usuário pra obter dados do novo livro
    novoLivroNome = input(str("Título: "))
    novoLivroAutor = input(str("Autor: "))
    novoLivroISBN = int(input("ISBN: "))
    novoLivroPreco = float(input("Preço: "))
    novoLivroQuantidade = int(input("Quantidade inicial em estoque: "))
    print()

    # Criando o livro novo
    livro = Livro(novoLivroNome, novoLivroAutor, novoLivroISBN, novoLivroPreco, novoLivroQuantidade)
    livros.append(livro)
    return livro

def listarLivros(livros):
    print("Livros cadastrados: ")
    for livro in livros:
        livro.exibirInformacoes()
        print()
    return livros

def buscarLivros(livros):
    busca = input("Informe o ISBN ou titulo: ")
    for livro in livros:
        if livro.titulo.lower() == busca.lower() or str(livro.isbn) == busca:
            livro.exibirInformacoes()
            return livro
    print("Livro não encontrado")
    return None

def atualizarEstoque(livros):
    busca = input("Informe o ISBN ou titulo: ")
    for livro in livros:
        if livro.titulo.lower() == busca.lower() or str(livro.isbn) == busca:
            quantidade = int(input("Quantidade a ser adicionada ou removida: "))
            if quantidade > 0:
                livro.adicionarAoEstoque(quantidade)
            else:
                livro.removerDoEstoque(-quantidade)
            return livro
    print("Livro não encontrado")
    return None

def removerLivro(livros):
    busca = input("Informe o ISBN ou titulo: ")
    for livro in livros:
        if livro.titulo.lower() == busca.lower() or str(livro.isbn) == busca:
            livros.remove(livro)
            print("Livro removido.")
            return True
    print("Livro não encontrado")
    return False

