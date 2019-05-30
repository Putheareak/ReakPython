def test(x):
    # creating your own library
    my_dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    x = x.replace(" ", "").lower()
    x = list("".join(x))
    new_list = []
    # Used to compare list to dictionary and if it correct it will assign the value into new list
    for i in x:
        for k, j in my_dict.items():
            if i == k:
                new_list.append(j)
    new_list = str(" ".join(new_list))


test("Hello World")
