# in을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기보다는 get을 사용하라

counter_dict = {
    "품퍼니켈": 2,
    "사워도우": 1,
}

key = '밀'

def use_ifelse():
    if key in counter_dict:
        count = counter_dict[key]
    else:
        count = 0

    counter_dict[key] = count + 1


def use_try_except():
    try:
        count = counter_dict[key]
    except KeyError:
        count = 0

    counter_dict[key] = count + 1


def use_dict_get():
    count = counter_dict.get(key, 0)
    counter_dict[key] = count + 1


def differenc_get_vs_setdefault():
    votes = {
        '바게트': ['철수', '순이'],
        '치아바타': ['하니', '유리']
    }

    key = '브리오슈'
    who = '단이'

    names = votes.get(key, [])
    # names = votes.setdefault(key, [])
    names.append(who)

    print(votes)
    print(names)


# use_ifelse()
# use_try_except()
# use_dict_get()

# print(counter_dict)