#1
# Маємо кортеж з цілими числами. Виведіть статистику за кількістю цифр в елементах кортежу. Наприклад:
#
# Одна цифра — 3 елементи;
# Дві цифри — 4 елементи;
# Три цифри — 5 елементів.
# t = (1,2,0,22,33,13,55,123,123,444,12314)
# d = dict()
# for i in t:
#     j=0
#     if i == 1 or i == 0:
#         j+=1
#         d[j] = 1
#     while i>1:
#         i = i/10
#         j+=1
#     if d.get(j):
#         d[j] += 1
#     else:
#         d[j]=1
# print(d)
# #2
# Маємо кортеж з назвами автовиробників (назва виробника може зустрічатися від 0 до N разів).
# Користувач вводить з клавіатури назву виробника та слово для заміни. Замініть в кортежі усі елементи з цією назвою на
# слово для заміни. Збіг за назвою має бути повним.
# t2 = ('vasia','dmytro','babzzina','folc','folc','philipinene','babzzina','babzzina')
# changeElement = input('enter element for change:')
# wordForChange = input('enter word for change:')
# listOfT2 = list(t2)
# for i in range(len(listOfT2)):
#     if listOfT2[i] == changeElement:
#         listOfT2[i] = wordForChange
# t2 = tuple(listOfT2)
# print(t2)
# #3
# У словнику зберігається набір пар: Назва країни -> Столиця. Реалізуйте функ­ціо­наль­ність за
# d3 = {
#     'Ukraine': 'Kyiv',
#     'Parasha':'Moscoviya',
#     'Norway':'Oslo'
# }
# action = input('enter action(del/search/add/update)')
# match action:
#     case 'del':
#         #  видаленням,
#         deletabelElement = input('enter deletable land')
#         del d3[deletabelElement]
#         print(d3)
#     case 'search':
#         #  пошуком,
#         searchableLand = input('enter land:')
#         capital3 = input('enter capital:')
#
#         for land,capital in d3.items():
#             if(land == searchableLand):
#                 print(land + ' - '+ capital)
#             if(capital == capital3):
#                 print(land + ' - '+ capital)
#         ## Або якщо потрібно просто столицю то
#         searchableCapital = d3[searchableLand]
#         print(searchableCapital)
#     case 'add' | 'update':
#         # додаванням/заміною.
#         searchableLand = input('enter land:')
#         capital31 = input('enter capital:')
#         d3[searchableLand] = capital31
#         print(d3)
#     case _:
#         print("No match")


