def xor(bit1,bit2):
    return "".join(['0' if bit1[i]==bit2[i] else '1' for i in  range(len(bit1))])

# print(xor('1001','1011'))


dataword ='1001110'
poly ='1011'
first = dataword[0:4]
rest = dataword[4:]
def mod2div(first,rest,poly):
    if rest=="" :
        return ( first if  first[0]=='0' else xor(first,poly))[1:]
    else:
        if(first[0]=='1'):
            return mod2div(xor(first,poly)[1:]+rest[0],rest[1:],poly)
        else:
            return mod2div(first[1:]+rest[0],rest[1:],poly)

print(mod2div(first,rest,poly))