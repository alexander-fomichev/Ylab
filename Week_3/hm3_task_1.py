def cash_result(func):
    """
    функция-декоратор сохраняет (кэширует) результат декорируемой функции
    """
    results = {}

    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]

    return wrapper


@cash_result
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    [print(multiplier(i)) for i in range(5)]
    [print(multiplier(i)) for i in range(5)]
