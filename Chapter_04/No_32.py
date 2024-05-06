# 긴 리스트 컴프리헨션보다는 제너레이터 식을 사용하라

def use_list_comprehension():
    value = [len(x) for x in open('my_file.txt', encoding='utf-8')]
    print(value)


def use_generator():
    it = (len(x) for x in open('my_file.txt', encoding='utf-8'))
    for length in it:
        print(length)


# use_list_comprehension()
use_generator()