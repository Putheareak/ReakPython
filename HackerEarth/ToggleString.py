x = input("")
x = list(x)
final = []   
for i in range(len(x)):
   if x[i].islower():
      final.append(x[i].upper())
   else:
      final.append(x[i].lower())
print("".join(final))
