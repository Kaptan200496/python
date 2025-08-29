#1
# data = int(input('enter number:'))
# for i in range(0,7):
#     print(data**i)
#2
# iceMin = int(input('enter price ice-vodafon:'))
# durationSec = int(input('enter duration:'))
# vodafonMin = int(input('enter price vodafon-ice:'))
# callingOf = input('enter callingOf:')
#
# iceSec = iceMin/60
# vodafonSec = vodafonMin/60
# if(callingOf == 'ice'):
#     result = iceSec*durationSec
# elif(callingOf == 'vodafon'):
#     result = vodafonSec*durationSec
# else:
#     print('enter right operator')
#
# print(result)


#3
# inputNumber = int(input('enter number:'))
# if(100> inputNumber >0):
#     if(inputNumber%3==0 and inputNumber%5==0):
#         print('Fizz Buzz')
#     elif(inputNumber%3 == 0):
#         print('Fizz')
#     elif(inputNumber%5==0):
#         print('Buzz')
#     else:
#         print(inputNumber)
# else:
#     print('Wrong number. Write number in 1-100 range')
#4
# sFirstManager = float(input('enter salary to first manager:'))
# sSecondManager = float(input('enter salary to second manager:'))
# sThirdManager = float(input('enter salary to third manager:'))
#
# if(sFirstManager <= 500):
#     firstSalary = sFirstManager*0.03 + sFirstManager
# elif(500 < sFirstManager < 1000):
#     firstSalary = sFirstManager*0.05 + sFirstManager
# elif(sFirstManager >= 1000):
#     firstSalary = sFirstManager*0.08 + sFirstManager
#
# if(sSecondManager <= 500):
#     secondSalary = sSecondManager*0.03 + sSecondManager
# elif(500 < sSecondManager < 1000):
#     secondSalary = sSecondManager*0.05 + sSecondManager
# elif(sSecondManager >= 1000):
#     secondSalary = sSecondManager*0.08 + sSecondManager
#
# if(sThirdManager <= 500):
#     thirdSalary = sThirdManager*0.03 + sThirdManager
# elif(500 < sThirdManager < 1000):
#     thirdSalary = sThirdManager*0.05 + sThirdManager
# elif(sThirdManager >= 1000):
#     thirdSalary = sThirdManager*0.08 + sThirdManager
#
# if(firstSalary > secondSalary and firstSalary > thirdSalary):
#     firstSalary+=200
# elif(secondSalary > firstSalary and secondSalary > thirdSalary):
#     secondSalary+=200
# elif(thirdSalary > firstSalary and thirdSalary > secondSalary):
#     thirdSalary+=200
#
# print(f"firstS={firstSalary}\nsecondS={secondSalary}\nthirdS={thirdSalary}")

#5
# bodyOfCredit = float(input('Enter body of credit:'))
# yearsCount = int(input('Enter years:'))
# creditProcent = 0;
# if(bodyOfCredit <= 10000 and yearsCount<=3):
#     creditProcent = 8
# elif(bodyOfCredit <= 10000 and yearsCount >3):
#     creditProcent = 10
# elif((50000 >= bodyOfCredit > 10000) and yearsCount <= 3):
#     creditProcent = 12
# elif((50000 >= bodyOfCredit > 10000) and yearsCount > 3):
#     creditProcent = 15
# elif(bodyOfCredit > 50000):
#     creditProcent = 20
#
# resultCredit = bodyOfCredit+(bodyOfCredit*creditProcent/100)
# payPerMonth = resultCredit/(yearsCount*12)
#
# print(resultCredit,"\n",payPerMonth)

#6
#Закуски
#salat = 5
#soop = 7
#Основні страви:
#kylling = 10
#fish = 12
#Десерти:
# ice = 3
# fruits = 4
#
# regularFlag = input('are you regular client(yes or no):')
# appetizers = input('salat or soop or both:')
# mainDishes = input('kylling or fish or both:')
# deserts = input('ice or fruits or both:')
# appetizersFlag = 0
# mainDishesFlag = 0
# desertsFlag = 0
# total = 0
# soopAndFish = 0
# kyllingAndIce = 0
# sale = 0
# tee = 0
# match appetizers:
#     case "salat":
#         appetizersFlag+=1
#         total+=salat
#     case "soop":
#         appetizersFlag+=1
#         total+=soop
#         soopAndFish+=1
#     case "both":
#         appetizersFlag+=1
#         total+=salat+soop
#         soopAndFish+=1
# match mainDishes:
#     case "kylling":
#         mainDishesFlag+=1
#         total+=kylling
#         kyllingAndIce+=1
#     case "fish":
#         mainDishesFlag += 1
#         total+=fish
#         soopAndFish+=1
#     case "both":
#         mainDishesFlag += 1
#         total+=fish+kylling
#         soopAndFish+=1
#         kyllingAndIce+=1
# match deserts:
#     case "ice":
#         desertsFlag+=1
#         total += ice
#         kyllingAndIce+=1
#         if(soopAndFish==2):
#             total-=2
#             soopAndFish = 0
#     case "fruits":
#         desertsFlag += 1
#         total += fruits
#         if (soopAndFish == 2):
#             total -= 2
#             soopAndFish = 0
#     case "both":
#         desertsFlag += 1
#         total+= fruits+ice
#         kyllingAndIce+=1
#         if (soopAndFish == 2):
#             total -= 2
#             soopAndFish = 0
# if(regularFlag == "yes"):
#     sale+=5
# if(mainDishesFlag and desertsFlag and appetizersFlag):
#     sale+=10
#     if(total>20):
#         sale+=5
# if(kyllingAndIce == 2):
#     tee = 1
# #print(total,sale,tee)
# total = total-(total*(sale/100))
# result = f"Ваше замовлення коштує: {total}$."
# if tee:
#     result+=" Також ви отримуєте додатковий чай безкоштовно"
# print(result)