# firstNumber = float(input('first number: '))
# secondNumber = float(input('second number: '))
#
# isSumm = firstNumber + secondNumber
# isDifference = firstNumber - secondNumber
# isProduct = firstNumber*secondNumber
#
# print(f"{isSumm}\n{isDifference}\n{isProduct}")
from sys import flags

# 1. Користувач вводить суму в євро та курс обміну на гривню, програма має обчислити скільки гривень отримує користувач

# 2. Користувач вводить число, з 4 цифрами (напр 1234), необхідно вивести його навпаки, (напр: 4321)

# isAmount = float(input('how much EUR: '))
# isExchange = float(input('exchange to UAH: '))
#
# print(f"Ви отримаєте " ,{isAmount*isExchange} ," UAH")

#num = input('number for reverse: ')[::-1]
#num = input('number for reverse: ')
# num = '42134'
# strlen = len(str(int(num)))
# i = 1
# n = int(num)
# resStr = ''
#
# while i <= strlen:
#     n2 = n % 10
#     resStr+=str(n2)
#     n1 = int(n / 10)
#     n = n1
#     i+=1
#
# print(resStr)
# x1=2
# y1 =3
# x2 =1
# y2 = 6
#
# if x1 == x2 or y2 == y1:
#     print('yes')
# else:
#     print('no')

# x1 = 4
# y1 = 4
# x2 = 3
# y2 = 6
# x1 = 4
# y1 = 4
# x2 = 6
# y2 = 5
#
# if(x1<=8 and y1<=8 and x2<=8 and y2<=8):
#     if (abs(x2 - x1) + abs(y2 - y1)) == 3:
#         print('yes')
#     else:
#         print('no')
# else:
#     print('Невірний формат дошки')
# Користувач вводить числа, коли він написав 0, програма має зупинитися, і вивести суму всіх чисел, які він ввів,
# також вивести середнє арифметичне,
# ** також вивести максимальне і мінімальне число

# flag = True
# maximalt = 0
# gjennomsiktig = 0
# sum = 0
# generelt = 0
# while flag:
#     inputNumber = float(input('Enter your number: '))
#     print(type(inputNumber))
#     if(type(inputNumber) == float or type(inputNumber) == int):
#         generelt += 1
#         if (generelt == 1):
#             minimalt = inputNumber
#         if(inputNumber != 0):
#             sum += inputNumber
#             if(inputNumber < minimalt):
#                 minimalt = inputNumber
#             if(inputNumber > maximalt):
#                 maximalt = inputNumber
#         else:
#             if(generelt > 0):
#                 gjennomsiktig = sum / generelt
#             flag = False
#             continue
#     else:
#         print('Wrong number, please enter valid value.')
#
# print(f"max={maximalt},min={minimalt},sum={sum},generelt={generelt},gjennomsiktig={gjennomsiktig}")

# for i in range(5, 10 , -1):
#     print(i)

