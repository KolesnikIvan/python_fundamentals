class Car:
    """Базовый класс Car.

    Атрибуты: speed, color, name, is_police (boolean).
    Методы: go, stop, turn(direction).

    """
    is_police = False

    def __init__(self, color, name):
        self.speed = 0.0
        self.color = color
        self.name = name

    def go(self, speed):
        self.speed = speed
        print('Car goes.')

    def stop(self):
        self.speed = 0
        print('Car stopped.')

    def turn(self, direction):
        print(f'Car has turned {direction}')


class TownCar(Car):
    speed = 120
    color = 'white'
    name = 'VAZ'
    is_police = False

    def show_speed(self):
        print('speed is ', self.speed, 'km/h.', ('WARNING: speed is too high' if self.speed > 60 else ''))


class SportCar(Car):
    speed = 200
    color = 'red'
    name = 'Ferrari'
    is_police = False


class WorkCar(Car):
    speed = 70
    color = 'orange'
    name = 'KAMAZ'
    is_police = False

    def show_speed(self):
        print('speed is ', self.speed, 'km/h.', ('WARNING: speed is too high' if self.speed > 40 else ''))


class PoliceCar(Car):
    speed = 150
    color = 'blue'
    name = 'Volga'
    is_police = True


passenger_car = TownCar('white', 'VAZ')
bolide = SportCar('red', 'Ferrari')
truck = WorkCar('orange', 'KAMAZ')
dps = PoliceCar('blue', 'Volga')


print(*map(dir, (passenger_car, bolide, truck, dps)), sep='\n')
# lst = [cl.attr for cl in (passenger_car, bolide, truck, dps) for attr in dir(cl) if not attr.startswith("_")]
# print(*lst, sep='\n')
# print(*[attr for attr in dir(TownCar) if not attr.startswith('_')], sep='\n')
for ob in (passenger_car, bolide, truck, dps):
    print(*[str(ob)+'.'+str(attr) for attr in dir(ob) if not attr.startswith('_')], sep='\n')

passenger_car.go(70)
passenger_car.show_speed()
truck.go(75)
truck.show_speed()
# как сдедалть, чтобы скорость проверялась не в методе go,
# а в обработчике событий что ли?
# а то вдруг она будет изменена не только в этом методе, а и где-то еще
# можно событие изменение скорости связать с классом?
