def f(name):
    i = 0
    x = ''
    for i in range(len(name) - 1): 
        if name[i] == ' ':
            x = x + name[i+1]
    return(name[0] + x) 
