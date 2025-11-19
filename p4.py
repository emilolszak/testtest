def f(card_number):
    card = ''
    for i in range(len(card_number)):
        if i < 2 or i > 11:
            card = card + card_number[i]
        elif 2 < i < 12:
            card = card + '*'
    return card       
