# 1 задание

 # for k, v in classmates.items():
#         print(k + v)
#
#         spisok = [1, 2]
#
#         # spisok[:1] = [2]
# print(spisok)


# classmates = {'a': '2', 'b': '3', 'c': '4', 'd': '5'}

# def list_function(x):
#     x[1] = x[1] + 1
#     return x
#
#
#     n = (2, 3, 4)
#     print(n)



# 3 задание фибоначи

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci(-1)+fibonaccci(n-2))

fibonacci(1)
fibonacci(2)
fibonacci(3)
fibonacci(4)
fibonacci(5)
fibonacci(6)

