class Road:
    """Класс Road (дорога).

    Атрибуты: _length (длина), _width (ширина) передаются при создании;
    метод asphalt_mass возвращает массу асфальта для покрытия всей дороги.

    """
    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_mass(self, thickness, density):
        return self._length * self._width * thickness * density


r1 = Road(5000, 20)
print(r1.asphalt_mass(0.1, 20))
