def int32_to_ip(int32: int):
    """
    Возвращает строковое значение ip адреса из 4-х байтного числа
    """
    res = [str((int32 >> i * 8) & 0xff) for i in range(4)]
    return '.'.join(res[::-1])


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"