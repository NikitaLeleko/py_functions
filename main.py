def xo(string: str):
    counter_x = 0
    counter_o = 0
    for i in range(len(string)):
        if string[i]=="x" or string[i]=="X":
            counter_x+=1
        elif string[i]=="o" or string[i]=="O":
            counter_o+=1
    return counter_x == counter_o
