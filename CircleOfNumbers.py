def circleOfNumbers(n, firstNumber):
    midpoint=int(n/2)
    
    if firstNumber<midpoint:
        return midpoint+firstNumber
    elif firstNumber==midpoint:
        return 0
    else:
        return (firstNumber-midpoint)
    
    print(firstNumber+int(n/firstNumber))