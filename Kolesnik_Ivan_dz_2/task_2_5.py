import random
costs = [round(random.uniform(1, 100), 2) for _ in range(random.randint(10, 20))]
# print(costs)
print(id(costs))
print('A:')
for cost in costs:
    # здесь разделяю рубли и копейки
    # хотел бы знать более изящный способ
    # сплит по разделителю целой и дробной частей не использую, т.к. число может оказаться целым
    mantissa = int(cost // 1)
    ordinate = int(round(cost - (cost // 1), 2) * 100)
    print(f'{mantissa:02d} руб {ordinate:02d} коп', '\t')  # печатаю цены в требуемом формате
costs.sort()
print(id(costs))
print('B:', id(costs), costs, 'отсортировано без создания нового списка')
s_costs = sorted(costs)
print('C:', id(s_costs), s_costs, 'отсортировано с созданием нового списка')
print('D:', costs[-5::1], 'пять самых больших цен')
