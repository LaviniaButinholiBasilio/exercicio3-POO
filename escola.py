class Escola:
    def __init__(self, nome, cidade, diretor):
        self.nome = nome
        self.cidade = cidade
        self.diretor = diretor

    def obter_escolaridade_diretor(self):
        return self.diretor.escolaridade.nivel
