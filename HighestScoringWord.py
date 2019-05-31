def test(x):
    x = x.split()
    x = [i.lower() for i in x]
    my_list = []
    emp = []
    new = []
    res = 0
    for i in x:
        my_list.append(list("".join(i)))
    for i in range(len(my_list)):
        for ele in range(len(my_list[i])):
            my_list[i][ele]=ord(my_list[i][ele])- 96 
            res = res + my_list[i][ele]
        new.append(res)
        res = 0
    final = sorted(new)
    dic = dict(zip(x,new))
    final = list(final[-1::])
    for i in final:
        for k, j in dic.items():
            if i == j:
                emp.append(k)
    return emp[0]
        
    
print(test('man i need a taxi up to ubud'))
