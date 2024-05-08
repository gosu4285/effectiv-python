# 대입식을 사용해 반복을 피하라


fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

def assignment_statement():
    count = fresh_fruit.get('레몬', 0)
    if count:
        print('make lemonade')
    else:
        print('out of stock')


def walrus_operation():
    if count := fresh_fruit.get('레몬', 0):
        print('make lemonade')
    else:
        print('out of stock')


# assignment_statement()
# walrus_operation()
