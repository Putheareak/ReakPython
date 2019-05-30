def test(x):
    ori = x
    x = str(x)
    sum = 0
    lenght = len(x)
    x = list("".join(x))
    x =[int(i) for i in x]
    for ele in x:
        sum = sum + (ele**lenght)
    if sum == ori:
        return True
    return False
print(test(4887))
