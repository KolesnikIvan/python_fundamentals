from decimal import Decimal


class Worker:
    """Базовый класс Worker (работник).
    
    Атрибуты: name, surname, position (должность), income (доход).
    """
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0.0, 'bonus': 0.0}

    def __init__(self):
        self.name = str(input('Type worker\'s name: ')).capitalize()
        self.surname = str(input('Type surname: ')).capitalize()
        self._income = {'wage': Decimal(input(f'Insert {self.name}\'s wage: ')),
                        'bonus': Decimal(int(input('Insert bonus: '))/100)}


class Position(Worker):
    """Класс Position (должность) наследует класса Worker."""
    def get_full_name(self):
        """Возвращает полное имя сотрудника"""
        full_name = self.surname + ' ' + self.name
        print('Worker\'s name is', full_name)
        return full_name

    def get_total_income(self):
        """Возвращает доход с уччетом премии"""
        total_income = self._income['wage'] * self._income['bonus']
        print('Total income of ', self.get_full_name(), ' is ', total_income)
        return total_income


a = Position()
print(a.get_full_name())
print(a.get_total_income())
