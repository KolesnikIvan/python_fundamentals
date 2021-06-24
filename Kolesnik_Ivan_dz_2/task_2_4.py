raw_msg = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in raw_msg:
    name = worker.split()[-1].lower().capitalize()
    print(f'Привет {name}!')
