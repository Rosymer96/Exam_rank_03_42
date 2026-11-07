def whisper_cipher(text: str, shift: int) -> str:
    new_text = ""
    for c in text:
        if c.islower():
            new_text += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif c.isupper():
            new_text += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_text += c
    return new_text