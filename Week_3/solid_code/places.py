from abc import ABC, abstractmethod, abstractproperty
from typing import List


class Place(ABC):
    @abstractmethod
    def get_antagonist(self):
        pass

    @abstractmethod
    def get_location(self):
        pass


class City(Place, ABC):

    name: str

    def get_location(self):
        return self.name


class Planet(Place, ABC):

    coordinates: List[float] = []

    def get_location(self):
        return self.coordinates


class Kostroma(City):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(City):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
