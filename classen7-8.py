#Exercise 1

# arrayOfDays = ['','Вт','Ср','Чт','Пт','Сб','Вс']
# inputData = int(input('Введіть порядковий номер:'))
# if(inputData <= 7):
#     print(arrayOfDays[inputData-1])
# else:
#     print('Номер не вірний, введіть вірний порядковий номер до дня тижня.')

#Exercise 2

# arrayOfDays = ['січень','лютий','березень','квітень','травень','червень','липень','серпень','вересень','жовтень','листопад','грудень']
# inputData = int(input('Введіть порядковий номер:'))
# if(inputData <= 12):
#     print(arrayOfDays[inputData-1])
# else:
#     print('Номер не вірний, введіть вірний порядковий номер до місяця.')

#Exercise 3

# sumForBuy = float(input('Введіть сумму:'))
# age = int(input('Введіть вік:'))
# sale = 0;
# if(age < 18):
#     sale = 10/100
# elif(age >= 18 and age <= 60):
#     sale = 5/100
# elif(age > 60):
#     sale = 15/100
#
# print(sumForBuy-(sumForBuy*sale))

#Exercise 4

# ball1 = float(input('Введіть перший бал:'))
# ball2 = float(input('Введіть другий бал:'))
# ball3 = float(input('Введіть третій бал:'))
#
# if(ball1 == 2 or ball2==2 or ball3 == 2):
#     print('Незадовільно')
# elif (ball1 >= 4 and ball2 >= 4 and ball3 >= 4):
#     print('Відмінно')
# else:
#     print('Задовільно')

#Exercise 5

# ball1 = float(input('Введіть перший бал:'))
# ball2 = float(input('Введіть другий бал:'))
# ball3 = float(input('Введіть третій бал:'))
# ball4 = float(input('Введіть четвертий бал:'))
#
# if(ball1 == 2 or ball2==2 or ball3 == 2 or ball4 == 2):
#     print('Не допускається до іспиту')
# elif (ball1 >= 4 and ball2 >= 4 and ball3 >= 4 and ball4 >= 4):
#     print('Допускається з відзнакою')
# else:
#     print('Допускається')

#Exercise 6

# age = float(input('Введіть вік автомобіля:'))
# kmQuantity = float(input('Введіть пробіг:'))
#
# if(age < 3 and kmQuantity < 30000):
#     print('Автомобіль у відмінному стані')
# elif (age < 10 and kmQuantity < 100000):
#     print('Автомобіль у хорошому стані')
# else:
#     print('Автомобіль потребує перевірки')