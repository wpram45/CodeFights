def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
       
    
    #strongest arm is left
    if max(yourLeft,yourRight) ==yourLeft:
        
        #friend weak arm is left
        if min(friendsLeft,friendsRight)==friendsLeft:
            #compare weaks
            if yourRight==friendsLeft:
                return True
            else:
                return False
        elif min(friendsLeft,friendsRight)==friendsRight:
            #compare weaks
            if yourRight==friendsRight:
                return True
            
            else:
                return False
    ##strongest arm is right
    elif max(yourLeft,yourRight)==yourRight:
        if min(friendsLeft,friendsRight)==friendsLeft:
            #compare weaks
            if yourLeft==friendsLeft and yourRight==friendsRight:
                return True
            else:
                return False
        elif min(friendsLeft,friendsRight)==friendsRight:
            #compare weaks
            if yourLeft==friendsRight and yourRight==friendsLeft:
                return True
            
        
        
            else:
                return False
        
    
        
