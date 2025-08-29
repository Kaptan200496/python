# Рівень 1

# Завдання 1
# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:

text = "Don't compare yourself with anyone in this world…"


def adder(textForAdding ) -> str:
    textForAdding += "\n  if you do so, you are insulting yourself.\n\tBill Gates"
    return textForAdding

print(adder(text))

# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

def searchPar(firstNumber, secondNumber) -> list:
    for i in range(firstNumber, secondNumber):
        if (i % 2) == 0:
            print(i)
searchPar(5,10)

# Рівень 2

# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
#
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.

squareSize = 6
fulling = False
def printSquare(fullOrNot,size):
    if fullOrNot:
        for _ in range(size):
            print('*' * size)
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print('*' * size)
            else:
                print('*' + ' ' * (size - 2) + '*')

printSquare(fulling, squareSize)

# Завдання 4
# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри
def minimalt(listOfNumbers)-> float:
    min = None
    for i in listOfNumbers:
        if min == None:
            min = i
        else:
            if min > i:
                min = i
    return min

print(minimalt([2,3,5,1,2,3,6,7,-7]))

# Рівень 3
# Завдання 5
# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр. З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.

def countOfNumber(number)-> int:
    count = 0
    while number > 1:
        number = number/10
        count+=1
    return count
print(countOfNumber(3456))
# Завдання 6
# Напишіть функцію, яка перевіряє чи є число паліндромом. Число передається як параметр. Якщо число паліндром, потрібно повернути з функції true, інакше false.
def palindrom(num):
    str_of_num = str(num)
    while len(str_of_num):
        print(str_of_num[1],str_of_num[-1])
        if str_of_num[0] != str_of_num[-1]:
            return False
        str_of_num = str_of_num[1:-1]
    return True

print(palindrom(123322))
