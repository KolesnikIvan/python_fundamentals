"""Функция email_parse(<email_address>)
при помощи регулярного выражения извлекает
имя и домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError."""
import re

def email_parse(email_address):
    re_mail = re.compile(r'(?P<username>[A-Za-z0-9]*)@(?P<domain>[A-Za-z0-9]*\.[A-Za-z0-9]*)')
    # result = re_mail.finditer(email_address)
    result = re_mail.search(email_address)
    if result is None:
        raise ValueError(f'wrong email {email_address}')
    else:
        return result.groupdict()

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
