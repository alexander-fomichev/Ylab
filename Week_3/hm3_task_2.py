import time
from functools import wraps


def repeat(call_count: int, start_sleep_time: int, factor: int, border_sleep_time: int):
    """
    Декоратор для повторного выполнения декорируемой функции через некоторое время.
    Использует наивный экспоненциальный рост времени повтора (factor) до граничного времени ожидания (border_sleep_time)

    :param call_count:int - число, описывающее кол-во запуска функции;
    :param start_sleep_time: - начальное время повтора;
    :param factor: - во сколько раз нужно увеличить время ожидания;
    :param border_sleep_time: - граничное время ожидания.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Начало работы")
            exec_count = 0
            sleep_time = start_sleep_time
            while exec_count < call_count:
                sleep_time = sleep_time if sleep_time < border_sleep_time else border_sleep_time
                exec_count += 1
                time.sleep(sleep_time)
                res = func(*args, **kwargs)
                print(
                    f"Запуск номер {exec_count}. Ожидание: {sleep_time} секунд. Результат декорируемой функций = {res}."
                )
                sleep_time *= factor
            print("Конец работы")
            return

        return wrapper

    return decorator


@repeat(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=60)
def multiplier():
    return time.time()


if __name__ == "__main__":
    multiplier()
