#code
def duplicate_count(text):
    text = text.lower()
    print(text)
    x = list(''.join(text))
    my_dict = {}
    total = 0
    empty_list = []
    for i in range(len(x)):
        my_dict[x[i]] = x.count(x[i])
    a = list(my_dict.values())
    for ele in a:
        if ele > 1 :
            total = total + 1
    return total
print(duplicate_count("indIvisibIlitUu"))
