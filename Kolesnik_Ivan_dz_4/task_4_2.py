from decimal import *
from requests import get, utils
from datetime import datetime


def get_string_from_tag(text, tag):
    """функция возвращает содержимое тэга,
    которое из переданного текста с помощью сплитов"""
    if tag in text:
        text_s = text.split(tag)[1]
        begin = 1
        end = text_s.find(r'</')
        return text_s[begin:end]


def get_date(text):
    """фнукция извлекает дату из переданного текста и возвращает ее в виде строки"""
    dt = text.split('Date="')[1].split('"')[0]
    dd, mm, yy = map(int, dt.split('.'))
    return datetime(day=dd, month=mm, year=yy).date().isoformat()


def currency_rates(curr_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    # а где брать данные в такой удобной форме? html ведь, как правило, сложнее
    if response.status_code == 200
        curr_code_u = curr_code.upper()
        encodings = utils.get_encoding_from_headers(response.headers)
        content = response.content.decode(encoding=encodings)
        if curr_code_u in content:
            content_s = content.split(curr_code_u)[1]  # перввц шаг к нужной валюте
            getcontext().prec = 4  # устанавливаю точность
            nom = int(get_string_from_tag(content_s, 'Nominal'))  # какому количеству установлен курс
            val = Decimal(get_string_from_tag(content_s, 'Value').replace(',', '.'))/nom
            dt = get_date(content)
            return val, dt
        else:
            return None,


if __name__ == '__main__':
    print(*currency_rates('eur'), sep=', ')
    print(*currency_rates('usd'), sep=', ')
    print(*currency_rates('foo'), sep=', ')
