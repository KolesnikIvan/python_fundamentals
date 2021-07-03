"""Необходимо реализовать генератор,
возвращающий кортежи вида (<tutor>, <klass>) из соответсвующих списков:"""
from itertools import zip_longest
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
if len(tutors) > len(klasses):
    """чтобы по заданию кол-во кортежей 
    определялось длиной списка tutor применяю не zip, а zip_longest"""
    kls_ttr_gen = ((tt, kl) for tt, kl in zip_longest(tutors, klasses))
else:
    kls_ttr_gen = ((tt, kl) for tt, kl in zip(tutors, klasses))
print('data structre is of type ', type(kls_ttr_gen))
print(*kls_ttr_gen, sep='\n')
