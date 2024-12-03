from aluno import Aluno
from professor import Professor
from tipo_ensino import TipoEnsino
from curso import Curso
from escola import Escola
from cidade import Cidade


cidade = Cidade("São Paulo", "SP")
diretor = Professor("Carlos Silva", "SP", None, None)
escola = Escola("Escola ABC", cidade, diretor)

coordenador = Professor("Ana Pereira", "RJ", None, None)
curso = Curso("Engenharia", coordenador, escola)

aluno = Aluno("João Souza", "MG", curso)
tipo_ensino = TipoEnsino("Superior")


print(f"Aluno: {aluno.nome}, Estado de Naturalidade: {aluno.obter_estado_naturalidade()}")
print(f"Coordenador do Curso: {aluno.obter_coordenador_curso().nome}")
print(f"Escola: {escola.nome}, Cidade: {escola.cidade.nome}")
