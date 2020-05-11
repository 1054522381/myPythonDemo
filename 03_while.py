# 计算0到100累加的和
i = 0
sum = 0
while i < 100:
    print('i=%s' % i)
    sum += i
    i += 1
print('sum=%s' % sum)

# 计算0到100的奇数累加和
j = 0
sum = 0
while j < 100:
    if j % 2 != 0:
        sum += j
        print(j)
    j += 1
print('奇数和为：%s' % sum)

# 打印星星
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('=============================')

# 打印星星
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    i += 1
    print()

# range()函数生成数列
print(f'type rang(5) => {type(range(5))}')
print(f'rang(5) => {list(range(5))}')
print(f'rang(5, 9) => {list(range(5, 9))}')
print(f'range(0, 10, 3) => {list(range(0, 10, 3))}')

