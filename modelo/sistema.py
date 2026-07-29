from modelo.avaliacao import Avaliacao



class Produto:
    produtos = []
    def __init__(self,id:str, nome:str, categoria:str,peso:float,preco:float):
        self._id = id.upper().strip()
        self._nome = nome.strip()
        self._categoria = categoria.strip()
        self._peso = float (peso)
        self._preco = float (preco)
        self._ativo = True
        self._avaliacoes = []
        Produto.produtos.append(self)


    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_produtos(cls):
        print(f'{"Nome do Produto:".ljust(25)} | {"Categoria do produto:".ljust(25)} | disponível: ')
        for estoque in cls.produtos:
            print(f'{estoque._nome.ljust(25)} | {estoque._categoria.ljust(25)} | {estoque.emoji()}')

    @property
    def ativo(self):
        return self._ativo

    def emoji(self):
        return "disponível" if self._ativo else "Indisponivel"
    

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_nota(self,cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print ("nota inválida")
            
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "-"
        somar_notas = sum (avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_notas = len (self._avaliacoes)
        media = round (somar_notas/quantidade_notas,1)
        return media 

    @classmethod
    def buscar_por_id(cls, id_produto):
        id_produto = id_produto.upper().strip()
        for produto in cls.produtos:
            if produto._id == id_produto:
                return produto
        return None