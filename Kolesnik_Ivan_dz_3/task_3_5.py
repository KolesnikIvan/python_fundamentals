def get_jokes(prohibit_repeat=False):
    """ Эта функция соединяет три слова,
    выбранные случайным образом из трех массивов"""
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while True:
        if len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0:
            print('All the words were used. The end')
            break
        nn = nouns[random.randint(0, len(nouns)-1)]
        adv = adverbs[random.randrange(0, len(adverbs))]
        adj = adjectives[random.randrange(0, len(adjectives))]
        if prohibit_repeat:
            nouns.pop(nouns.index(nn))
            adverbs.pop(adverbs.index(adv))
            adjectives.remove(adj)
        print(nn, adv, adj, end=' ')
        print()
        condition = input('Continue Y/N?')
        if condition == 'n' or condition == 'N':
            break  # А можно как-то покрасивее прописать условие выхода в while? В строке 8?


get_jokes(prohibit_repeat=True)
# get_jokes()
