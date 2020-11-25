# Дано натуральне число n. Перевірити усі числа від 1 до n на те,
# чи можна подати факторіал цього числа у вигляді добутку трьох  послідовних цілих чисел.
# Вивести числа, для яких виконується умова.

n = int(input('Please, enter natural number n: '))
fact = 1
print('A sequence of numbers that fulfill the condition of the problem:')
for i in range(1, n + 1):
    fact = fact * i
    j = 1
    while j * (j + 1) * (j + 2) <= fact:
        if fact == j * (j + 1) * (j + 2):
            print(i, ' (', i, '!=', j, '*', j + 1, '*', j + 2, ')', sep='')
        j = j + 1
