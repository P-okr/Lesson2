# print(list('Cписок данных'))   # Задание 1
# li = [1, 2, 3, 4, 5, 'Курица', "бекон", "томаты"]
# print(type(li[0]))
# print(type(li[1]))
# print(type(li[2]))
# print(type(li[3]))
# print(type(li[4]))
# print(type(li[5]))
# print(type(li[6]))
# print(type(li[7]))
# print(li[3])
#
# print('Введите элементы списка') # Задание 2
# a = int(input('Введите элемент 1 :'))
# b = int(input('Введите элемент 2 :'))
# c = int(input('Введите элемент 3 :'))
# d = int(input('Введите элемент 4 :'))
# e = int(input('Введите элемент 5 :'))
# f = int(input('Введите элемент 6 :'))

# li = [ a , b , c, d, e , f] #Задание 3
# print('Change 1 and 2')
# li[a],li[b] = li[b] , li[a]
# print(li)
# print('Change 3 and 4')
# li[c],li[d] = li[d],li[c]
# print(li)


# a ={'Зима': [1,2,12] , "Весна" : [4,5,3], "Лето" : [7,8,6], "Осень" :[9,10,11]} #Задание 4
# n = int(input('Введите номер месяца :'))
# for el in a:
#     if n in a[el]:
#         print(el)
#         break
#
#
# st = (input('Введите слова :')). lower().split() #Задание 5
# li = [st]
#
# for i, el in enumerate(st):
#     print(f'{i}. {el}')

a = int(input('gh'))
li = [7,5,3,3,2,a]
li.sort(reverse=True)
print(f'Новый список: {li}')


