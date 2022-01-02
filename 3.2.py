def num_translate(num):
    Translate = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
    }
    if num.istitle() == True:
        num_new = num.lower()
        result = Translate.get(num_new)
        print(result.capitalize())
    else:
        print(Translate.get(num))

Number = input('Введите число от 0 до 10 на англиском языке: ')
num_translate(Number)