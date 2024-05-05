# range보다는 enumerate를 사용하라

def loop_list():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
    for flavor in flavor_list:
        print(f'{flavor} 맛있어요')


def index_loop_list():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
    for i in range(len(flavor_list)):
        print(f'{i+1}: {flavor_list[i]}')


def use_enumerate_loop_list():
    flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
    for i, flavor in enumerate(flavor_list, 1):
        print(f'{i}: {flavor}')


# loop_list()
# index_loop_list()
# use_enumerate_loop_list()