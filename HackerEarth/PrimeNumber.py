N = int(input())
final = ""
for i in range(N+1):
    if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           final = final + " "+ str(i)
print(final.lstrip(" "))
