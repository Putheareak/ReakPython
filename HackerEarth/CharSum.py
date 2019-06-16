x = input()
sum1 = 0
x = list(x)
for i in range(len(x)):
    num = ord(x[i])-96
    sum1 = sum1 + num
print(sum1)
