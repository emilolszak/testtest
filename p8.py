def f(palindrome):
    x = len(palindrome)
    b = len(palindrome)
    for i in range(x):
        y = x - i - 1
        if (palindrome[i] == palindrome[y]): 
            b = b - 1    
    if b == 0:
        return True
    else:
        return False
    