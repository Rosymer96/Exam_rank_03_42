def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (1 < from_base < 37 and 1 < to_base < 37 and number):
        return "ERROR"

    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sign = ""
    res = ""
    dec = 0
    if number[0] == "-":
        sign = "-"
        number = number[1:]

    for c in number:
        if c not in base[:from_base]:
            return "ERROR"
        dec = dec * from_base + base.index(c)

    if dec == 0:
        return "0"

    while dec > 0:
        res = base[dec % to_base] + res
        dec //= to_base
    
    return sign + res 


if __name__ == "__main__":
    print(number_base_converter("111", 2, 10))
    print(number_base_converter("A0", 16, 10))
    print(number_base_converter("160", 10, 16))
    print(number_base_converter("100", 10, 2))
    print(number_base_converter("Y", 36, 10))
    print(number_base_converter("34", 10, 36))
    print(number_base_converter("12", 1, 10))
    print(number_base_converter("H", 16, 10))
    print(number_base_converter("-", 16, 10))