class Curso:
    def __init__(self, nome, coordenador, escola):
        self.nome = nome
        self.coordenador = coordenador
        self.escola = escola

    def obter_escolaridade_coordenador(self):
        return self.coordenador.escolaridade.nivel
