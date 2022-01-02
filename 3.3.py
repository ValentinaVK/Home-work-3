from pprint import pprint
def thesaurus_adv(num):
    surname = {}
    lst = {}
    for i in num:
        name, surname = i.split()
        if not lst.get(surname[0]):
            lst[surname[0]] = {name[0] : [i]}
        elif not lst[surname[0]].get(name[0]):
            (lst[surname[0]])[name[0]] = i
        else:
            (lst[surname[0]])[name[0]].append(i)

    pprint(lst, width = 1)

strok = input('Введите имена и фамилии: ')
str = strok.split(', ')
print(str)

thesaurus_adv(str)

