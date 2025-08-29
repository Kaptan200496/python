# Завдання 1
# Користувач з клавіатури вводить елементи списку цілих.
# Необхідно порахувати суму всіх елементів та їхнє середньоарифметичне.
# Результати вивести на екран.
# inputData = input('enter list of numbers with coma').split(',')
# data = []
# for item in inputData:
#         data.append(int(item))
# summa = sum(data)
# count = len(data)
# result = summa/count
# print(result)
# Завдання 2
# Користувач з клавіатури вводить елементи списку цілих і деяке число.
# Необхідно порахувати скільки разів дане число присутнє у списку.
# Результат вивести на екран
# inputData2 = input('enter list of numbers with coma2').split(',')
# targetNumber = input('enter target number')
# count = 0
# for item2 in inputData2:
#     if targetNumber == item2:
#         count+=1
# print(count)

# Завдання 3
# Користувач з клавіатури вводить список чисел.
# Необхідно знайти суму всіх додатних чисел у списку. Результат вивести на екран.
# inputData3 = input('enter list of numbers with coma3').split(',')
# data3 = []
# for item3 in inputData3:
#         data3.append(int(item3))
# res = sum([number3 for number3 in data3 if number3>0])
# print(res)
# Завдання 4
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно визначити індекси всіх парних чисел у списку.
# Результат вивести на екран.
# inputData4 = input('enter list of numbers with coma3').split(',')
# data4 = []
# for item4 in inputData4:
#         data4.append(int(item4))
# res = [data4.index(number4) for number4 in data4 if number4%2 == 0]
# print(res)

# Завдання 5
# Є деякий текст. Реалізуйте таку функціональність
# Змінити текст таким чином, щоб кожне речення починалося з великої літери;

# Баба міша1.пішла додопу22.збирати йогуртc333
# inputData5 = input('enter list of data with coma5').split('.')
# result = ''
# for raw in inputData5:
#     raw = raw.lstrip().capitalize()
#     result += raw+'.'
# print(result)

##Порахуйте скільки разів цифри зустрічаються в тексті;

import re
# counter = 0
# inputData51 = input('enter list of data with coma5')
# for raw in inputData51:
#     match = re.findall(r"[0-9]", raw, re.I)
#     if match:
#        counter+=1
# print(counter)
## Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# counter2 = 0
# inputData52 = input('enter list of DATA with coma5')
# for raw in inputData52:
#     match = re.findall(r"[\\^$.|?*+()|_\-|\!,]", raw, re.I)
#     if match:
#        counter2+=1
# print(counter2)
## Порахуйте кількість знаків оклику в тексті.
# Завдання 6
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно видалити зі списку всі елементи, що повторюються, залишивши тільки унікальні. Результат вивести на екран.

# inputData6 = input('enter list of numbers with coma6').split(',')
# resultArray = list()
# for i in inputData6:
#     if i not in resultArray:
#         resultArray.append(i)
# print(resultArray)
#### aбо по новому уроку 20-06-2025
# print(list(set(inputData6)))