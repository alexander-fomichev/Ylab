from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """
        Метод генератор возвращает дни в которые показывают фильм
        """
        for period in self.dates:
            date = period[0]
            while date <= period[1]:
                yield date
                date += timedelta(days=1)


if __name__ == "__main__":
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
