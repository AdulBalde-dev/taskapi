from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Dados necessários para criar um usuário.
    """

    name: str
    email: str