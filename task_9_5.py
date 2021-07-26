class Stationery:
    """Класс Stationery (канцелярская принадлежность).

    """
    title = ''

    def draw(self):
        print('Start drawing')
        print("It's ", self.__class__.__name__, "'s draw method")


class Pen(Stationery):

    def draw(self):
        print("It's ", self.__class__.__name__, "'s draw method")


class Pencil(Stationery):

    def draw(self):
        print("It's ", self.__class__.__name__, "'s draw method")


class Handle(Stationery):

    def draw(self):
        print("It's", self.__class__.__name__, "'s draw method")


ink_pen = Pen()
color_pencil = Pencil()
a_handle = Handle()

for ob in (ink_pen, color_pencil, a_handle):
    ob.draw()