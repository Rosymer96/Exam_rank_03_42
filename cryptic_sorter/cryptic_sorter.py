def cryptic_sorter(strings: list[str]) -> list[str]:
    result = strings[:]

    def get_key(s: str) -> tuple:
        vocals = 0
        s = s.lower()
        for c in s:
            if c in "aeiou":
                vocals += 1
        return len(s), s, vocals

    for c in result:
        for i in range(len(result) - 1):
            if get_key(result[i]) > get_key(result[i + 1]):
                result[i], result[i+1] = result[i+1], result[i]

    return result

if __name__ == "__main__":
    print(cryptic_sorter(["banana", "kiwi", "fig", "grape", "date"]))
    print(cryptic_sorter(["ccc", "AAA", "bbb", "aaa"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))



