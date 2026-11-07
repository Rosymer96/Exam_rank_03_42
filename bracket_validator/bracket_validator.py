def bracket_validator(s: str) -> bool:
    dic = {")": "(", "]": "[", "}": "{"}
    brackets = []

    for c in s:
        if c in "({[":
            brackets.append(c)
        elif c in "]})" and brackets:
            if brackets.pop() != dic[c]:
                return False
        elif c in "]})" and not brackets:
            return False

    return len(brackets) == 0


if __name__ == "__main__":
    print(bracket_validator("{[()]}"))
    print(bracket_validator("([)]"))
    print(bracket_validator("func(a, [b, c])"))
    print(bracket_validator("(()"))
    print(bracket_validator(""))
    print(bracket_validator("}"))