# Рівень 1
# Завдання 1
# Напишіть функцію, яка повертає суму чисел у вказаному діапазоні.
# Межі діапазону передаються як параметри.
# Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх потрібно поміняти місцями.
def sum_func(frm: int, to: int) -> int:
    if frm > to:
        frm ,to = to, frm
    elif frm == to:
        return frm
    sum = 0
    #У завданні написано "межі" але не вказано чи враховуємо ми межі чи ні. Тут я не враховую ні верхню ні нижню.
    for i in range(frm+1,to):
        sum+=i
    return sum
print(sum_func(6,1))
# Завдання 2
# Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
def dobytok_of_list(arg: list) -> int:
    numbers_sum=1
    for i in range(len(arg)):
        numbers_sum *=arg[i]
    return numbers_sum
argsList = [2,3,4,5]
print(dobytok_of_list(argsList))
# Завдання 3
# Напишіть функцію для знаходження мінімуму в списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
def min_of_list(arg: list) -> int:
    min_of = min(arg)
    return min_of
argsList = [2,3,4,1,5,0]
print(min_of_list(argsList))
#
#
# Рівень 2
# Завдання 4
# Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр. Отриманий результат повертається з функції.
def simple_number(arg: list) -> int:
    enkelt=0
    for i in range(len(arg)):
        if arg[i] != 0 == 1 and arg[i]/1 == arg[i] and arg[i]/arg[i]:
            enkelt+=1
    return enkelt
argsList = [2,3,4,5,22,11,10,-1,-2,0]
print(simple_number(argsList))
# Завдання 5
# Напишіть функцію, що видаляє зі списку цілих деяке задане число. З функції потрібно повернути кількість видалених елементів.
#
def delete_of_list(arg: list, number: int) -> int:
    qty = 0
    indexes_for_remove = [i for i, x in enumerate(arg) if x == number]
    for i in reversed(indexes_for_remove):
        arg.pop(i)
        qty+=1
    return qty
argsList = [2,3,2,4,5,22,2,11,2,10,-1,-2,0]
print(delete_of_list(argsList,2))
#
# Рівень 3
# Завдання 6
# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків
def add_lits(*args):
    args = list(args)
    result = args[0]+args[1]
    return result
list1 = [1,2,3]
list2 = [2,3,4]
print(add_lits(list1,list2))
# Завдання 7
# Напишіть функцію, що вираховує ступінь кожного елемента списку цілих. Значення для ступеня передається як параметр, список теж передається як параметр. Функція повертає новий список, що містить отримані результати.

def exponent(args:list,exp:int)-> list:
    new_list = []

    for i in range(len(args)):
        new_list.append(args[i]**exp)
    return new_list

list = [2,3,4]
print(exponent(list,3))