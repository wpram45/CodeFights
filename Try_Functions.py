import math
def tryFunctions(x, functions):
    return [eval(i+"("+str(x)+")") if  not i.startswith("lambda") else  eval(str(i))(x)  for i in functions]



print(tryFunctions(1,["math.sin", "math.cos", "lambda x: x * 2", "lambda x: x ** 2"]))
