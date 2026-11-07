def anagram(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False
 
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    print(anagram("elbow", "below"))
    print(anagram("night", "thing"))
    print(anagram("apple", "grape"))
    print(anagram("", ""))
    print(anagram("abcd", "abc"))
