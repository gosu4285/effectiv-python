# 시퀀스를 슬라이싱하는 방법으르 익혀라

# 리스트[시작:끝]

a = ['a', 'b', 'c', 'd', 'e', 'g']

print(a[:])      # ['a', 'b', 'c', 'd', 'e', 'g']
print(a[:3])     # ['a', 'b', 'c']
print(a[:-1])    # ['a', 'b', 'c', 'd', 'e']
print(a[4:])     # ['e', 'g']
print(a[-3:])    # ['d', 'e', 'g']
print(a[1:3])    # ['b', 'c']
print(a[2:-1])   # ['c', 'd', 'e']
print(a[-3:-1])  # ['d', 'e']

