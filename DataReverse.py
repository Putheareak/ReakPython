def data_reverse(data):
    s = [str(i) for i in data]          #convert number into string
    new_list = []
    empty=[]
    new_list = [s[x:x+8] for x in range(0,len(s),8)] #make a sublist of 8 character
    new_list = new_list[::-1]
    final_list=[]
    for ele in range(len(new_list)):
        final_list = final_list + new_list[ele]
    final = [int(e) for e in final_list]
    print(final)
