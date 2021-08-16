class Pessoa:  # Classe
    def __init__(self, nome=None, idade=38):  # atributo de dados
        self.nome = nome
        self.idade = idade


    def cumprimentar(self): #
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Júnior')  # cria o objeto
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Eduardo'
    print(p.nome)
    print(p.idade)
