def zeros(n: int):
    """
    возвращает количество конечных нулей в факториале числа n
    """
    res = 0
    while n:
        n //= 5
        res += n
    return res

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
