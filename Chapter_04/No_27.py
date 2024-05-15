# map과 filter 대신 컴프리헨션을 사용하라

def use_loop():
    a = [1, 2, 3, 4, 5]
    squares = []
    for num in a:
        squares.append(num**2)
    print(squares)


def use_list_comprehension():
    a = [1, 2, 3, 4, 5]
    squares = [num**2 for num in a]
    print(squares)


# use_loop()
# use_list_comprehension()
