def myFunc(var):
    if type(var) is not str:
        raise Exception("please provide only a string")
    return print("Hello from myFunc!" + var)
