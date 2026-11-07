def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for list in matrix:
        new_matrix.append(list[::-1])

    return new_matrix

if __name__ == "__main__":
    # examples from the statement
    print(mirror_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(mirror_matrix([[9]]))
    print(mirror_matrix([[1, -2, 3, -4]]))

    # extra cases
    print(mirror_matrix([[1], [2], [3]]))        # single column
    print(mirror_matrix([[1, 2], [3, 4]]))       # 2x2
    print(mirror_matrix([[1, 2, 1], [5, 5, 5]])) # palindromic rows
    print(mirror_matrix([[1, 2], [3]]))          # rows of different length
    print(mirror_matrix([[0, -1, 0]]))           # zeros and negatives
    print(mirror_matrix([]))                     # empty matrix
    print(mirror_matrix([[]]))                   # one empty row

    # the input must not be modified
    original = [[1, 2, 3], [4, 5, 6]]
    result = mirror_matrix(original)
    print(original)                              # must stay unchanged
    print(result is original)                    # must be False
    print(result[0] is original[0])              # must be False