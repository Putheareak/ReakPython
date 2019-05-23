string = input("Enter your secret message: ")
newstr = ""
i = 0
if string == "" :
    print("Nothing to encode")
else :
    while i<len(string):
        #The ascii value of capital letter is from 64 to 90 so if
        #If 65 to 77 we need to add 13
        if ord(string[i]) > 64 and ord(string[i]) < 78:
            cha = chr(ord(string[i])+13)
            newstr += cha
        #if 77 to 90 we need to minus 13
        elif ord(string[i]) < 91 and ord(string[i]) > 76 :
            cha = chr(ord(string[i])-13)
            newstr += cha
        elif ord(string[i]) > 96 and ord(string[i]) < 110:
            cha = chr(ord(string[i])+13)
            newstr += cha
        elif ord(string[i]) > 109 and ord(string[i]) < 123:
            cha = chr(ord(string[i])-13)
            newstr += cha
        else:
            newstr += string[i]
        i += 1
    print(newstr)
