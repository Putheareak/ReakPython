def test(x):
    check = True
    while(check):
        x = str(x)
        x = list("".join(x))
        x = [int(i) for i in x]
        res = sum(ele for ele in x)
        x = res
        if x > 10:
            continue
        else:
            check = False
        return x
print(test(456))
