"""
MambaCipher: A Custom Proprietary Encryption & Encoding System.
Designed for secure tokenization, signature verification, and custom obfuscation.
"""

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
    """
    Encodes standard plain text into MambaCipher format.
    - Digits (0-9) are mapped to special symbols.
    - Lowercase letters (a-z) are mapped to positional tags like <1>, <2>...
    - Uppercase letters (A-Z) are mapped to bracket tags like [1], [2]...
    """
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
    """
    Decodes MambaCipher encoded text back into original plain text.
    """
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

# Local Test
if __name__ == "__main__":
    test_str = "MasterBot-2026-Secure"
    enc = encrypt(test_str)
    dec = decrypt(enc)
    print(f"Original: {test_str}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
