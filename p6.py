def f(number, even):
    x = 0
    for i in range(len(number)):
        n = int(number[i])
        if even == '1':
            if n % 2 == 1:
                x = x + n
        elif even == '2':
            if n % 2 == 0:
                x = x + n
    return x
