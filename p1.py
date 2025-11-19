def f(amount_to_pay):
    y = amount_to_pay // 5 
    z = amount_to_pay % 5 
    p = z // 2 
    x = z % 2 
    return y + p + x

print(f(8))