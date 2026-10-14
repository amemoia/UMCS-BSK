import hashlib
def md5_hash_string(input_string: str) -> str:
    """
    Returns the MD5 hash of a given string.
    """
    return hashlib.md5(input_string.encode()).hexdigest()
if __name__ == "__main__":
    text = "hello world"
    print(f"MD5 hash of '{text}': {md5_hash_string(text)}")