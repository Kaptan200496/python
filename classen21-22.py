# Завдання 5
import random
# Два списки цілих заповнюються випадковими числами. Необхідно:
#
#1 Сформувати третій список, що містить елементи обох списків;
#2 Сформувати третій список, що містить елементи обох списків без повторень;
#3 Сформувати третій список, що містить елементи спільні для двох списків;
#4 Сформувати третій список, що містить тільки унікальні елементи кожного зі списків;
#5 Сформувати третій список, що містить тільки мінімальне і максимальне значення кожного зі списків.

# array1 = [random.randint(1, 10) for _ in range(3)]
# array2 = [random.randint(1, 10) for _ in range(3)]
#1 print(array1+array2)
#2 print(list(set(array1+array2)))

#3
# resultAr = []
# for i in array1:
#     if i in array2:
#         resultAr.append(i)
# print(resultAr)
#3# або  з нового уроку
# set1 = set(array1)
# set2 = set(array2)
# print(list(set1 & set2))

#4
# resultAr4 = []
# for i in array1:
#     if i not in array2:
#         resultAr4.append(i)
# for j in array2:
#     if j not in resultAr4:
#         resultAr4.append(j)
# print(resultAr4)
# #4# або  з нового уроку
# both = list(set(array1) - set(array2) ^ set(array2) - set(array1))
# print(both)

#5
# max1 = max(array1)
# max2 = max(array2)
# min1 = min(array1)
# min2 = min(array2)
# print([max1,max2,min1,min2])

# Завдання 6
# Користувач вводить список цілих чисел. Необхідно відсортувати список так, щоб числа чергувалися:
# спочатку найменше, потім найбільше, потім друге за величиною, друге за мінімальністю тощо.
# Приклад:
# Вхідні дані: [4, 1, 7, 2, 9, 3].
# Очікуваний результат: [1, 9, 2, 7, 3, 4].
# ar1 = [4, 1, 7, 2, 9, 3]
# ar1 = sorted(ar1)
# ar2 = sorted(ar1,reverse=True)
# ar1.sort()
# i = 0
# resultArray = []
# while i <= (len(ar1)/2)+1:
#     resultArray.append(ar1.pop(0))
#     resultArray.append(ar2.pop(0))
#     i+=1
# print(resultArray)