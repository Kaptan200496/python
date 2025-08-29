numbers = ['116264223', '46264223', '36264223', '126264223', '56264223', '86264223', '96264223', '106264223', '16264223', '76264223']
ids = [11, 4, 3, 12, 5, 8, 9, 10, 1, 7]

def numbers_head_part(cur_number):
    if len(cur_number) == 8:
        head_part = cur_number[:1]
    else:
        head_part = cur_number[:2]
    return int(head_part)
def sort_ids(list_of_ids,list_of_numbers):
    for i in range(0, len(list_of_ids) + 1):
        for j in range(i+1,len(list_of_ids)):
            if list_of_ids[i] > list_of_ids[j]:
                list_of_ids[i], list_of_ids[j] = list_of_ids[j], list_of_ids[i]
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
    return [list_of_ids,list_of_numbers]
def sort_numbers(list_of_ids,list_of_numbers):
    for i in range(0, len(list_of_numbers) + 1):
        for j in range(i+1,len(list_of_numbers)):
            cur_i = numbers_head_part(list_of_numbers[i])
            cur_j = numbers_head_part(list_of_numbers[j])
            if cur_i > cur_j:
                list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]
                list_of_ids[i], list_of_ids[j] = list_of_ids[j], list_of_ids[i]
    return [list_of_numbers,list_of_ids]

while True:
    menu = input('choose punkt of menu sort numbers/sort ids/show list/exit')
    match menu:
        case 'sort ids':
            sorting_ids_result = sort_ids(ids,numbers)
            print(sorting_ids_result)
        case 'sort numbers':
            sorting_numbers_result = sort_numbers(ids, numbers)
            print(sorting_numbers_result)
        case 'show list':
            for i in range(len(ids)):
                print(f"Користувач {i+1} має айді {ids[i]} та номер телефону {numbers[i]}")
        case 'exit':
            break
        case _:
            continue
