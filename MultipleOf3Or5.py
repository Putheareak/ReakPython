def test(x):
    sum = 0
    arr = []
    for i in range(1,x):
        if i % 3 == 0 or i % 5 == 0:
            arr.append(i)
    for ele in arr:
        sum = sum + ele
    return sum
print(test(10))
