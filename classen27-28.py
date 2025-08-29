# Завдання 1
# Створіть програму, що містить інформацію про відомих баскетболістів.
# Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.
#
# match_action = input('enter your action(delete/edit/add/search)')
# resultObject = {
#     'kapitoshkin':{
#         'name':'vasia',
#         'second_name':'evhenievich',
#         'height':'175'
#     }
# }
# match match_action:
#     case 'delete':
#         deletable_surname = input('enter deletable surname')
#           if(resultObject2.get(deletable_surname) != None):
#               del resultObject[deletable_surname]
#           else:
#             print('Такого немає у словнику')


#     case 'add':
#         name = input('enter name')
#         surname = input('enter surname')
#         second_name = input('enter second name')
#         height = input('enter height')
#         resultObject[surname] = {
#             'name':name,
#             'second_name':second_name,
#             'height':height
#         }
#     case 'search':
#         surname = input('enter surname for search')
#         print(resultObject[surname])
#     case 'edit':
#         editable_surname = input('enter editable surname')
#         editable_name = input('enter name')
#         editable_second_name = input('enter second name')
#         editable_height = input('enter height')
#         resultObject[editable_surname] = {
#             'name': editable_name,
#             'second_name': editable_second_name,
#             'height': editable_height
#         }
#
# print(resultObject)
# Завдання 2
# Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку. Реалізуйте можливість додавати, видаляти, знахо­дити та змінювати дані. Використовуйте словник для збереження інформації.
# match_action2 = input('enter your action(delete/edit/add/search)')
# resultObject2 = {
#     'have':"мати"
# }
# match match_action2:
#     case 'delete':
#         deletable_word = input('enter deletable word')
#         if(resultObject2.get(deletable_word) != None):
#             del resultObject2[deletable_word]
#         else:
#             print('Такого слова немає у словнику')
#     case 'add':
#         word = input('enter word')
#         translate = input('enter word')
#         resultObject2[word] = translate
#     case 'search':
#         word = input('enter word for search')
#         if (resultObject2.get(word) != None):
#             print(resultObject2[word])
#         else:
#             print('Такого слова немає у словнику')
#     case 'edit':
#         editable_word = input('enter editable word')
#         editable_translate = input('enter translate')
#         resultObject2[editable_word] = editable_translate
#
# print(resultObject2)
# Завдання 3
# Створіть програму «Фірма», яка зберігає інформацію про працівників: ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.
# match_action3 = input('enter your action(delete/edit/add/search)')
# resultObject3 = {
#     'kapitoshkin':{
#         'name':'vasia',
#         'second_name':'evhenievich',
#         'phone':'175',
#         'email':'evqwe@gmail.com',
#         'place':'director',
#         'accountnumber':'56',
#         'skype':'biburishvili'
#     }
# }
# match match_action3:
#     case 'delete':
#         deletable_word = input('enter deletable word')
#         if(resultObject3.get(deletable_word) != None):
#             del resultObject3[deletable_word]
#         else:
#             print('Такого слова немає у словнику')
#     case 'add':
#         name3 = input('enter name')
#         surname3 = input('enter surname')
#         second_name3 = input('enter second name')
#         height3 = input('enter height')
#         phone3 = input('enter phone')
#         email3 = input('enter email')
#         place3 = input('enter height')
#         accountnumber3 = input('enter accountnumber')
#         skype3 = input('enter skype')
#
#         resultObject3[surname3] = {
#             'name':name3,
#             'second_name':second_name3,
#             'height':height3,
#             'phone': phone3,
#             'email': email3,
#             'place': place3,
#             'accountnumber': accountnumber3,
#             'skype': skype3
#         }
#     case 'search':
#         surname3 = input('enter surname for search')
#         if (resultObject3.get(surname3) != None):
#             print(resultObject3[surname3])
#         else:
#             print('Такої фамілії немає у словнику')
#     case 'edit':
#         editable_ansatt = input('enter editable ansatt surname')
#         name3 = input('enter name')
#         second_name3 = input('enter second name')
#         height3 = input('enter height')
#         phone3 = input('enter phone')
#         email3 = input('enter email')
#         place3 = input('enter place')
#         accountnumber3 = input('enter accountnumber')
#         skype3 = input('enter skype')
#         resultObject3[editable_ansatt] = {
#             'name': name3,
#             'second_name': second_name3,
#             'height': height3,
#             'phone': phone3,
#             'email': email3,
#             'place': place3,
#             'accountnumber': accountnumber3,
#             'skype': skype3
#         }
#
# print(resultObject3)
# Завдання 4
# Створіть програму «Книжкова колекція», яка зберігає інформацію про книги: автор, назва книги, жанр, рік випуску, кількість сторінок, видавництво.
# Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані.
# Використовуйте словник для збереження інформації.
# match_action4 = input('enter your action(delete/edit/add/search)')
# resultObject4 = {
#     'leleka':{
#         'author':'vasia',
#         'genre':'horror',
#         'year':'1715',
#         'number_of_page':'2222',
#         'publishing':'lelekatv',
#     }
# }
# match match_action4:
#     case 'delete':
#         deletable_book = input('enter deletable book')
#         if(resultObject4.get(deletable_book) != None):
#             del resultObject4[deletable_book]
#         else:
#             print('Такої книги немає у словнику')
#     case 'add':
#         booksname = input('enter booksname')
#         author = input('enter author')
#         genre = input('enter genre')
#         year = input('enter second year')
#         number_of_page = input('enter number_of_page')
#         publishing = input('enter publishing')
#
#         resultObject4[booksname] = {
#             'author':author,
#             'genre':genre,
#             'year':year,
#             'number_of_page': number_of_page,
#             'publishing': publishing,
#         }
#     case 'search':
#         booksname = input('enter booksname for search')
#         if (resultObject4.get(booksname) != None):
#             print(resultObject4[booksname])
#         else:
#             print('Такої фамілії немає у словнику')
#     case 'edit':
#         editable_booksname = input('enter editable booksname')
#         author = input('enter author')
#         genre = input('enter genre')
#         year = input('enter year')
#         number_of_page = input('enter number_of_page')
#         publishing = input('enter publishing')
#         resultObject4[editable_booksname] = {
#             'author': author,
#             'genre': genre,
#             'year': year,
#             'number_of_page': number_of_page,
#             'publishing': publishing,
#         }
#
# print(resultObject4)