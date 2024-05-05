# 리스트를 반환하기보다는 제너레이터를 사용하라

from typing import List


def index_words_return_list(text) -> List[int]:
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_words_use_yield(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


# input_text = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관'
# res = index_words_return_list(input_text)
# print(res)
# for index in index_words_use_yield(input_text):
#     print(f'index:{index}')
