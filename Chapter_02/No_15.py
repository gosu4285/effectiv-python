# 딕셔너리 삽입 순서에 의존할 때는 조심하라


def dict_order_print():
    # 파이썬 3.6 이후부터는 딕트에 입력한 순서대로 출력이 보장됨
    baby_names = {
        'cat': 'kitten',
        'dog': 'puppy',
    }
    print(baby_names)


class MyClass:
    def __init__(self):
        self.aligator = 'hatchling'
        self.elephant = 'calf'


def class_dict_example():
    a = MyClass()
    for k, v in a.__dict__.items():
        print(f'{k} = {v}')


# dict_order_print()
class_dict_example()