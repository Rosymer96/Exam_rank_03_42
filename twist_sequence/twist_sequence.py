def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return []
    if k > len(arr):
        k = k % len(arr)
    ini = arr[-k:]
    fin = arr[:-k]
    return ini + fin 
