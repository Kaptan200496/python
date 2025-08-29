# k1 = (1,3,4,5,7,6,8)
# k2 = (123,1,4,5,6,7,8,9,10)
# k3 = (2,3,4,6,7,55)
# Завдання 1
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є у всіх кортежах.
# sets = [set(k1), set(k2), set(k3)]
# searchingSame = set.intersection(*sets)
## abo tak print(set(k1) & set(k2) & set(k3))
# print(searchingSame)
# Завдання 2
# Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.
# l1 = list(k1)
# l2 = list(k2)
# l3 = list(k3)
# uniq1 = []
# uniq2 = []
# uniq3 = []
# for i in l1:
#     if i not in l2 and i not in l3:
#         uniq1.append(i)
# for j in l2:
#     if j not in l1 and j not in l3:
#         uniq2.append(j)
# for g in l3:
#     if g not in l1 and g not in l2:
#         uniq3.append(g)
#print(tuple(uniq1),tuple(uniq2),tuple(uniq3))
# Завдання 3
# Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів і знаходяться в кожному з них на тій самій позиції.
#
#
# resultArray = []
# minRange = min(len(k1), len(k2), len(k3))
# # проходимо по всіх позиціях (індексах)
# for i in range(minRange):
#     if(k1[i] == k2[i] == k3[i]):
#         resultArray.append(k1[i])
#
# print(resultArray)