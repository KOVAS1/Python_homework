'''
4. Реализуйте базовый класс Car:

    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
    также методы: go, stop, turn(direction), которые должны сообщать, что машина
    поехала, остановилась, повернула (куда);
    
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую
    скорость автомобиля;
    
    ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
    скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
    превышении скорости.
    
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала.'

    def stop(self):
        return f'\nМашина {self.name} остановилась.'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость {self.speed}. Это выше, чем разрешено!'
        else:
            return f'Скорость {self.name} нормальная'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВаша скорость {self.speed}. Это выше, чем разрешено!'
        else:
            return f'Скорость {self.name} нормальная'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 65, 'blue', False)
print('1:' + town.go(), town.show_speed(),
      town.turn('налево'), town.turn('направо'), town.stop(), '\n')

sport = SportCar('Jaguar_XK', 120, 'red', False)
print('2:' + sport.go(), sport.show_speed(),
      sport.turn('налево'), sport.stop(), '\n')

work = WorkCar('MAZ', 50, 'red', False)
print('3:' + work.go(), work.show_speed(),
      work.turn('направо'), work.stop(), '\n')

work = WorkCar('MAZ', 39, 'red', False)
print('4:' + work.go(), work.show_speed(),
      work.turn('налево'), work.stop(), '\n')

police = PoliceCar('Porsche_911', 180, 'yellow', True)
print('5:' + police.go(), police.show_speed(),
      police.turn('направо'), police.stop())
