import redis


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


def cash_redis(func):
    """
    функция-декоратор сохраняет (кэширует) результат декорируемой функции
    """

    def wrapper(*args):
        if redis_client.exists(str(*args)):
            res = int(redis_client.get(name=str(*args)))
        else:
            res = func(*args)
            redis_client.set(name=str(*args), value=res)
        return res

    return wrapper


@cash_redis
def multiplier2(number: int):
    return number * 2


if __name__ == "__main__":
    [print(multiplier(i)) for i in range(5)]
    [print(multiplier(i)) for i in range(5)]

    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    [print(multiplier2(i)) for i in range(5)]
    [print(multiplier2(i)) for i in range(5)]
    redis_client.close()
