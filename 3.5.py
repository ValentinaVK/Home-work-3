import random
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Number = int(input('Введите количество шуток: '))

def get_jokes(Num):
    i = 0
    lst = []
    while i < Num :
        i += 1
        lst.append(random.choice(nouns)+' '+ random.choice(adverbs)+' '+ random.choice(adjectives))
    print(lst)

get_jokes(Number)