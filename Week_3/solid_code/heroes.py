from abc import ABC


class MartialArt(ABC):
    def roundhouse_kick(self):
        print('Bump')


class Gunnery(ABC):
    def fire_a_gun(self):
        print('PIU PIU')


class KryptonPower(ABC):
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    def find(self, place):
        place.get_antagonist()

    def attack(self):
        pass

    def ultimate(self):
        pass


class Superman(SuperHero, KryptonPower):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        return print('Kick')

    def ultimate(self):
        self.incinerate_with_lasers()


class TexasRanger(SuperHero, MartialArt, Gunnery):

    def attack(self):
        return self.fire_a_gun()
