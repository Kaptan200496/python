#1
# inputData = input('Enter number:')
# if(int(inputData) > 0):
#     result = 0
#     for i in inputData:
#         result += int(i)
# print(result)
#2
#endNumber = int(input('Enter number:'))
# n = 1
# while n < endNumber:
#     for i in range(1, n+1):
#         if(n%i == 0 and i != n and i != 1):
#             n += 1
#             continue
#     print(n)
#     n+=1


# 3
# Знайти НСД (наибільший спільний дільник) двох чисел.
# користувач вводить два числа, необхідно знайти НСД.
# 10 20 -> 10
# NSD = None
# firstNumber = int(input('Enter first number:'))
# secondNumber = int(input('Enter second number:'))
# if(secondNumber > firstNumber):
#     if(secondNumber%firstNumber == 0):
#         NSD = firstNumber
#     else:
#         for i in range(firstNumber, 1 , -1):
#             if(firstNumber%i==0 and secondNumber%i==0):
#                 NSD = i
# elif(firstNumber > secondNumber):
#     if(firstNumber%secondNumber == 0):
#         NSD = secondNumber
#     else:
#         for i in range(secondNumber, 1 , -1):
#             if(secondNumber%i==0 and firstNumber%i==0):
#                 NSD = i
#
# if(NSD == None):
#     print('Спільний дільник не знайдено, змініть вхідні дані')
# else:
#     print(f"Cпільний дільник={NSD}")
# 4**
# перетворення десяткового числа в двійковий рядок
# 10 -> 1010
# 5 -> 101
# 8 -> 1000
# 15 -> 1111
# decimalNumber = int(input('Enter decimal number:'))
# degree = 0
# beginsNumber = 2**degree
# resultStr = '1'
# while(beginsNumber < decimalNumber):
#     degree+=1
#     beginsNumber = 2 ** degree
# else:
#     degree-=1
#     beginsNumber = 2 ** degree
# #print(degree, beginsNumber)
# nextNumber = decimalNumber - beginsNumber
# degree -= 1
# # while(nextNumber != 0 and nextNumber > 0):
# while degree+1:
#     if((nextNumber/(2**degree)) >= 1):
#         resultStr +='1'
#         nextNumber = nextNumber-2**degree
#     else:
#         resultStr +='0'
#     degree-=1
# print(resultStr)
# 5**
# розклад числа на прості множини
# 4 -> 2*2
# 6 -> 2*3
# 8 -> 2*2*2
# 20 -> 2*2*2*5
# 100 -> 2*2*2*2*5*5
# decimalNumber = int(input('Enter decimal number:'))
# dell = 2
# resultStr = ''
# while decimalNumber > 1:
#     if (decimalNumber%dell == 0):
#         if(not resultStr):
#             resultStr = '*'+str(dell)
#         else:
#             if(decimalNumber/dell == 1):
#                 resultStr = str(dell) + resultStr
#             else:
#                 resultStr = '*'+str(dell) + resultStr
#         decimalNumber = decimalNumber//dell
#     else:
#         dell+=1
#
# print(resultStr)


