# ============================================================
# IMPORTAÇÕES
# ============================================================

# Importamos a classe FastAPI.
#
# FastAPI é o framework que vamos utilizar para construir
# nossa API REST.
from fastapi import FastAPI
from app.models.user import User
from app.schemas.task import Task, Priority
from app.schemas.user import UserCreate
from app.database.database import engine, Base, SessionLocal
# ============================================================
# CRIAÇÃO DA APLICAÇÃO
# ============================================================

# Criamos uma instância da classe FastAPI.
#
# 'FastAPI' é a classe.
# 'app' é o objeto/instância que representa nossa aplicação.
#
# É através de 'app' que vamos registrar nossas rotas.
app = FastAPI()


# Cria no banco todas as tabelas dos modelos registrados no Base.
Base.metadata.create_all(bind=engine)

# ============================================================
# ROTA PRINCIPAL
# ============================================================

# @app.get("/")
#
# '@app.get' é um decorator.
#
# Ele informa ao FastAPI:
#
# "Quando alguém fizer uma requisição HTTP GET
#  para o caminho '/', execute a função abaixo."
#
# '/' representa a raiz da nossa API.
@app.get("/")
def home():

    # O FastAPI transforma este dicionário Python
    # em uma resposta JSON.
    return {"Hello": "World"}


# ============================================================
# ROTA /hello
# ============================================================

# Quando alguém fizer:
#
# GET /hello
#
# o FastAPI executará a função 'hello'.
@app.get("/hello")
def hello():

    # Retornamos um dicionário Python.
    #
    # O FastAPI transforma automaticamente esse dicionário
    # em JSON na resposta HTTP.
    return {"Hello": "FastAPI"}


# ============================================================
# PATH PARAMETER
# ============================================================

# Nesta rota:
#
# /tasks/{task_id}
#
# '{task_id}' é um PATH PARAMETER.
#
# Isso significa que o valor faz parte do caminho da URL.
#
# Exemplos:
#
# /tasks/1
# /tasks/10
# /tasks/500
#
# O valor será enviado para a função através da variável
# 'task_id'.
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    # ': int' é um type hint.
    #
    # Estamos dizendo ao FastAPI que esperamos que
    # 'task_id' seja um número inteiro.
    #
    # O FastAPI valida o valor antes de chamar a função.
    #
    # Portanto:
    #
    # /tasks/10     -> válido
    # /tasks/123    -> válido
    # /tasks/abc    -> inválido
    #
    # type(task_id)
    # retorna o tipo do objeto.
    #
    # .__name__
    # pega somente o nome do tipo.
    #
    # Exemplo:
    #
    # type(10)              -> <class 'int'>
    # type(10).__name__    -> 'int'

    return {
        "task_id": task_id,
        "tipo": type(task_id).__name__
    }


# ============================================================
# QUERY PARAMETERS
# ============================================================

# ------------------------------------------------------------
# EXEMPLO 1 — PARÂMETROS OBRIGATÓRIOS
# ------------------------------------------------------------

# Este exemplo está comentado porque não estamos utilizando
# esta versão atualmente.
#
# Aqui:
#
# completed: bool
# priority: str
#
# seriam parâmetros obrigatórios.
#
# Portanto:
#
# /tasks?completed=true&priority=high
#
# funcionaria.
#
# Mas:
#
# /tasks
#
# retornaria erro porque os parâmetros não foram enviados.

# @app.get("/tasks")
# def get_tasks(completed: bool, priority: str):
#     return {
#         "completed": completed,
#         "priority": priority
#     }


# ------------------------------------------------------------
# EXEMPLO 2 — PARÂMETROS OPCIONAIS
# ------------------------------------------------------------

# Aqui definimos a rota:
#
# GET /tasks
#
# Os valores serão recebidos através da QUERY STRING.
#
# Exemplos:
#
# /tasks
#
# /tasks?completed=true
#
# /tasks?priority=high
#
# /tasks?completed=false&priority=high
#
# /tasks?completed=false&priority=high&category=study
#
@app.get("/tasks")
def get_tasks(

    # 'completed' é opcional.
    #
    # bool:
    # esperamos True ou False.
    #
    # | None:
    # também permitimos que o valor seja None.
    #
    # = None:
    # se o usuário não enviar o parâmetro,
    # o valor será None.
    completed: bool | None = None,

    # 'priority' também é opcional.
    #
    # Porém, em vez de aceitar qualquer string,
    # usamos nosso Enum Priority.
    #
    # Portanto, valores válidos são:
    #
    # low
    # medium
    # high
    # urgent
    #
    # Um valor como:
    #
    # priority=banana
    #
    # será rejeitado pelo FastAPI/Pydantic.
    priority: Priority | None = None,

    # 'category' é opcional e deve ser uma string.
    #
    # Como não criamos um Enum para categorias,
    # qualquer string será aceita neste momento.
    category: str | None = None
):

    # Retornamos os valores recebidos.
    #
    # O FastAPI transforma automaticamente o dicionário
    # Python em JSON.
    #
    # Se o usuário acessar:
    #
    # /tasks?completed=false&priority=high&category=study
    #
    # teremos algo semelhante a:
    #
    # {
    #     "completed": false,
    #     "priority": "high",
    #     "category": "study"
    # }
    return {
        "completed": completed,
        "priority": priority,
        "category": category
    }


# ============================================================
# POST /tasks
# ============================================================

# Agora temos uma rota POST.
#
# POST normalmente é utilizado quando queremos enviar
# dados para o servidor para criar um novo recurso.
#
# Neste caso:
#
# POST /tasks
#
# significa:
#
# "Quero enviar os dados de uma nova tarefa para a API."
@app.post("/tasks")
def create_task(task: Task):

    # 'task: Task' é muito importante.
    #
    # Estamos dizendo:
    #
    # "O corpo (body) dessa requisição deve seguir
    #  o modelo Task."
    #
    # O Pydantic irá validar automaticamente os dados.
    #
    # Esperamos algo como:
    #
    # {
    #     "title": "Estudar FastAPI",
    #     "description": "Aprender Pydantic",
    #     "priority": "high"
    # }
    #
    # Se os dados estiverem errados, o FastAPI retorna
    # automaticamente um erro de validação.

    # Retornamos o objeto Task.
    #
    # O FastAPI transforma o modelo Pydantic em JSON
    # para enviar a resposta ao cliente.
    return task


@app.post("/users")
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

    # 'user: UserCreate' é muito importante.
    #
    # Estamos dizendo:
    #
    # "O corpo (body) dessa requisição deve seguir
    #  o modelo UserCreate."
    #
    # O Pydantic irá validar automaticamente os dados.
    #
    # Esperamos algo como:
    #
    # {
    #     "name": "Adul Balde",
    #     "email": "adul@example.com"
    # }
    #
    # Se os dados estiverem errados, o FastAPI retorna
    # automaticamente um erro de validação.

    # Retornamos o objeto UserCreate.
    #
    # O FastAPI transforma o modelo Pydantic em JSON
    # para enviar a resposta ao cliente.