# 인덱스를 사용하는 대신 대입을 사용해 데이터를 언패킹하라

def tuple_unpacking():
    item = ('호박엿', '식혜', '약과')
    first, second, third = item
    print(first, second, third)


def list_iteration():
    snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
    for i in range(len(snacks)):
        item = snacks[i]
        name = item[0]
        calories = item[1]
        print(f'#{i+1}: {name} 은 {calories} 칼로리입니다')


def list_unpacking():
    snacks = [('베이컨', 350), ('도넛', 240), ('머핀', 190)]
    for i, (name, calories) in enumerate(snacks, 0):
        print(f'#{i + 1}: {name} 은 {calories} 칼로리입니다')


# tuple_unpacking()
# list_iteration()
# list_unpacking()
