# 


arr1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
arr2="abcdefghijklmnopqrstuvwxyz"
arr3="0123456789"
arr4=['!','@','#','$','%','^','&','*','(',')','_','+','=','-','{','}','[',']',';'':',"'",'"',',','.','<','>','?','/','|','~','`','"']


def validate_password(ip):

    len1=len(ip)
    list1=[]
    validcnt=0

    if len1<8:
        list1.append("Minimum Length")

    else:
        validcnt=validcnt+1
    
    upchcnt=0
    for c in ip:
        if c in arr1:
            upchcnt+=1

    if upchcnt<=0:
        list1.append("Uppercase Letter")

    else:
        validcnt=validcnt+1
    
    lowchcnt=0
    
    for c in ip:
        if c in arr2:
            lowchcnt+=1

    if lowchcnt<=0:
        list1.append("Lowercase Letter")
    
    else:
        validcnt=validcnt+1
    
    dignotcnt=0

    for c in ip:
        if c not in arr3:

            dignotcnt+=1

    if dignotcnt<=0:
        list1.append("Digit")

    else:
        validcnt=validcnt+1
        
    speccharnotcnt=0

    for c in ip:
        if c not in arr4:
            speccharnotcnt+=1
    
    if speccharnotcnt<=0:
        list1.append("Special Character")

    else:
        validcnt=validcnt+1


    spacecnt=0 
    for c in ip:
        if c==" ":
            spacecnt+=1
    
    if spacecnt>=1:

        list1.append("No Spaces")
    else:
        validcnt=validcnt+1

    if validcnt==6:
        return f"VALID score: {validcnt}"
    
    else:
        return f"INVALID special score: {validcnt}"
        # return list1
    

if __name__=="__main__":
    ip="Campus25"

    res=validate_password(ip)

    print(res)

    