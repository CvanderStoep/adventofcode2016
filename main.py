import time
import random
import sys

def decrypt_animation(encrypted_text, decrypted_text):
    # Clear the output
    def clear_output():
        sys.stdout.write('\r' + ' ' * len(encrypted_text) + '\r')

    # Create a pool of possible characters
    pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for i in range(len(decrypted_text)):
        for _ in range(10):  # Simulate multiple attempts
            clear_output()
            # Randomly replace each character with a character from the pool
            intermediate_text = encrypted_text[:i] + ''.join(random.choice(pool) for _ in range(len(decrypted_text) - i))
            sys.stdout.write(intermediate_text)
            sys.stdout.flush()
            time.sleep(0.05)

        # Set the correct character at position i
        encrypted_text = encrypted_text[:i] + decrypted_text[i] + encrypted_text[i + 1:]
        clear_output()
        sys.stdout.write(encrypted_text)
        sys.stdout.flush()
        time.sleep(0.1)

    print("\nDecryption Complete!")

# Example usage
encrypted_text = "????????"
decrypted_text = "999828ec"
decrypt_animation(encrypted_text, decrypted_text)
