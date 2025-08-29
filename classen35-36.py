# #3
# # фунція яка прінтує N кількість зірок у рядок за допомогою рекурсивної функції
# # def printing_n_stars(stars_qty,current=0):
# #     if current == stars_qty:
# #         print(current*" * ")
# #         return
# #     else:
# #         printing_n_stars(stars_qty, current+1)
# #
# # n = input('enter n for print n stars')
# # printing_n_stars(int(n),0)
# #4
# # функція яка приймає дві дати та обчислює між ними різницю днів
# months_dict = {
#     0:31,
#     1:28,
#     2:31,
#     3:30,
#     4:31,
#     5:30,
#     6: 31,
#     7: 31,
#     8: 30,
#     9: 31,
#     10: 30,
#     11: 31
# }
# def check_rest_of_part(rest_days,rest_months, years_flag = False)-> int:
#     global months_dict
#     rest_part_of_days = 0
#     for i in range(len(months_dict)):
#         if i + 1 >= int(rest_months):
#             rest_part_of_days += months_dict[i]
#     if years_flag:
#         if int(rest_months) <= 2:
#             rest_part_of_days += 1
#     rest_part_of_days = rest_part_of_days - int(rest_days)
#
#     return rest_part_of_days
#
# def check_year(y):
#     if (int(y) % 4) == 0:
#         return True
#     else:
#         return False
#
# def difference_between_date(first:list, second:list) -> int:
#     global months_dict
#     #  Виявлення більшої дати
#     if (int(second[2]) - int(first[2])) < 0:
#         first, second = second, first
#     #Отримання залишку днів до кінця поточного року обох дат
#     first_part = check_rest_of_part(first[0],first[1], check_year(first[2]))
#     second_part = check_rest_of_part(second[0], second[1], check_year(second[2]))
#
#     result_diff_days = 0
#     print(first_part,second_part)
#     # Якщо рік поточний і цільовий співпадають
#     if (int(second[2]) - int(first[2])) == 0:
#         if (int(second[1]) - int(first[1])) == 0:
#             result_diff_days = first_part - second_part
#         else:
#             result_diff_days =  first_part - second_part
#             if check_year(first[2]) and first[1] == 2:
#                 result_diff_days+=1
#     else:
#         for i in range(first[2],second[2]):
#             for j in range(0,12):
#                 result_diff_days += months_dict[j]
#                 if check_year(i) and j == 2:
#                     result_diff_days+=1
#         result_diff_days = result_diff_days + (first_part - second_part)
#     return result_diff_days
#
# first_date = input('enter first date day,month,year with coma').split(',')
# second_date = input('enter second date day,month,year with coma').split(',')
# TEST DATA
# # first_date = ['10', '1', '2022']
# # second_date = ['25', '10', '2025']
#end test data
# first_date = [int(x) for x in first_date]
# second_date = [int(x) for x in second_date]
# print(first_date,second_date)
# result = difference_between_date(first_date,second_date)
# print(result)
#
# test data
# from datetime import date
#
# date1 = date(2022, 1, 10)
# date2 = date(2025, 10, 25)
#
# difference = date2 - date1
#
# days = difference.days
# print(days)
#end test data