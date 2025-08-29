#Рівень 1
# Завдання 1
# Напишіть програму, яка запитує в користувача три рядки і записує їх у файл data.txt, кожен рядок має бути записаний на новому рядку.
# first_row = input('enter first row:')
# second_row = input('enter second row:')
# third_row = input('enter third row:')
# rows = [first_row,second_row,third_row]
# file = open("data.txt", "w+")
# for line in rows:
#     print(line)
#     file.write(line+"\n")
# f = open("data.txt", "r")
# print(f.read())
# f.close()
# Завдання 2
# Напишіть програму, яка перевіряє, чи існує файл data.txt, і виводить відповідне повідомлення. Якщо файл існує, відкрийте його і виведіть кожен другий рядок у консоль.
# try:
#     i = 1
#     with open("data.txt", "r+") as f:
#         flag = True
#         while flag:
#             a = f.readline()
#             if not a:
#                 flag = False
#             if i%2 == 0:
#                 print(a)
#             i+=1
# except Exception as e:
#     print(f"Щось пішло не так {e}")

# Рівень 2
# Завдання 3
# Напишіть програму, яка читає файл data.txt, фільтрує рядки, що містять слово "Python", і записує їх у новий файл filtered.txt.
# try:
#     f2 = open("filtered.txt", "w+")
#     with open('data.txt', 'r+') as f1:
#         lines = f1.readlines()
#         for line in lines:
#             print(line)
#             if "python" in line or "Python" in line:
#                 f2.write(line)
#     print(f2.read())
# except Exception as e:
#     print(e)
# finally:
#     f2.close()
# Завдання 4
# Напишіть програму, яка запитує в користувача ім'я файлу, відкриває його, видаляє всі цифри з вмісту і зберігає результат у новому файлі cleaned.txt.
# import re
# name_of_file = input('enter name of file:')
# try:
#     fil1 = open('cleaned.txt', 'w+')
#     with open(name_of_file, "r+") as fil:
#         text = fil.read()
#         result = re.sub(r"\d+", "", text)
#         fil1.write(result)
# except Exception as e:
#     print(e)
# finally:
#     fil1.close()
# Рівень 3
# Завдання 5
# Напишіть програму, яка аналізує файл log.txt, визначає 10 найпоширеніших слів, що зустрічаються найчастіше, і записує їх разом з їхньою частотою в word_stats.txt.
# name_of_file5= input('enter name of file:')
# try:
#     counter_array = {}
#     text5 = None
#     with open(name_of_file5, "r+") as f:
#         text5 = f.read().split(' ')
#
#     for i in range(0,len(text5)):
#         print(text5[i],counter_array.get(text5[i]))
#         if counter_array.get(text5[i]) == None:
#             counter_array[text5[i]] = 0
#         else:
#             counter_array[text5[i]] += 1
#     print(text5, counter_array)
#     fil5 = open('word_stats.txt', 'w+')
#     for key,value in counter_array.items():
#         fil5.write(key+'='+str(value)+"\n")
# except Exception as e:
#     print(e)
# finally:
#     fil5.close()
# Завдання 6
# Напишіть програму, яка читає файл data.txt, інвертує порядок рядків і зберігає результат у новому файлі reversed.txt.
# Наприклад, якщо data.txt містить:
#
# Перший рядок
# Другий рядок
# Третій рядок
#
# Після виконання програми reversed.txt має містити:
#
# Третій рядок
# Другий рядок
# Перший рядок
# try:
#     fil6 = open('reversed.txt','w+')
#     with open("data.txt", "r+") as f:
#         text6 = f.readlines()
#         buffer_text = text6
#         for i in range(len(text6)):
#             fil6.write(buffer_text.pop())
# except Exception as e:
#     print(e)
# finally:
#     fil6.close()
#     print('vikonano')