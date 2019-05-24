def reverse_number(n):
    if n<0 :
        n = str(n)
        n = n.lstrip('-')
        n = int(n[::-1])*-1
        return n
    else :
        return int(str(n)[::-1])
        
