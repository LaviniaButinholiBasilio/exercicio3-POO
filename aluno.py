from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, estado_naturalidade, curso):
        super().__init__(nome, estado_naturalidade)
        self.curso = curso

    def obter_estado_naturalidade(self):
        return self.estado_naturalidade

    def obter_coordenador_curso(self):
        return self.curso.coordenador
