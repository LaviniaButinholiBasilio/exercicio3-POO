from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, estado_naturalidade, escolaridade, tipo_ensino, diretor=None, coordenador=None):
        super().__init__(nome, estado_naturalidade)
        self.escolaridade = escolaridade
        self.tipo_ensino = tipo_ensino
        self.diretor = diretor
        self.coordenador = coordenador

    def obter_escolaridade(self):
        return self.escolaridade.nivel

    def obter_estado_nascimento(self):
        return self.estado_naturalidade

    def obter_tipo_ensino(self):
        return self.tipo_ensino.tipo

    def obter_diretor(self):
        return self.diretor

    def obter_coordenador(self):
        return self.coordenador
