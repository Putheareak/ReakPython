def decipher(string):
    
    #split the string
    x = list(string.split(" "))
    
    #Take first character of the string and convert it into an ascii value
    empty_li = []
    str_em = ""
    for i in range(len(x)):
        str_em = str(ord(x[i][0]))
        empty_li.append(str_em)
    
    #split the string into a character and stored it in the list
    no_list = []
    for a in range(len(x)):
        y = list(''.join(x[a]))
        no_list.append(y)
        
    #Take away the first character and swap the the 1st and last character
    new_str = []
    new_li = []
    for l in range(len(x)):
        sl = slice(1,len(no_list[l]))       #remove the last character
        new_str = no_list[l][sl]
        b = ''.join(new_str)                #join to the character to string
        new_string = b[-1:]+b[1:-1]+b[:1]   # This is to swap between the first and last character
        new_li.append(new_string)

    # concatdinate the two list.
    final_list=[]
    for i in range(0, len(empty_li)):
        final_list.append(empty_li[i] + new_li[i])  #adding a between 2 different list
    x = " ".join(final_list)                #join a list to become a sentence
    return x
    
#decipher("A wise old owl lived in an oak")
print(decipher("A wise old owl lived in an oak"))

Output : Test.assert_equals(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak")
