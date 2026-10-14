import bcrypt
import sys

def bcrypt_hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def bcrypt_verify_password(password: str, hashed: str) -> bool:
    """
    Verify a password against a bcrypt hash.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Example usage
if __name__ == "__main__":
    pwd = sys.argv[1]

    # Generowanie hasha
    hashed_pwd = bcrypt_hash_password(pwd)
    print(f"Wygenerowany hash: {hashed_pwd}")

    # Weryfikacja
    is_valid = bcrypt_verify_password(pwd, hashed_pwd)
    print(f"Czy hasło jest poprawne: {is_valid}")
