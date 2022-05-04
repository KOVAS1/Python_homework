'''
4. Начать работу над проектом «Склад оргтехники». 
    Создать класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников. 
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
    В базовом классе определить параметры, общие для приведённых типов. 
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class Warehouse:
    """Класс, описывающий склад оргтехники"""
    print("Склад оргтехники:\n")


class OfficeEquipment:
    """Базовый класс оргтехники"""

    def __init__(self, producer, model, country, year, price, color):
        self.producer = producer
        self.model = model
        self.country = country
        self.year = year
        self.price = price
        self.color = color


class Printer(OfficeEquipment):
    """Класс принтер"""
    amount_pr = 0

    def __init__(self, producer, model,  country, year, price, color, pr_type):
        super().__init__(producer, model, country, year, price, color)
        self.pr_type = pr_type

        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "\tКатегория-Принтер:"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return f"Модель: {self.producer} {self.model},\tВыпуск:{self.year}, {self.country},\tЦена:{self.price}₽,\tЦвет: {self.color},\tТип: {self.pr_type}"


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

    def __init__(self, producer, model, country, year, price, color,  sc_sensor):
        super().__init__(producer, model, country, year, price, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"\n\tКатегория-Сканер:"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return f"Модель: {self.producer} {self.model}, \tВыпуск: {self.year}, {self.country}, \tЦена: {self.price}₽, \tЦвет: {self.color}, \tТип сенсора: {self.sc_sensor}"


class Xerox(OfficeEquipment):
    """Класс ксерокс"""
    amount_x = 0

    def __init__(self, producer, model, country, year, price, color, xer_wi_fi):
        super().__init__(producer, model,  country, year, price, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "\n\tКатегория-Ксерокс:"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return f"Модель: {self.producer} {self.model},\tВыпуск:{self.year}, {self.country},\tЦена:{self.price}₽,\tЦвет: {self.color},\tWi-Fi: {self.xer_wi_fi}"


p = Printer('HP', 'OfficeJet Pro 8210', 'China',
            2020, 10311, 'white', 'струйный')
p2 = Printer('Brother', 'HL-1223WR', 'Japan', 2021, 16890, 'blue', 'лазерный')
print(p.name(), p.amount_pr, "ед.")
print(p.__str__())
print(p2.__str__())


s = Scanner('Epson', 'DS-310', 'Japan', 2019, 31700, 'black', 'CIS')
s2 = Scanner('Avision', 'AV186', 'Taiwan', 2020, 1995, 'white', 'CCD')
s3 = Scanner('AVE', 'PS1001', 'China', 2021, 32345, 'blue', 'CMOS')
print(s.name(), s.amount_sc, "ед.")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())


x = Xerox('Pantum', ' M6500', 'China', 2019, 13026, 'black', 'нет')
x2 = Xerox('Sharp', 'AR-7024', 'Japan', 2020, 58981, 'white', 'н.д.')
x3 = Xerox('Xerox', ' B215', 'Germany', 2019, 38779, 'white', 'да')
x4 = Xerox('Ricoh', 'IM 2702', 'China', 2022, 177200, 'grey', 'да')
print(x.name(), x.amount_x, "ед.")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())
