import random
def byk_korova(number:str):
    check_chance = input('enter your number(4 ints)')
    if number == check_chance:
        print("Добре зіграно. Ви вгадали число!")
    else:
        right_qty = 0
        right_position = 0
        checked_array = {'i':[],'j':{}}
        for i in range(len(number)): # 8 7 7 8
            if i in checked_array['i']:
                continue
            else:
                for j in range(len(check_chance)): # 7 8 7 8
                    if checked_array['i'].get(i) == None:
                        if check_chance[j] == number[i]:
                            if i == j:
                                checked_array['j'][j] = True
                                checked_array['i'].append(i)
                                right_position+=1
                            else:
                                checked_array['i'][i] = False
                                right_qty += 1
                    elif checked_array['j'].get(j) == True:
                            continue
                    elif checked_array['j'].get(j) == False:
                        if check_chance[j] == number[i]:
                            if i == j:
                                checked_array['j'][j] = True
        if(right_qty == 4) and (right_position == 4):
            print("Добре зіграно. Ви вгадали число!")
        else:
            print(f"Вгадано {right_qty} цифр, Стоїть на своїх позиціяї {right_position} цифр.")
            byk_korova(number)

#integer_str = str(random.randint(1000,9999))
integer_str = '8778'
byk_korova(integer_str)

# a =  {
#     'i':[1,2,3],
#     'j':{
#         '0':True,
#         '1':False
#     }
# }
# print(a['j'].get('1'))
