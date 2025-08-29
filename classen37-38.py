# #Завдання 1
# Відсортуйте перші дві третини списку в порядку зростання, якщо середнє арифметичне всіх елементів більше за нуль;
#  якщо ні — тільки першу третину. Решту списку не сортуйте, а розташуйте у зворотному порядку.
#
#
# def sortering(sorted_data:list) -> list:
#     for i in range(0,len(sorted_data)+1):
#         for j in range(i+1,len(sorted_data)):
#             if sorted_data[i] > sorted_data[j]:
#                 sorted_data[i], sorted_data[j] = sorted_data[j], sorted_data[i]
#     return sorted_data
#
#
# def f_sort(ar_data:list):
#     avarage = sum(ar_data)/len(ar_data)
#     if avarage > 0:
#         target_list = ar_data[:int((len(ar_data)/3)*2)]
#         rest_of = ar_data[int((len(ar_data)/3)*2):]
#     else:
#         target_list = ar_data[:int(len(ar_data)/3)]
#         rest_of = ar_data[int(len(ar_data) / 3):]
#     sortered_list = sortering(target_list)
#     print(sortered_list)
#     sortered_list.extend(sorted(rest_of, reverse=True))
#
#     return sortered_list
#
# test_data = [1,3,2,5,4,-5,10,20]
#
# print(f_sort(test_data))
# Завдання 2
# Написати програму «Успішність».
# Користувач вводить 10 оцінок студента. Оцінки від 1 до 12. Реалізуйте меню для користувача:
# виведення оцінок (виведення вмісту списку);
# перескладання іспиту (користувач вводить номер елемента списку та нову оцінку);
# отримання стипендії (стипендію отримують, якщо середній бал не нижче 10.7);
# виведення відсортованого списку оцінок: за зростанням або спаданням.
# def show(show_data):
#     print(show_data)
# def retest(retest_data, pos, evaluation):
#     retest_data[pos-1] = evaluation
#     return retest_data
# def degree(current_list):
#     avarage = sum(current_list)/len(current_list)
#     return avarage
# input_data = [10,7,4,1,8,9,3,5,11,12]
# menu_choose = input('enter data show/retest/degree/sort')
# match menu_choose:
#     case 'show':
#         show(input_data)
#     case 'retest':
#         number_for_change = int(input('enter number of element'))
#         evaluation_for_change = int(input('enter new evaluation'))
#         result = retest(input_data, number_for_change, evaluation_for_change)
#         print(result)
#     case 'degree':
#         if degree(input_data) >= 10.7:
#             print('Є степендія!')
#         else:
#             print('Немає степендії')
#     case 'sort':
#         method = input('choose sort method up or down')
#         match method:
#             case 'up':
#                 print(sorted(input_data))
#             case 'down':
#                 print(sorted(input_data, reverse=True))

# Завдання 3
# Напишіть програму для сортування списку методом удосконаленого буль­баш­ко­вого сортування.
# Удосконалення полягає в тому,
# щоб аналізувати кількість перестановок на кожному кроці.
# Якщо ця кількість дорівнює нулю, то продов­жувати сортування немає сенсу — список відсортовано.

# input_data = [10,7,4,1,8,9,3,5,11,12]
#
# def sortering(sorted_data:list) -> list:
#     for i in range(0,len(sorted_data)+1):
#         flag = False
#         for j in range(i+1,len(sorted_data)):
#             if sorted_data[i] > sorted_data[j]:
#                 sorted_data[i], sorted_data[j] = sorted_data[j], sorted_data[i]
#                 flag = True
#         if not flag:
#             print('Сортування завершене')
#             break
#     return sorted_data
# print(input_data)
# sortering_result= sortering(input_data)
# print(sortering_result)