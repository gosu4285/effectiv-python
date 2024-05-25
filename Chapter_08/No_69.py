# 정확도가 매우 중요한 경우에는 Decimal을 사용하라

from decimal import Decimal


def normal_usecase():
    rate = 1.45
    seconds = 3*60 + 42
    cost = rate * seconds / 60
    print(cost)  # 5.364999999999999
    print(round(cost, 2))  # 5.36


def decimal_usecase():
    rate = Decimal('1.45')
    seconds = Decimal(3*60 + 42)
    cost = rate * seconds / Decimal(60)
    print(cost)  # 5.365


# normal_usecase()
# decimal_usecase()
