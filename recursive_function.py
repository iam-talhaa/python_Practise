

def pattern(num):
    if(num==0):
        return print("")
    print("*" *num)
    pattern(num-1)

pattern(4)    
