# level 1
# exercise 1
numberOne = float(input('write in  number 1:'))
numberTo = float(input('write in  number 2:'))
numberThree = float(input('write in  number 3:'))
sum = numberOne+numberTo+numberThree
dobutok = numberOne*numberTo*numberThree
print(f"{sum}\n{dobutok}")

#exercise 2
d1 = float(input('write in  d1:'))
d2 = float(input('write in  d2:'))

S = (d1 * d2) / 2;

print(f"Площа ромба дорівнює {S}")


# level 2
# exercise 3

salary = float(input('write in  salary:'))
credit = float(input('write in  Credit:'))
utilities = float(input('write in  Utilities:'))
if(salary > (credit+utilities)):
    balance = salary - (credit+utilities)
    print(balance)
elif(salary <= (credit+utilities)):
    print("Зарплатні не вистачить все погасити, йди працюй")

# exercise 4
distance = float(input('write in  distance:'))
priceForFuel = float(input('write in  priceForFuel:'))
consumption = float(input('write in  consumption:'))

forOneK = consumption/100
tripFuelPrice = distance*forOneK*priceForFuel
print(f"Поїзда обійдеться: {tripFuelPrice}")


# level 3
# exercise 5

account = float(input('write in  account:'))
quantity = int(input('write in  quantity:'))
tip = account / 100*15
ingeneral = account + tip
result = ingeneral / quantity
print(result)

# exercise 6
perDay = float(input('write in  perDay:'))
quantityDays = float(input('write in  quantityDays:'))
deposit = float(input('write in  deposit:'))

ingeneralLie = perDay*quantityDays+deposit
withoutDeposit = ingeneralLie - deposit
pricePerDay = withoutDeposit / quantityDays

print('Не розумію навіщо все це робив , але зробив')
