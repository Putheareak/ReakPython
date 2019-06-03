def test(x):
    x = x.split()
    em = []
    emp = ""
    for i in x:
        for j in range(len(i)):
            if j % 2 == 0:
                emp = emp + i[j].upper()
            else:
                emp = emp + i[j].lower()
        em.append(emp)
        emp = ""
    em = [" ".join(em)]
    return em[0]

print(test('Weird string case'))
