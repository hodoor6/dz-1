# 1. Задание	написати функцію, яка приймає словник і повертає список в якому всі значення словника помножені на 2
#
# def dictList():
#     dictionary = {'a': 2, 'b': 3, 'c': 4}
#     listt = dictionary.values()
#     listt = list(listt)
#     for i in range(len(listt)):
#         print(listt[i] * 2)
# dictList()

# 2. Задание 	написати функцію, яка приймає 3 рядки - шаблон (в якому є %s i %d), якесь слово і число і виводить відформатований рядок. наприклад format3(‘%s speak %d languages’, ‘Petro’, 5) має друкувати ‘Petro speak 5 languages’

# def fun():
#     print('%s speak %d languages' % ('Petro',5))
# fun()
#
# def fun1():
#     print('%s %s, %d %s' % ('Petro','speak',5,'languages'))
# fun1()
#
# def fun2():
#   print ('%(name)s speak %(number)d languages.' % {"name": "Petro", "number": 5})
# fun2()

# def fun3():
#   name = 'Petro'
#   age = 5
#   print ('%s speak: %d languages' % (name, age))
#
# fun3()

# 3 Задание 	написати функцію, яка повертає n-e число фібоначчі. fibo(n):***return f  1->1, 2->1, 3->2, 4->3, 5->5, 6->8
#
# def fibonacci(n):
#     fib1, fib2 = 0, 1
#     for i in range(n):
#         fib1, fib2 = fib2, fib1 + fib2
#         yield fib1
#
# print(list(fibonacci(6)))

# 4. Задание	написати функцію, яка сортує масив слів по кількості голосних і видаляє з масиву інші (не string) типи (потрібно використати функцію для перевірки типу)

# word = "Python"
# vowels = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))


# def CountVowel(string):
#     countVowel = 0;
#     for i in string:
#         if  i == 'а' or i == 'е' or i == 'ё' or i == 'и' or i == 'о' or i == 'у' or i == 'ы' or i == 'э' or i == 'ю' or i == 'я':
#            countVowel+=1
#     return countVowel
# lst = ['кошка','кофе','телевизор','автомобиль']
# rang = range(len(lst))
# for i in rang:
#     lst[i] = CountVowel(lst[i])
# print(lst)

# 5 Задание 4.	є версії програми в форматі ‘1.5.3.45’ або ‘2.0’. кількість чисел в версії може бути різна. треба написати функцію, яка відсортує версії.

# def printVers():
#   vers = [10.5,3.56,4.678,1.6677,9.5779]
#   vers.sort()
#   print(vers)
# printVers()
#
#
# def printVers1():
#     vers1 = [[2.667, 101], [2.6, 4.45], [1.8, 9.9]]
#     vers1.sort()
#     print(vers1)
# printVers1()
