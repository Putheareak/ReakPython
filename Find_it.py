#Find the most odd number
def find_it(seq):
    odd = []
    for i in seq:
        if i%2 == 0:
            continue
        else:
            odd.append(i)
    my_dict = {}
    for i in range(len(odd)):
        my_dict[odd[i]]=odd.count(odd[i])
    sorted(my_dict.items(), key = 
             lambda kv:(kv[1], kv[0]))
    return list(my_dict.keys())[-1]
