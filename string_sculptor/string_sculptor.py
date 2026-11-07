def string_sculptor(text: str) -> str:
    new_text = ""
    count = 0

    for c in text:
        if c.isalpha():
            if count % 2 == 0:
                new_text += c.lower()
            else:
                new_text += c.upper()
            count += 1
        else:
            new_text += c
        if c == " ":
            count = 0

    return new_text

