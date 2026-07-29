from modelo.sistema import Produto

class Menu:

    @staticmethod
    def exibir_opcoes():
        print("\n1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Avaliar produto")
        print("4 - Alternar disponibilidade")
        print("0 - Sair")

    @staticmethod
    def cadastrar_produto():
        print("\n--- Cadastro de novo produto ---")
        id_produto = input("ID: ")
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        peso = input("Peso: ")
        preco = input("Preço: ")
        Produto(id_produto, nome, categoria, peso, preco)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    @staticmethod
    def avaliar_produto():
        id_produto = input("ID do produto: ")
        produto = Produto.buscar_por_id(id_produto)

        if produto is None:
            print("Produto não encontrado!")
            return

        cliente = input("Seu nome: ")
        try:
            nota = float(input("Nota (0 a 5): "))
            produto.receber_nota(cliente, nota)
        except ValueError:
            print("Digite um número válido para a nota.")

    @staticmethod
    def alternar_disponibilidade():
        id_produto = input("ID do produto: ")
        produto = Produto.buscar_por_id(id_produto)

        if produto is None:
            print("Produto não encontrado!")
            return

        produto.alternar_estado()
        print(f"Produto '{produto._nome}' agora está: {produto.emoji()}")

    @classmethod
    def rodar(cls):
        while True:
            cls.exibir_opcoes()
            opcao = input("Escolha: ")

            if opcao == "1":
                Produto.listar_produtos()
            elif opcao == "2":
                cls.cadastrar_produto()
            elif opcao == "3":
                cls.avaliar_produto()
            elif opcao == "4":
                cls.alternar_disponibilidade()
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida")