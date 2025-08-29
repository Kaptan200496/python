#Рівень 1
# Завдання 1
# Напишіть програму, яка запитує в користувача два числа і виводить результат ділення першого числа на друге.
#
# У блоці try отримайте числа, перетворіть їх у тип float і виконайте ділення.
# Перехопіть ValueError, якщо введене значення не є числом, і ZeroDivisionError, якщо відбувається ділення на нуль.
# У блоці finally виведіть повідомлення про завершення операції.

# number1 = input('enter first number')
# number2 = input('enter second number')
# try:
#     if isinstance(number1, str) and isinstance(number2, str):
#         raise ValueError
#     fnumber1 = float(number1)
#     fnumber2 = float(number2)
#
#     try:
#         result = fnumber1/fnumber2
#         print(result)
#     except ValueError:
#         print(f"{number2} або {number1} не є цифрою")
# except ValueError:
#     print(f"{number2} або {number1} не є цифрою")
# except ZeroDivisionError:
#     print("На нуль ділити не можна, ай ай ай...")
# finally:
#     print('Ділення завершене')
# Завдання 2
# Створіть програму, у якій заздалегідь задано список (наприклад, [10, 20, 30, 40, 50]).
#
# Запитайте в користувача введення індексу елемента, який необхідно витягти.
# У блоці try перетворіть введення в число і виведіть елемент списку за вказаним індексом.
# Перехопіть ValueError (якщо індекс не є числом) і IndexError (якщо індекс виходить за межі списку).
# У блоці finally виведіть повідомлення про завершення операції.
# example_list = [10, 20, 30, 40, 50]
# input_data = input('введіть індекс цифри яку ви хочете вивести:')
# try:
#     if not input_data.isdigit():
#         raise ValueError
#     correct_data = int(input_data)
#     try:
#         output_data = example_list[correct_data]
#         print(output_data)
#     except IndexError:
#         print(f"Введений індекс {correct_data} за межами списку")
# except ValueError:
#     print('Індекс має бути цілим числом')
# finally:
#     print('Операція завершена')
# Рівень 2
# Завдання 3
# Попросіть користувача ввести дані про продажі через пробіл (наприклад, "100 250 300").
#selges_data = input('Введіть дані про продаж товарів через пробіл (наприклад, "100 250 300"):')
# У блоці try перетворіть введений рядок на список чисел і обчисліть загальну суму продажів.
# Перехопіть ValueError для некоректного введення.
# У блоці finally виведіть повідомлення про завершення обробки.
# try:
#     list_of_data = selges_data.split(' ')
#     buffer = list_of_data
#     list_of_data = []
#     for i in range(len(buffer)):
#         list_of_data.append(int(buffer[i]))
#     print(sum(list_of_data))
# except ValueError:
#     print('Введіть корректний рядок як у прикладі.')
# finally:
#     print('Обчислення завершене.')

# Завдання 4
# Напишіть програму, яка запитує в користувача число й обчислює його квадратний корінь.
# У блоці try перетворіть введення в число і перевірте, що воно не від'ємне.
# Якщо число від'ємне, згенеруйте виняток (raise Exception("Не можна обчислити квадратний корінь від'ємного числа")).
# Перехопіть ValueError і згенероване виключення, виведіть відповідне повідомлення.
# У блоці finally виведіть повідомлення про завершення обчислень.
# input_number = input('Введіть число для обчислювання:')
# try:
#     num = float(input_number)
#     if num < 0:
#         raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
#     print(num**0.5)
# except ValueError:
#     print("Невірний формат вводу даних.")
# except Exception as error:
#     print(f"Помилка: {error}")
# finally:
#     print("Обчислювання завершене.")
#
#
# Рівень 3
# Завдання 5
# Попросіть користувача ввести дані про товар у форматі: назва, ціна, кількість (наприклад, "Хліб:1.5, 10").
# product_row = input('Введіть рядок з товарoм через кому з ціною та кількістю наприклад "Хліб,1.5,10":')
# try:
#     list_of_product_data = product_row.split(",")
#     if len(list_of_product_data) < 3:
#         raise Exception('не повний рядок з даними')
#     price = int(list_of_product_data[1])
#     qty = int(list_of_product_data[2])
# except ValueError:
#     print('Невірний формат вводу даних ціни та кількості.')
# except Exception as e:
#     print(f"Зверніть увагу, {e}")
# finally:
#     print("Обробку завершено")
# У блоці try розділіть рядок по комах і спробуйте перетворити ціну та кількість на числа.
# Якщо перетворення не вдається, перехопіть ValueError для цієї операції, виведіть попередження і завершіть обробку.
# У блоці finally виведіть повідомлення про завершення парсингу.
# Завдання 6
# Реалізуйте функцію connect_to_server(), яка з використанням модуля random випадковим чином або повертає повідомлення про успішне підключення,
# або генерує виняток ConnectionError (за допомогою raise ConnectionError("Помилка підключення")).
#
# В основному блоці try викличте функцію connect_to_server().
# Перехопіть ConnectionError у блоці except і виведіть повідомлення "Не вдалося підключитися до сервера".
# У блоці finally виведіть повідомлення "Спробу завершено".
import random

def connect_to_server():
    if random.choice([True, False]):
        return "Успішне підключення"
    else:
        raise ConnectionError("Помилка підключення")

try:
    result = connect_to_server()
    print(result)
except ConnectionError as e:
    print(f"Не вдалося підключитися до сервера. {e}.")
finally:
    print("Спробу завершено")