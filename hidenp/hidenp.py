def hidenp(small: str, big: str) -> bool:
    i = 0
    for c in big:
        if i < len(small) and c == small[i]:
            i += 1
    return i == len(small)

if __name__ == "__main__":
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "xyz"))
    print(hidenp("sing", "subsequence testing"))