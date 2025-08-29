# Завдання 5
# Запитайте в користувача введення номера замовлення.
#
# У блоці try перевірте, що номер замовлення починається з "ORD" і містить після цього цифри.
# Якщо формат неправильний, за допомогою raise згенеруйте виняток (raise Exception("Неправильний формат номера замовлення")).
# Перехопіть виняток у блоці except і виведіть зрозуміле повідомлення.
# У блоці finally виведіть повідомлення про завершення перевірки.

try:
    text = input('Введіть номер замовлення (наприклад ORD123):')
    first_check = False
    second_check = False
    if text[:3] == 'ORD' and text[3:].isdigit():
        first_check = True
    for i in range(len(text[3:])):
        if text[i].isdigit:
            second_check = True
        else:
            second_check = False
    if first_check == False or second_check == False:
        raise Exception
except Exception:
    print("Неправильний формат номера замовлення")
finally:
    print('Перевірку завершено')
# Завдання 6
# Попросіть користувача ввести послідовність чисел через пробіл.
#
# У блоці try перетворіть рядок на список чисел.
# Для кожного елемента використовуйте вкладений блок try для перетворення на число, перехоплюючи ValueError для некоректних значень з виведенням попередження і пропуском таких елементів.
# Після успішного перетворення обчисліть суму і, якщо потрібно, середнє значення. Перехопіть ZeroDivisionError, якщо список виявиться порожнім.
# У блоці finally виведіть повідомлення про завершення обробки даних.
try:
    raw_row = input('Введіть послідовність чисел через пробіл:').split(' ')
    list_of_raw_row = list()
    for i in range(len(raw_row)):
        try:
            list_of_raw_row.append(int(raw_row[i]))
        except ValueError:
            print(f"{raw_row[i]} має некоретний тип для форматування")
            continue
    result = sum(list_of_raw_row)
    print(result)
    avarge = result/len(list_of_raw_row)
except ZeroDivisionError:
    print('Список пустий для визначення середнього')
finally:
    print("Обробку було завершено")

# Напишіть програму, яка зчитує з консолі один рядок з інформацією про товари у форматі
#
# назва:ціна:кількість,…
# де записи розділені комами; програма повинна відкинути некоректні записи,
# обчислити загальну вартість кожного товару (ціна × кількість) та вивести три найдорожчі товари за спаданням вартості,
# обробивши всі помилки введення за допомогою винятків.
result_dict = dict()
def filling_up_dict(current_row: str):
    global result_dict
    split_row = current_row.split(':')
    try:
        if split_row[0].isdigit():
            raise ValueError
        try:
            split_row[1] = int(split_row[1])
            split_row[2] = int(split_row[2])
            result_dict[split_row[0]] = split_row[1] * split_row[2]
        except ValueError:
            print(f"{split_row} кількість та ціна мають бути цифрами")
        except IndexError:
            print(f"Бракує інформації у {split_row}")
    except ValueError:
        print(f'Назва товару {split_row} не має бути цифрою')


try:
    raw_list = input('Введіть інформацію про товари які ви купили у форматі (назва:ціна:кількість, назва:ціна:кількість,...').split(',')
    for i in range(len(raw_list)):
        filling_up_dict(raw_list[i])
    result_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
    l = 0
    for k in result_dict:
        if l < 3:
            print(f"{k}:{result_dict[k]}")
finally:
    print('Обробку завершено')