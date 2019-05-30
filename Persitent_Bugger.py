def test(x):
    if x<10:
        return 0
    else:
        check = True
        counter = 1
        res = 1
        while(check):
            x = str(x)
            print(x)
            x = list("".join(x))
            print(x)
            x = [int(i) for i in x]
            for i in x:
                res = res * i
            x = res
            res = 1
            if x >= 10:
                counter += 1
                print(x)
                continue
            else:
                check = False
            return counter
print(test(25))
