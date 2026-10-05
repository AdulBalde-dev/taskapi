from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class User(Base):
    """
    Modelo SQLAlchemy que representa a tabela 'users'
    no banco de dados.
    """

    __tablename__ = "users"

    # Chave primária do usuário.
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # Nome do usuário.
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Email do usuário.
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )