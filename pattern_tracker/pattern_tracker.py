def pattern_tracker(text: str) -> int:
    count = 0

    for i, c in enumerate(text, start=1):
        if i < len(text):
            if c.isdigit() and text[i].isdigit() and c < text[i]:
                count += 1

    return count


if __name__ == "__main__":
    print(pattern_tracker("456"))
    print(pattern_tracker("45a67"))
    print(pattern_tracker("999888777"))
    print(pattern_tracker("0123456789"))
    print(pattern_tracker("xyz"))
