# 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들어라

# 파라메터가 모두 위치 인자인 경우
def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number/divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# 파라메터가 모두 위치인자, 마지막 2 인자는 디폴트값으로 셋팅되지만 위치가 다를 경우 에러의 소지가 있음
def safe_division_b(number, divisor, ignore_overflow=False, ignore_zero_division=False):
    pass


# *기호를 기준으로 이전은 위치 인자 이후는 키워드 인자로 구분됨
# (위치 인자 2 파라메터의 경우 키워드 인자로 혼용도 가능하여 역시 에러의 소지가 있음)
def safe_division_c(number, divisor, *, ignore_overflow=False, ignore_zero_division=False):
    pass


# /기호 인전의 파라메터는 위치로만 지정하는 파라메터 강제가 됨
def safe_division_d(number, divisor, /, *, ignore_overflow=False, ignore_zero_division=False):
    pass


# /, *기호 사이에 있는 파라메터는 위치, 키워드 방식 모두 허용하여 필요에 따라 설정하여 사용하면 됨
def safe_division_e(number, divisor, /, ndigits=10, *, ignore_overflow=False, ignore_zero_division=False):
    pass


# result = safe_division(1.0, 10**500, True, False)
result = safe_division(1.0, 0, False, True)
print(result)
