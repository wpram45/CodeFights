def avoidObstacles(inputArray):

    start=2
    counter=0
    found=False
    while found==False and start <41:
        counter=0
        #print(start,counter)

        
        for i in inputArray:
            if i%start!=0:
                counter+=1
                
            else:
                start+=1
                
        if counter==len(inputArray):
            found=True
            break
                
                
    return start
