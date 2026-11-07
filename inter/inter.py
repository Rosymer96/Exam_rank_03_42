def inter(s1: str, s2: str) -> str:
    res = ""

    for c in s1:
        if c in s2 and c not in res:
            res += c

    return res