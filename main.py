def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-letter characters are added as-is
    return ''.join(encrypted_text)

# Example usage
plaintext = "hello-world"
shift = 3
encrypted = caesar_encrypt(plaintext, shift)
print("Encrypted:", encrypted)
