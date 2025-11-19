def f(binary_number):
    
    x = 0
    length = len(binary_number)

    for i in range(length):
        if binary_number[i] == '0' or binary_number[i] == '1':
            x = x + 1
    if x == length:
        return True
    else: 
        return False