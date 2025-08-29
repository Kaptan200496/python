level = int(input('enter lvl for visualisation'))
if level == 1:
    # i
    for x in range(10,1,-1):
        print(" * "*(x-1))
    # б
    for x in range(1,10):
        print(" * "*(x-1))
    # к
    w = 10
    for x in range(1,10,1):
        print("  "*(w-x)+" *"*x)
    # a
    w = 10
    for x in range(1,10,1):
        print("  "*(x-1)+" *"*(w-x))
if level == 2:
    # # Ж1
    y=0
    for x in range(10, 0, -1):
        if(x>y):
            print(" * " * (y+1) + "  " * (x - y))
        elif(y>x):
            print(" * " * (x) + "  " * (y - x))
        y += 1

    # # З
    y = 10
    for x in range(0, 10, 1):
        if (x >= y):
            print(" " * (x - y)+" *" * (y))
        elif (y >= x):
            print(" " * (y - x) + " *" * (x))
        y -= 1

    # # В
    w = 11
    h = 10
    for i in range(0, (h//2+1)):
        print((i*2)*" "+(w-i*2)*" *"+(i*2)*" ")
    # Г
    w = 11
    h = 10
    for i in range((h//2+1),0, -1):
        print((i*2)*" "+(w-i*2)*" *"+(i*2)*" ")
if level == 3:
    # # Д
    w = 11
    h = 10
    for i in range(0, (h//2+1)):
        print((i*2)*" "+(w-i*2)*" *"+(i*2)*" ")
    w = 11
    h = 11
    for i in range((h//2),-1, -1):
        print((i*2)*" "+(w-i*2)*" *"+(i*2)*" ")

    # e
    w = 11
    h = 10

    for i in range(0, (h+1), 1):
        if(i<=5):
            print((i)*"*"+(w-i*2)*" "+(i)*"*")
        elif (i > 5):
            print((i-(-w + i * 2))  * "*" + (-w + i * 2) * " " + (i-(-w + i * 2)) * "*")
