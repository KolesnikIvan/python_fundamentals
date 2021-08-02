import random
import string


class OfficeTechnic:
    """Класс «Оргтехника», базовый для классов-наследников (принтер, сканер, ксерокс).

    Общие параметры тиы, имя, объем, цена.
    В классах-наследниках реализоваyd уникальные для каждого типа параметры.
    """
    def __init__(self, ttype, name, length, width, height, weight, cost):
        if not self.validator(ttype):
            raise TypeError('недопустимый класс')
        self.ttype = str(ttype)
        self.name = name
        self.volume = float(length) * float(width) * float(height)
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return self.ttype + ' ' + self.name

    @staticmethod
    def validator(ttype):
        valid_types = ('computer', 'printer', 'plotter', 'xerox')
        if ttype in valid_types:
            return True
        return False


class Warehouse:
    """Класс, описывающий склад."""
    def __init__(self, length, width, height):
        self.__capacity = int(length) * int(width) * int(height)
        self.__free_volume = self.capacity
        self.occupied_volume = 0
        self.stock_list = []  # список хранения

    def accept_item_to_store(self, technic):
        """Прием на хранение оргтехники по списку"""
        if self.occupied_volume + technic.volume <= self.capacity:
            self.stock_list.append(technic)
            self.occupied_volume += technic.volume
            self.__free_volume -= technic.volume
        else:
            print('Предмету ', technic.ttype, ' не хватает места на складе.')

    def dispatch(self, ttype, num):
        """Отправка num единиц обрудования типа ttype.

        Если на складе нет заправшиваемого оборудования
        в нужном количестве, то выводится сообщение."""
        for obj in self.stock_list:
            if obj.ttype == ttype:
                self.stock_list.pop(self.stock_list.index(obj))
                num -= 1
                if num == 0:
                    print('Со склада отправлено', num, 'единиц оборудования типа', ttype)
                    break
        if num:
            print('На складе не хватает ', num, 'единиц обрудования ', ttype, 'для удовлетворения запроса.')

    @property
    def free_volume(self):
        return self.__capacity - self.occupied_volume

    @free_volume.setter
    def free_volume(self, value):
        # я хочу просто отслеживать свободное место,
        # поэтому не использую value
        # допустимо это?
        self.free_volume = self.capacity - self.occupied_volume

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def total_of_stored_goods(self, value):
        # Находится суммарный показатель
        total = 0
        for obj in self.stock_list:
            total += getattr(obj, value)
        return 'total of ' + value + ' is ' + str(total)

    def heaviest_subject(self):
        nam = ''
        mx = 0
        for obj in self.stock_list:
            nam = obj.name if obj.weight / obj.volume > mx else nam
            mx = obj.weight / obj.volume if obj.weight / obj.volume > mx else mx
        return 'The heaviest object is ' + nam


class Computer(OfficeTechnic):

    def __init__(self, name, ln,  wd, hg, wg, price, cpu=2):
        super().__init__('computer', name, ln, wd, hg, wg, price)
        self.cpu_freq = cpu


class Printer(OfficeTechnic):

    def __init__(self, name, ln, wd, hg, wg, price, dpi=200, is_color=False):
        super().__init__('printer', name, ln, wd, hg, wg, price)
        self.dpi = dpi
        self.is_color = is_color


class Plotter(OfficeTechnic):

    def __init__(self, name,  ln, wd, hg, wg, price, width=1000):
        super().__init__('plotter', name, ln, wd, hg, wg, price)
        self.plot_width = width


class Xerox(OfficeTechnic):

    def __init__(self, name, ln, wd, hg, wg, price, label='HP', has_scaner=True):
        super().__init__('xerox', name, ln, wd, hg, wg, price)
        self.label = label
        self.has_scaner = has_scaner


# формируется склад случайного размера (в м)
l_w = random.randint(5, 6)
w_w = random.randint(3, 6)
h_w = random.randint(2, 4)
wh = Warehouse(l_w, w_w, h_w)
print(wh.capacity)

# склад заполняется случайными видами техники
# со случайными параметрами (размерами и весами)
num_of_tech = random.randrange(5, 50)
for i in range(num_of_tech):
    tp = random.choice(('computer', 'printer', 'plotter', 'xerox'))
    nm = ''.join(random.sample(string.ascii_letters, 3))
    lng = random.randint(20, 150) / 100
    wdt = random.randint(20, 150) / 100
    hgh = random.randint(20, 150) / 100
    wgt = random.randint(2, 15)
    prc = random.randint(4, 150) * 1000
    # формируется строка передачи параметров создаваемому объекту техники
    string_to_create_stored_class = tp.capitalize() + '(' + \
        '"' + nm + '", ' + str(lng) + ', ' + str(wdt) + ', ' + \
        str(hgh) + ', ' + str(wgt) + ', ' + str(prc) + ')'
    equip = eval(string_to_create_stored_class)
    wh.accept_item_to_store(equip)
    print(wh.free_volume)

print(wh.stock_list)
print(wh.occupied_volume, wh.free_volume, wh.capacity)

print(wh.heaviest_subject())

for _ in range(5):
    wh.accept_item_to_store(Plotter('pl', 200, 70, 120, 10, 80000))

wh.dispatch('plotter', 3)
print(wh.occupied_volume, wh.free_volume, wh.capacity)
# print(wh.stock_list)
for obj in wh.stock_list:
    print(obj)
wh.dispatch('plotter', 10)
print(wh.occupied_volume, wh.free_volume, wh.capacity)

print(wh.total_of_stored_goods('cost'))  # суммарная стоимость товаров на складе
