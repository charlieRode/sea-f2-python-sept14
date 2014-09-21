import string

def rot13(str):
    """Return rot13 encryption of str"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_alphabet = alphabet.lower()
    encrypted_alphabet = alphabet[13:] + alphabet[0:13]
    encrypted_lowercase_alphabet = encrypted_alphabet.lower()
    encryption = string.maketrans(alphabet + lowercase_alphabet, encrypted_alphabet + encrypted_lowercase_alphabet)
    return str.translate(encryption)

