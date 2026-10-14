import hashlib
def sha1_hash_string(input_string: str) -> str:
    """
    Returns the SHA-1 hash of a given string.
    """
    return hashlib.sha1(input_string.encode()).hexdigest()
if __name__ == "__main__":
    text = "hello world"
    print(f"SHA-1 hash of '{text}': {sha1_hash_string(text)}")