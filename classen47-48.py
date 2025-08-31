# #nomer 5
# import json
# while True:
#     print("1.Додати замовлення \n"
#           "2.Переглянути всі замовлення\n"
#           "3.Пошук замовлення за номером\n"
#           "4.Оновити замовлення\n"
#           "5.Видалити замовлення\n"
#           "6.Вихід\n")
#     menu = input('Виберіть пункт: ')
#     match menu:
#         case "1":
#             orders_number = input('Введіть номер замовлення:')
#             name = input('Введіть назву товару:')
#             qty = input('Введіть кількість товару:')
#             price = input('Введіть ціну на товар:')
#             result_row = {
#                 "Номер ордера":orders_number,
#                 "Інформація про товар":{
#                     "Назва товару": name,
#                     "Кількість товару": qty,
#                     "Ціна на товар": price
#                 }
#             }
#             with open("orders.txt","a+", encoding='utf-8') as f:
#                 f.write(json.dumps(result_row, ensure_ascii=False)+"\n")
#             print(result_row)
#         case "2":
#             with open("orders.txt","r+", encoding='utf-8') as f:
#                 lines = f.readlines()
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     #print(i)
#                     print(f"Номер ордера:{line["Номер ордера"]}, Назва товару:{line["Інформація про товар"]["Назва товару"]},Кількість товару:{line["Інформація про товар"]["Кількість товару"]},Ціна на товар:{line["Інформація про товар"]["Ціна на товар"]}")
#         case "3":
#             target_order = input('Введіть номер ордеру який ви хочете знайти:')
#             with open("orders.txt", "r+", encoding='utf-8') as f:
#                 lines = f.readlines()
#                 print(lines)
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Номер ордера"] == target_order:
#                         print(f"Номер ордера:{line["Номер ордера"]}, Назва товару:{line["Інформація про товар"]["Назва товару"]},Кількість товару:{line["Інформація про товар"]["Кількість товару"]},Ціна на товар:{line["Інформація про товар"]["Ціна на товар"]}")
#         case "4":
#             target_order = input('Введіть номер ордеру який ви хочете змінити:')
#             with open("orders.txt", "r+", encoding='utf-8') as f:
#                 lines = f.readlines()
#                 print(lines)
#                 f.seek(0)
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Номер ордера"] == target_order:
#                         new_name = input('Введіть назву товару або нічого якщо не хочете змінювати:')
#                         new_qty = input('Введіть кількість товару або нічого якщо не хочете змінювати:')
#                         new_price = input('Введіть ціну на товар або нічого якщо не хочете змінювати:')
#                         result_row = {
#                             "Номер ордера": line["Номер ордера"],
#                             "Інформація про товар": {
#                                 "Назва товару": line["Інформація про товар"]["Назва товару"],
#                                 "Кількість товару": line["Інформація про товар"]["Кількість товару"],
#                                 "Ціна на товар": line["Інформація про товар"]["Ціна на товар"]
#                             }
#                         }
#                         if new_name != "":
#                             result_row["Інформація про товар"]["Назва товару"] = new_name
#                         if new_qty != "":
#                             result_row["Інформація про товар"]["Кількість товару"] = new_qty
#                         if new_price != "":
#                             result_row["Інформація про товар"]["Ціна на товар"] = new_price
#                         line = result_row
#                         print(lines)
#
#                     f.write(json.dumps(line, ensure_ascii=False) + "\n")
#                     print(line)
#         case "5":
#             target_order = input('Введіть номер ордеру який ви хочете змінити:')
#             file = open('orders.txt','r', encoding='utf-8')
#             lines = file.readlines()
#             with open("orders.txt", "w+", encoding='utf-8') as f:
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Номер ордера"] != target_order:
#                         f.write(json.dumps(line, ensure_ascii=False) + "\n")
#                     print(line)
#         case "6":
#             break
#         case _:
#             print("Виберіть вірний пункт з меню.")
#

#number 6
# import json
# while True:
#     print("1.Додати студента \n"
#           "2.Переглянути всіх студентів\n"
#           "3.Пошук студлента за ім'ям\n"
#           "4.Оновити дані про студента\n"
#           "5.Видалити інформацію про студента\n"
#           "6.Вихід\n")
#     menu = input('Виберіть пункт: ')
#     match menu:
#         case "1":
#             name = input("Введіть ім'я:")
#             kurs_title = input('Введіть назву курсу:')
#             avarage = input('Введіть середній бал:')
#             result_row = {
#                 "Ім'я":name,
#                 "Інформація про студента":{
#                     "Назва курсу": kurs_title,
#                     "Середній бал": avarage
#                 }
#             }
#             with open("students.txt","a+", encoding='utf-8') as f:
#                 f.write(json.dumps(result_row, ensure_ascii=False)+"\n")
#         case "2":
#             with open("students.txt","r+", encoding='utf-8') as f:
#                 lines = f.readlines()
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     print(f"Ім'я студента:{line["Ім'я"]}, Назва курсу:{line["Інформація про студента"]["Назва курсу"]},Середній бал:{line["Інформація про студента"]["Середній бал"]}")
#         case "3":
#             target_name = input("Введіть ім'я студента якого ви хочете знайти:")
#             with open("students.txt", "r+", encoding='utf-8') as f:
#                 lines = f.readlines()
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Ім'я"] == target_name:
#                         print(f"Ім'я студента:{line["Ім'я"]}, Назва курсу:{line["Інформація про студента"]["Назва курсу"]},Середній бал:{line["Інформація про студента"]["Середній бал"]}")
#         case "4":
#             target_name = input("Введіть ім'я студента якого ви хочете змінити:")
#             file = open('students.txt', 'r', encoding='utf-8')
#             lines = file.readlines()
#             with open("students.txt", "w+", encoding='utf-8') as f:
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Ім'я"] == target_name:
#                         new_title = input('Введіть назву курсу або нічого якщо не хочете змінювати:')
#                         new_average = input('Введіть середній бал або нічого якщо не хочете змінювати:')
#                         result_row = {
#                             "Ім'я": line["Ім'я"],
#                             "Інформація про студента": {
#                                 "Назва курсу": line["Інформація про студента"]["Назва курсу"],
#                                 "Середній бал": line["Інформація про студента"]["Середній бал"],
#                             }
#                         }
#
#                         if new_title != "":
#                             result_row["Інформація про студента"]["Назва курсу"] = new_title
#                         if new_average != "":
#                             result_row["Інформація про студента"]["Середній бал"] = new_average
#                         line = result_row
#                     f.write(json.dumps(line, ensure_ascii=False) + "\n")
#             file.close()
#         case "5":
#             target_name = input("Введіть ім'я студента якого ви хочете змінити:")
#             file = open('students.txt','r', encoding='utf-8')
#             lines = file.readlines()
#             with open("students.txt", "w+", encoding='utf-8') as f:
#                 for i in range(len(lines)):
#                     line = json.loads(lines[i])
#                     if line["Ім'я"] != target_name:
#                         f.write(json.dumps(line, ensure_ascii=False) + "\n")
#             file.close()
#         case "6":
#             break
#         case _:
#             print("Виберіть вірний пункт з меню.")


