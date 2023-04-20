import dataclasses #встроенная аналогия структур
import enum #перечисление
import operator

class Cloudiness(enum.Enum):
    rainy = enum.auto()
    cloudy = enum.auto()
    sunny = enum.auto()

@dataclasses.dataclass
class DayForecast:
    day: int
    cloudiness: Cloudiness
    wind: float
    temperature: float

@dataclasses.dataclass
class PicnicDay:
    day: int
    comfort_temperature: int # округлить до целых стандартной функцией round(...)

@dataclasses.dataclass
class Test:
    day: int
    cloudiness: Cloudiness
    comfort_temperature: float

forecast: list[DayForecast] = []
days = []
test: list[Test] = []

for i in forecast:
    comfort_temperature = i.temperature - (i.wind * 1.5) + 5 * (i.cloudiness == Cloudiness.sunny)
    if i.cloudiness != Cloudiness.rainy and comfort_temperature >= 15:
        test  += [Test(i.day, i.cloudiness, comfort_temperature)]

test.sort(key = operator.attrgetter('comfort_temperature'), reverse = True)

days = [PicnicDay(i.day, round(i.comfort_temperature)) for i in test]

