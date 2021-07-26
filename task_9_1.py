import os
import random
import time
from termcolor import cprint


class TrafficLight:
    """Класс TrafficLight (светофор).

    Атрибут color (цвет).
    Метод running (запуск).
    """
    __color = ''

    def __init__(self):
        # инициализация полей
        self.duration = {'red': 7, 'yellow': 2, 'green': int(input('Insert green light duration: '))}
        self.test_sequence = ['red', 'yellow', 'green']
        # сфетофор инициализируется случайным элементом последовательности сигналов
        self.__color = random.choice(self.test_sequence)
        print('color', self.__color)

    # def __next_light(self, sequence)
    #     for clr in sequence:
    #         yield clr

    def running(self, sequence):
        sequence = list(sequence)
        if len(sequence) != 3:
            raise ValueError('Sequence must have three elements.')
        if self.__sequence_checker(sequence):
            while True:
                os.system('cls')  # хотел очистить консоль для вывода
                # определяется порядковый номер сигнала
                signal_num = sequence.index(self.__color)
                interval = self.duration[self.__color]  # определяется соответствующая длительность сигнала
                # print(self.__color)
                cprint(self.__color.ljust(6), 'white', 'on_' + self.__color)
                time.sleep(interval)  # задержка выполнения на соответствующее сигналу время
                # дойдя до конца последовательности, начинаем с начала; иначе берем следующий элемент
                self.__color = sequence[0] if signal_num == len(sequence) - 1 else sequence[signal_num + 1]

    def __sequence_checker(self, sequence):
        """Проверка правильнос последовательности. Сопоставление с хардкодной."""
        for light in sequence:
            if sequence[sequence.index(light) - 1] != self.test_sequence[self.test_sequence.index(light) - 1]:
                raise ValueError('Wrong light sequence')
                # return False
        return True


tl = TrafficLight()
tl.running(('red', 'yellow', 'green'))
