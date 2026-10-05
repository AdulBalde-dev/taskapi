from pydantic import BaseModel

# Importamos BaseModel do Pydantic.
#
# BaseModel permite criar modelos que definem:
# - quais dados esperamos receber;
# - quais tipos esses dados devem ter;
# - quais regras de validação eles devem seguir.
#
# Vamos utilizar BaseModel principalmente para validar
# os dados recebidos no corpo (body) das requisições.

# Importamos Enum do Python.
#
# Enum serve para definir um conjunto limitado de valores
# possíveis.
#
# Exemplo:
# Uma prioridade pode ser:
# - low
# - medium
# - high
# - urgent
#
# Não queremos aceitar qualquer texto como prioridade.
from enum import Enum


# ============================================================
# ENUM DE PRIORIDADE
# ============================================================

class Priority(str, Enum):
    """
    Define os valores permitidos para a prioridade de uma tarefa.

    'str':
        Faz com que os valores do Enum também se comportem
        como strings, o que é conveniente para trabalhar
        com JSON e APIs.

    'Enum':
        Faz com que Priority seja uma enumeração, ou seja,
        um conjunto fechado de valores possíveis.
    """

    # Nome da opção = valor que será enviado/recebido no JSON
    LOW = "low"

    # Prioridade média
    MEDIUM = "medium"

    # Prioridade alta
    HIGH = "high"

    # Prioridade urgente
    URGENT = "urgent"


# ============================================================
# MODELO DE DADOS DA TAREFA
# ============================================================

class Task(BaseModel):
    """
    Modelo Pydantic que representa os dados esperados
    quando queremos criar uma tarefa.

    O Pydantic utiliza essas definições para validar
    automaticamente os dados recebidos pela API.
    """

    # Título da tarefa.
    #
    # ': str' significa que esperamos uma string.
    title: str

    # Descrição da tarefa.
    #
    # Também esperamos uma string.
    description: str

    # Prioridade da tarefa.
    #
    # Aqui não usamos 'str'.
    #
    # Usamos 'Priority', porque queremos permitir somente
    # os valores definidos no Enum:
    #
    # low
    # medium
    # high
    # urgent
    priority: Priority