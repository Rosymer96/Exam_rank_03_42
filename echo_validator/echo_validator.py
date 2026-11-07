def echo_validator(text: str) -> bool:
    if not text:
        return False
    text = text.lower()
    return text.replace(" ", "") == text[::-1].replace(" ", "")
