import re


def domain_name(url: str):
    """
    Возвращает домен из строки url
    """
    res = re.search(r"^(?:https?://|)(?:www\.|)(?P<domain>[\w-]+).*", url)
    return res.group('domain')


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"