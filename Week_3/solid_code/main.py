from heroes import Superman, SuperHero, TexasRanger
from places import Place, Kostroma, Tokyo
from massmedias import MassMedia, TV, Radio


def save_the_place(hero: SuperHero, place: Place, massmedia: MassMedia = TV()):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    massmedia.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(TexasRanger('Chack Norris', False), Tokyo(), Radio())

