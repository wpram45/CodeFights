def chessBoardCellColor(cell1, cell2):
    my_str="ABCDEFGH"
    if cell1[0]==cell2[0]:
        if abs(int(cell1[1])-int(cell2[1]))%2==0:
            return True
        else:
            return False
    #aynı sıralama
    elif abs(my_str.index(cell1[0])-my_str.index(cell2[0]))%2==0  :
        if abs(int(cell1[1])-int(cell2[1]))%2==0 or abs(int(cell1[1])-int(cell2[1]))==1:
            return True
        
        
        else:
            return False
    #farklı sıralama
    elif abs(my_str.index(cell1[0])-my_str.index(cell2[0]))%2!=0:
        if abs(int(cell1[1])-int(cell2[1]))%2==0:
            return False
        
        else:
            return True
    
        
