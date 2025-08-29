#1
# inputNumber1 = int(input('enter from number'))
# inputNumber2 = int(input('enter to number'))
# for i in range(inputNumber1, inputNumber2):
#     if(i%7==0):
#         print(i)
#2
# inputNumber1 = int(input('enter from number: '))
# inputNumber2 = int(input('enter to number: '))
#
# for i in range(inputNumber2, inputNumber1-1,-1):
#         print(i,'r')
# for i in range(inputNumber1, inputNumber2+1):
#         print(i,'a')
# for i in range(inputNumber1, inputNumber2):
#     if(i%7==0):
#         print(i,'d7')
#
# count5 = 0
# for i in range(inputNumber1, inputNumber2+1):
#     if(i%5==0):
#         count5+=1
# print(count5,'d5')

#3
# inputNumber1 = int(input('enter from number: '))
# inputNumber2 = int(input('enter to number: '))
# for i in range(inputNumber1, inputNumber2+1):
#     if(i%3==0 and i%5==0):
#         print('Fizz Buzz')
#     elif(i%3 == 0):
#         print('Fizz')
#     elif(i%5==0):
#         print('Buzz')
#     else:
#         print(i)

#4
# inputNumber1 = int(input('enter from number: '))
# inputNumber2 = int(input('enter to number: '))
# step = int(input('enter step number: '))
# direction = input('enter direction(avers or revers):')
# if(direction == 'avers'):
#     for i in range(inputNumber1, inputNumber2, step):
#         print(i)
# elif(direction == 'revers'):
#     for i in range(inputNumber2, inputNumber1, -(step)):
#         print(i)

#5
# inputNumber1 = int(input('enter first number: '))
# inputNumber2 = int(input('enter second number: '))
# buffer=0
# resultSum = 0
# if(inputNumber2 < inputNumber1):
#     buffer = inputNumber1
#     inputNumber1 = inputNumber2
#     inputNumber2 = buffer
# for i in range(inputNumber1, inputNumber2+1):
#     if(i%4 == 0 and i%6 != 0):
#         resultSum+=i
# print(resultSum)

#6
# inputNumber1 = int(input('enter A number: '))
# inputNumber2 = int(input('enter N number: '))
# result = inputNumber1
# for i in range(1, inputNumber2):
#     result = result*inputNumber1
# print(result)
