"""Регулярное выражение для парсинга логов web-сервера
из ДЗ 6 урока nginx_logs.txt"""
import os
import re

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'

re_obj = re.compile(r'''^(\d.*\d)\s-.*      # address
                        \[(.*)].*           # time in square parentheses
                        "([A-Z]+)\s         # type between " and whitespace
                        (/.*)\sH.*          # resource
                        (\d{3})\s           # response code
                        (\d*)\s"            # size
                        ''', re.VERBOSE)
with open("nginx_logs.txt", 'r', encoding='utf-8') as f:
    for line in f:
        print('parsed_raw =',re_obj.findall(line), sep='')
        input()
