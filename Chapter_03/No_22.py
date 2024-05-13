# 변수 위치 인자를 사용해 시각적인 잡음을 줄여라


def use_postional_argument(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


def use_star_args(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


# use_postional_argument('내 숫자는', [1, 2])
# use_postional_argument('안녕', [])
# use_star_args('내 숫자는', [1, 2])
use_star_args('안녕')