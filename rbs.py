#!/usr/bin/env python
#encoding:UTF-8
import sys
"""
Сын учится читать, у него хорошо получается читать по слогам,
но читать тексты с целыми словами получается пока плохо.
Поиск книг типа "читаем по слогам" выдал где то штук 10 разных, мало :(.

Так появилась идея написать скриптик для разбивки текста на слоги.
Написал за вечер для того, что бы разбивать сказки для чтения по слогам :)

01.06.2013
Sergey Poterianski
s@poterianski.ru
"""

"""
объявляем словарики для согласных, глухих, гласных
"""
consonants = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к',
u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ']
thud = [u'к', u'п', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ']
vowels = [u'а', u'у', u'о', u'ы', u'и', u'э', u'я', u'ю', u'ё', u'е']

"""
usage:
    pbs.py [filename] - файлик с текстом для разбивки на слоги
    результат выводится в консоль
"""
def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    for line in file:
        split2words(line.decode(encoding='UTF-8',errors='strict'))

"""
Перебирает строки
"""
def split2words(line):
    i = 0
    result = ''
    word = ''
    while i < len(line):
        c = line[i]
        if isconsonant(c) or isvowel(c) \
        or c == u'ь' or c == u'Ь' or c == u'ъ' or c == u'Ъ':
            word += c
        else:
            if len(word) > 0:
                if len(word) <= 2:
                    result += word
                else:
                    result += split2syllables(word)
                word = ''
            result += c
        i += 1
    print(result.strip())

"""
Делит слово на слоги
"""
def split2syllables(word):
    splited = ''
    slog = ''
    i =  0
    #v = False
    scount = vowelcount(word)
    if scount == 1:
        return word

    while i < len(word):
        c = word[i]
        #добавляем букву в слог
        slog += c
        # если гласная
        if isvowel(c):
            # смотрим что идет после
            # есть буквы
            if i+1 < len(word):
                c1 = word[i+1]
                # если согласная
                if isconsonant(c1):
                    # если последняя в слове - добавляем в слог и выходим
                    if i+1 >= len(word) - 1:
                        slog += word[i+1]
                        i+=1
                    else:
                        # не последняя,запоминем проверяем что идет после нее
                        c2 = word[i+2]
                        # если идет Й и следом согласный - добавляем в слог
                        if (c1 == u'й' or c1 == u'Й') and isconsonant(c2):
                            slog += c1
                            i += 1
                        # если после звонкой не парной идет глухой согласный - добавляем в слог
                        elif (c1 in [u'м',u'н',u'р',u'л'] or c1 in [u'М',u'Н',u'Р',u'Л']) and isthud(c2):
                            slog += c1
                            i += 1
                        elif i+2 >= len(word) - 1 and (c2 == u'ь' or c2 == u'Ь' or c2 == u'ъ' or c2 == u'Ъ'):
                            # заканчивается на мягкий
                            i+=2
                            slog += c1 + c2
            splited += slog
            if i+1 < len(word):
                splited += '-'
            slog = ''
        i += 1
    return splited
"""
считает гласные
"""
def vowelcount(word):
    cnt = 0
    for c in word:
        if(isvowel(c)):
            cnt += 1
"""
Если согласный
"""
def isconsonant(char):
    x = char.lower()[0]
    for c in consonants:
        if c == x:
            return True
"""
Если глухой
"""
def isthud(char):
    x = char.lower()[0]
    for c in thud:
        if c == x:
            return True
"""
Если гласный
"""
def isvowel(char):
    x = char.lower()[0]
    for c in vowels:
        if c == x:
            return True
    return False


if __name__ == '__main__':
    main()
