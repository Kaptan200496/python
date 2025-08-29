import random
globaldict = {}
qty = 1
def check_num_and_position(stack:str,pos:int,num:str):
    global globaldict

    for i in range(len(stack)):
        if stack[i] == num:
            if globaldict[i].get(stack[i]) == None:
                if i == pos:
                    globaldict[i][stack[i]] = True
                    return 'pos True'
                else:
                    globaldict[i][stack[i]] = False
                    return 'pos False'
            elif globaldict[i].get(stack[i]) == False:
                continue
        else:
            continue
    return False


def byk_korova(number:str):
    global qty
    for n in range(len(number)):
        globaldict[n] = {number[n]:None}

    right_qty = 0
    right_position = 0

    check_chance = input('enter your number(4 ints)')
    for j in range(len(check_chance)):
        res = check_num_and_position(number,j,check_chance[j])
        if res == "pos False":
            right_qty += 1
        elif res == "pos True":
            right_qty += 1
            right_position += 1
    if(right_qty == 4) and (right_position == 4):
        print("Добре зіграно. Ви вгадали число!")
    else:
        print(f"Вгадано {right_qty} цифр, Стоїть на своїх позиціяї {right_position} цифр.")
        qty +=1
        byk_korova(number)

    res = qty
    return res

integer_str = str(random.randint(1000,9999))
#integer_str = '8778'
result = byk_korova(integer_str)
print(f"Ви зробили {result} спроб")
