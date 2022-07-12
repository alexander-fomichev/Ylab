В основе SOLID — пять универсальных и применимых к любому ООП-языку принципов. Все они направлены на то, чтобы привести ваш код к слабой связанности и сильной связности.

####1 Single Responsibility — принцип единственной ответственности.
Метод `create_news` перенесен из класса `SuperHero` в новый класс `MassMedia`
####2 Open-Closed — принцип открытости/закрытости.
Класс `SuperHero` преобразован в абстрактный. Создание супергероя `Чак Норрис` происходит из нового класса `TexasRanger` 
####3 Liskov Substitution — принцип подстановки Барбары Лисков.
В метод `attack` класса `Superman` добавлена функция `print` в соответствии с классом Superhero 
####4 Interface Segregation — принцип разделения интерфейса.
Методы `roundhouse_kick`, `fire_a_gun` и `incinerate_with_lasers` класса `SuperHero` вынесены в отдельные классы `MartialArt`, `Gunnery` и `KryptonPower`
####5 Dependency Inversion — принцип инверсии зависимостей.
Для упрощения логики удален класс `AntagonistFinder`. В методе `find` класса `Superhero` происходит обращение к методу `get_antagonist` класса `Place`



