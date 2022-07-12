class MassMedia:

    def create_news(self, hero, place):
        place_location = place.get_location()
        result = f'{hero.name} saved the {place_location}!'
        if hasattr(self, 'name'):
            result = f'{self.name}: ' + result
        print(result)


class TV(MassMedia):
    name: str = 'TV'


class Radio(MassMedia):
    name: str = 'Radio'
