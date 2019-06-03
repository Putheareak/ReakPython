def test(x):
    check = True
    if x == "":
        return False
    x = x.split('.')
    for i in x:
        if i.isdigit() == False:
            check = False
            break
        elif len(i) == 1:
            if int(i) == 0:
                check = True
            if len(x) != 4:
                check = False
                break
        else:
            if int(i[0]) == 0:
                check = False
                break
            elif int(i) > 255 or int(i) < 0:
                check = False
                break
            elif len(x) != 4:
                check = False
                break
            
    return check


print(test("1.2.3.4.5"))
print(test(""))
print(test("a.b.c.5"))
