import re


class TheDate:
    """Класс «Дата». """
    def __init__(self, dd_mm_yy_string):
        """Конструктор принимает дату в виде строки «день-месяц-год». """
        if self.method_validator(dd_mm_yy_string):
            self.dd, self.mm, self.yy = self.method_extractor(dd_mm_yy_string)
        else:
            raise ValueError("Incorrect dd_mm_yy string.")

    @classmethod
    def method_extractor(cls, dd_mm_yy_string):
        """Метод с декоратором @classmethod извлекает число, месяц, год
        и преобразует к типу «Число».
        """
        dt = re.compile(r'(\d{,2}).(\d{,2}).(\d{2,4})')
        mo = dt.match(dd_mm_yy_string)
        dd = int(mo.group(1))
        mm = int(mo.group(2))
        yy = int(mo.group(3))
        return [dd, mm, yy]

    @staticmethod
    def method_validator(dd_mm_yy_string):
        """Метод с декоратором @staticmethod проводит валидацию числа, месяца и года."""
        # dd, mm, yy = TheDate(dd_mm_yy_string).method_extractor(dd_mm_yy_string)
        dt = re.compile(r'(\d{,2}).(\d{,2}).(\d{2,4})')
        mo = dt.match(dd_mm_yy_string)
        dd = int(mo.group(1))
        mm = int(mo.group(2))
        yy = int(mo.group(3))
        if dd in range(1, 32) and mm in range(1,13):
            print(dd_mm_yy_string, 'is valid')
            return True
        else:
            print(dd_mm_yy_string, 'is not valid')
            return False


dat = TheDate('07.07,2014')
print(dat.dd)
print(dat.mm)
print(dat.yy)
TheDate.method_validator('13,04,2021')
# dat2 = TheDate('35,10,2021')
dat3 = TheDate('20,15,2021')
