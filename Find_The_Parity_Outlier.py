def test(x):
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
        return even_list[0]
    else:
        return odd_list[0]
print(test([160, 3, 1719, 19, 11, 13, -21]))
