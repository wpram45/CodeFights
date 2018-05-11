def palindromeRearranging(inputString):
    my_dict={}
    answer=True
    even=False
    counter=0
    if len(inputString)%2==0:
        even=True
    
    for i in inputString:
        if i not in my_dict:
            my_dict[i]=1
        else:
            my_dict[i]+=1
        
    print(my_dict)
    
    
    if even==True:
        for i in my_dict:
            if my_dict[i]%2==0:
                pass
            else:
                answer=False
        return answer
    
    else:
        for i in my_dict:
            if my_dict[i]%2==0:
                pass
            else:
                counter+=1
                
        
    if counter==1:
        answer=True
        
        return answer
    else:
        answer=False
        return answer
