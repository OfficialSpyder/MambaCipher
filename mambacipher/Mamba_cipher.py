"""
MambaCipher: A Custom Proprietary Encryption & Encoding System.
Designed for secure tokenization, signature verification, and custom obfuscation.
Author: Sukhpal Kherera
"""

import sys

# Digit to Special Symbol Mapping
DIGIT_TO_SYMBOL = {
    '0': ')',
    '1': '!',
    '2': '@',
    '3': '#',
    '4': '$',
    '5': '%',
    '6': '^',
    '7': '&',
    '8': '*',
    '9': '('
}

# Reverse mapping for decoding symbols back to digits
SYMBOL_TO_DIGIT = {v: k for k, v in DIGIT_TO_SYMBOL.items()}

def encrypt(text: str) -> str:
    """Encodes standard plain text into MambaCipher format."""
    encoded_chars = []
    for char in text:
        if char.isdigit():
            encoded_chars.append(DIGIT_TO_SYMBOL[char])
        elif char.islower():
            pos = ord(char) - ord('a') + 1
            encoded_chars.append(f"<{pos}>")
        elif char.isupper():
            pos = ord(char) - ord('A') + 1
            encoded_chars.append(f"[{pos}]")
        else:
            encoded_chars.append(char)
    return "".join(encoded_chars)

def decrypt(encoded_text: str) -> str:
    """Decodes MambaCipher encoded text back into original plain text."""
    decoded_chars = []
    i = 0
    length = len(encoded_text)
    
    while i < length:
        char = encoded_text[i]
        if char in SYMBOL_TO_DIGIT:
            decoded_chars.append(SYMBOL_TO_DIGIT[char])
            i += 1
        elif char == '<':
            end_idx = encoded_text.find('>', i)
            if end_idx != -1:
                pos = int(encoded_text[i+1:end_idx])
                decoded_chars.append(chr(ord('a') + pos - 1))
                i = end_idx + 1
            else:
                i += 1
        elif char == '[':
            end_idx = encoded_text.find(']', i)
            if end_idx != -1:
                pos = int(encoded_text[i+1:end_idx])
                decoded_chars.append(chr(ord('A') + pos - 1))
                i = end_idx + 1
            else:
                i += 1
        else:
            decoded_chars.append(char)
            i += 1
            
    return "".join(decoded_chars)

# Interactive CLI & User Input Handler
if __name__ == "__main__":
    print("=========================================")
    print("      MAMBACIPHER SECURITY MODULE        ")
    print("=========================================")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    choice = input("Select an option (1 or 2): ").strip()
    
    if choice == '1':
        user_input = input("\nEnter text to encrypt: ")
        result = encrypt(user_input)
        print(f"\n[Encrypted Output]:\n{result}")
    elif choice == '2':
        user_input = input("\nEnter text to decrypt: ")
        result = decrypt(user_input)
        print(f"\n[Decrypted Output]:\n{result}")
    else:
        print("\nInvalid choice! Please run the script again.")
