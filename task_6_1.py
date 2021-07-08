"""Получить список кортежей вида:
(<remote_addr>, <request_type>, <requested_resource>).
Например, ('141.138.90.60', 'GET', '/downloads/product_2')"""

file_log = 'nginx_logs.txt'
result = []
with open(file_log, 'r', encoding='utf-8') as fl:
    for row in fl:
        remote_addr = row[:row.find(' -')]
        request_type = row[row.find('"') + 1:row.find(' /')]
        requested_resource = row[row.find(' /') + 1:row.find(' HTTP')]
        result.append((remote_addr, request_type, requested_resource))

print(*result, sep='\n')
