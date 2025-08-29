# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно визначити кількість елементів у списку,
# які більші за попередній елемент. Результат вивести на екран.
# Приклад:
# Вхідні дані:
# Список чисел: 1, 3, 2, 4, 5
# Очікуваний результат:
# Кількість елементів: 3.
# (Пояснення: 3 > 1, 4 > 2, 5 > 4).

# enteringData = input('enter list av numbers1').split(',')
# count = 0
# for i in range(len(enteringData)):
#     if enteringData[i] > enteringData[i-1]:
#         count+=1

# Завдання 2
# Користувач вводить список цілих чисел. Необхідно вивести тільки ті елементи,
# які зустрічаються у списку рівно один раз, зберігаючи порядок їхньої появи.
# Приклад:
# Вхідні дані: 1, 2, 2, 3, 3, 4, 4, 5.
# Очікуваний результат: [1, 3, 5].
#
# enteringData2 = input('enter list av numbers2').split(',')
# unique_list = []
# arrResult = []
# for item in enteringData2:
#     if item not in unique_list:
#         unique_list.append(item)
#
# for i in range(len(unique_list)):
#     double = 0
#     for j in range(len(enteringData2)):
#         if unique_list[i] == enteringData2[j]:
#             double+=1
#     if double != 2:
#         arrResult.append(unique_list[i])
# print(arrResult)

# Завдання 3
# Користувач з клавіатури вводить список чисел.
# Необхідно знайти у списку найдовшу послідовність елементів,
# що зростають, і вивести її довжину та самі елементи.
# Приклад:
#
# Вхідні дані:
#
# Список чисел: 1, 2, 1, 2, 3, 4, 1.
#
# enteringData3 = input('enter list av numbers3').split(',')
# arResult = []
# previousElement = 0
# maxCount = 0
# for i in range(len(enteringData3)):
#     if i == 0:
#         arResult.append(enteringData3[i])
#        # previousElement = enteringData3[i]
#     else:
#         if int(enteringData3[i]) > previousElement:
#             arResult.append(int(enteringData3[i]))
#             previousElement = int(enteringData3[i])
#         else:
#             maxCount = len(arResult)
#             arResult = [int(enteringData3[i])]
#             previousElement = int(enteringData3[i])
# print(arResult,maxCount)
# Завдання 4
# Користувач із клавіатури вводить список цілих чисел.
# Необхідно реалізувати циклічний зсув списку вправо на N позицій. Результат вивести на екран.
# Приклад:
# Вхідні дані:
# Список чисел: 1, 2, 3, 4, 5.
# Число позицій N: 2.
# Очікуваний результат:
# Зсунутий список: [4, 5, 1, 2, 3].
# enteringData4 = input('enter list av numbers4').split(',')
# enteringStep = int(input('enter step'))
# arResult = []
# lengthOfArray = len(enteringData4)
# for i in range(enteringStep):
#     arResult.append(enteringData4.pop())
# arResult.reverse()
# arResult.extend(enteringData4)
# print(arResult)


