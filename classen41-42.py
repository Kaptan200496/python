books = ['Терен6', 'Драбина2', 'Багатий батько - бідний батько3', 'Крок4', 'Гра5', 'Мастер і Маргарита1']
years = ['2025','1999','2000','2002','2021','1987']

def numbers_head_part(cur_number):
    if len(cur_number) == 8:
        head_part = cur_number[:1]
    else:
        head_part = cur_number[:2]
    return int(head_part)

def sort_years(list_of_years,list_of_books):
    for i in range(0, len(list_of_years) + 1):
        for j in range(i+1,len(list_of_years)):
            if list_of_years[i] > list_of_years[j]:
                list_of_years[i], list_of_years[j] = list_of_years[j], list_of_years[i]
                list_of_books[i], list_of_books[j] = list_of_books[j], list_of_books[i]
    return [list_of_years,list_of_books]


def sort_books(list_of_years,list_of_books):
    for i in range(0, len(list_of_books) + 1):
        for j in range(i+1,len(list_of_books)):
            if list_of_books[i] > list_of_books[j]:
                list_of_books[i], list_of_books[j] = list_of_books[j], list_of_books[i]
                list_of_years[i], list_of_years[j] = list_of_years[j], list_of_years[i]
    return [list_of_books,list_of_years]

while True:
    menu = input('choose punkt of menu sort books/sort years/show list/exit')
    match menu:
        case 'sort years':
            sorting_years_result = sort_years(years,books)
            print(sorting_years_result)
        case 'sort books':
            sorting_books_result = sort_books(years,books)
            print(sorting_books_result)
        case 'show list':
            for i in range(len(years)):
                print(f"Книга {i+1} має рік випуску {years[i]} та назву {books[i]}")
        case 'exit':
            break
        case _:
            continue
