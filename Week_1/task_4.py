from itertools import combinations

def bananas(s: str) -> set:
    """
    возвращает множество вхождений слова «banana» в строке
    """
    base_word = "banana"
    len_bw = len(base_word)
    clear_s = '-' * len(s)
    result = set()
    for combination in combinations(enumerate(s), len_bw):
        cur_word = list(clear_s)
        i = 0
        for j, let in combination:
            if let == base_word[i]:
                cur_word[j] = let
                i += 1
            else:
                break
        if i == len_bw:
            result.add(''.join(cur_word))
    return result

assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
