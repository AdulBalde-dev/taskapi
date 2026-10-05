from pwdlib import PasswordHash


# Cria o objeto responsável por criar e verificar hashes.
password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Recebe uma password normal e devolve o seu hash.

    A password original nunca deve ser guardada na base de dados.
    """
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifica se a password fornecida corresponde ao hash guardado.

    Retorna:
        True  -> password correta
        False -> password incorreta
    """
    return password_hash.verify(password, hashed_password)