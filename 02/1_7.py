import hashlib
def sha256_hash_string(input_string: str) -> str:
    """
    Returns the SHA-256 hash of a given string.
    """
    return hashlib.sha256(input_string.encode())
if __name__ == "__main__":
    text = "hello world"
    print(f"SHA-256 hash of '{text}': {sha256_hash_string(text)}")