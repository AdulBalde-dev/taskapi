from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# ============================================================
# CONFIGURAÇÃO DO BANCO
# ============================================================

# URL de conexão com o banco SQLite.
#
# O banco será armazenado no arquivo:
#
# mytasks.db
#
# na pasta onde a aplicação for executada.
DATABASE_URL = "sqlite:///./mytasks.db"


# ============================================================
# ENGINE
# ============================================================

# O engine é responsável pela comunicação
# entre nossa aplicação Python e o banco.
engine = create_engine(
    DATABASE_URL,
    
    # SQLite possui uma particularidade relacionada
    # ao uso da conexão em diferentes threads.
    #
    # Para nossa aplicação FastAPI, precisamos permitir isso.
    connect_args={"check_same_thread": False}
)


# ============================================================
# SESSION
# ============================================================

# SessionLocal será utilizado para criar sessões
# de comunicação com o banco.
#
# Através de uma sessão poderemos:
#
# - consultar dados
# - inserir dados
# - atualizar dados
# - excluir dados
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)


# ============================================================
# BASE DOS MODELOS
# ============================================================

# Todos os nossos modelos SQLAlchemy irão herdar de Base.
#
# Exemplos futuros:
#
# class User(Base):
#     ...
#
# class Task(Base):
#     ...
class Base(DeclarativeBase):
    pass