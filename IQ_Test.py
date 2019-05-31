def test(x):
    x=list(x.split())
    x = [int(i) for i in x]
    odd_count = 0
    even_count = 0
    odd_list = []
    even_list = []
    for ele in x:
        if ele % 2 == 0:
            even_count += 1
            even_list.append(ele)
        else:
            odd_count += 1
            odd_list.append(ele)
    if odd_count > even_count:
        return x.index(even_list[0]) + 1
    else:
        return x.index(odd_list[0]) + 1
print(test("2 4 7 8 10"))
print(test("1 2 1 1"))
