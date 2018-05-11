def isIPv4Address(inputString):
    isipv4=False
    
    try:
        arr=list(map(int,inputString.split(".")))
        
        if len(arr)!=4:
            return False
                 
        for i in arr:
            if i >-1 and i< 256:
                 isipv4=True
            
            else:
                 isipv4=False
                 
                 return isipv4
            
        return isipv4
    except:
            return False
