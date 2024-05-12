# 키워드 인자로 선택적인 기능을 제공하라


def remainder(number, divisor):
    print(number % divisor)


def print_parameters(**kwargs):
    for k, v in kwargs.items():
        print(f'key:{k}, value:{v}')


def default_parameter(period: int = 1, **kwargs):
    print(f'period:{period}')
    for k, v in kwargs.items():
        print(f'key:{k}, value:{v}')


# remainder(20, 7)
# remainder(divisor=7, number=20)
# remainder(20, divisor=7)

my_kwargs = {
    'divisor': 7,
    'number': 20,
    'alpha': 1.5,
    'beta': 9,
    'gamma': 4
}
# remainder(**my_kwargs)
# print_parameters(**my_kwargs)

default_parameter(**my_kwargs, period=11)