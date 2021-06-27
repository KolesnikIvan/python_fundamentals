def translate(num_eng):
    vocabulary = {'one': 'один',
                  'two': 'два',
                  'three': 'три',
                  'four': 'четыре',
                  'five': 'пять',
                  'six': 'шесть',
                  'seven': 'семь',
                  'eight': 'восемь',
                  'nine': 'девять',
                  'ten': 'десять'}
    if num_eng.lower() in vocabulary:
        if num_eng.istitle():
            return vocabulary.get(num_eng.lower()).title()
        else:
            return vocabulary.get(num_eng.lower())
    else:
        return None  # если не нашел в словаре входной цифры, то None


# print(translate('Three'))
