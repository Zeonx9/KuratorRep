from itertools import product

codes = []
for length in range(2, 7):  # для длин кодов от 2 до 7 т.к меньше не подходит по условию а больше не получится т.к. всего 6 различных букв
    for x in product('ЯСУПЕР', repeat=length):   # состовляем все кобинации нужной длины из исходного набора
        if len(set(x)) == length:      # если повторов нет: т.е. число различных символов совпадает с длиной выборки, то нам подходит
            codes.append(''.join(x))            # добавляем в список


print(len(codes) * 10, codes)  # количество умножаем на 10 т.к. после каждого полученого кода можно поставить 10 различных цифр



