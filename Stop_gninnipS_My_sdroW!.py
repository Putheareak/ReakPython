def test(x):
    x = list(x.split())
    new_arr = []
    for i in x:
        if len(i) > 4:
            i=i[::-1]
            new_arr.append(i)
        else:
            new_arr.append(i)
    new_arr = [" ".join(new_arr)]
    return new_arr[0]
print(test("This is another test"))

