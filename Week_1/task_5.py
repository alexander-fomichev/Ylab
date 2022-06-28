from functools import reduce
def count_find_num(primesL, limit):
    """
    генерирует список чисел меньших значения limit, которые имеют все и только простые множители простых чисел primesL
    возвращает количество таких чисел и наибольшее из них
    """
    primesL.sort()
    res = []
    base_num = reduce(lambda a, b: a * b, primesL)
    if base_num > limit:
        return []
    res.append(base_num)
    for prime in primesL:
        for num in res:
            cur_num = num * prime
            while cur_num <= limit and cur_num not in res:
                res.append(cur_num)
                cur_num *= prime

    return([len(res), max(res)])


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
