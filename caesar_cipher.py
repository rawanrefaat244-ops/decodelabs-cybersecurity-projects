def encrypt(text, shift):
    """
    Encrypts the input text using Caesar Cipher with the given shift.
    Keeps spaces and puncruation unchanged.
    """
    result = ""
    for char in text:
        if char.isupper():     # Upper Letters
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():   # Lower Letters
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:                  # Non-alphabetic characters (punctuation, space)
            result += char
    return result


def decrypt(text, shift):
    """
    Decrypts the input text using Caesar Cipher with the given shift.
    """
    return encrypt(text, -shift)


# ===== Example Usage =====
if __name__ == "__main__":
    plaintext = "Hello World!"
    shift_key = 3

    ciphertext = encrypt(plaintext, shift_key)
    print("Encrypted:", ciphertext)

    decrypted_text = decrypt(ciphertext, shift_key)
    print("Decrypted:", decrypted_text)