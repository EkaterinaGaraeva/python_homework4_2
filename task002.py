# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def list_of_all_multipliers(n):
#     # list_of_multipliers = []
#     # for i in range(2, n):
#     #     if not int(n % i):
#     #         list_of_multipliers.append(i)
    list_of_multipliers = [i for i in range(2, n) if not int(n % i)]
    return list_of_multipliers


def list_of_simple_multipliers(list_of_multipliers):
#     # simple_multipliers = []
#     # for j in list_of_multipliers:
#     #     if (len(list_of_all_multipliers(j)) == 0):
#     #         simple_multipliers.append(j)
    simple_multipliers = [j for j in list_of_multipliers if not len(list_of_all_multipliers(j))]
    return simple_multipliers


n = 12345
all = list_of_all_multipliers(n)
print(f'Все множители числа N = {n} (кроме 1 и {n}): {all}')
simple = list_of_simple_multipliers(all)
print(f'Простые множители числа N = {n}: {simple}')


def list_of_simple_multipliers2(n):
    simple_multipliers = []
    for i in range(2, n):
        if not int(n % i):
            count = 0
            for k in range(2, i):
                if not int(i % k):
                    count += 1
                    if count > 0:
                        break
            if count == 0:
                if i not in simple_multipliers:
                    simple_multipliers.append(i)
    return simple_multipliers


s = list_of_simple_multipliers2(n)
print(f'Простые множители числа N = {n}: {s}')

