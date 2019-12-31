# 定义函数
def print_stars():
    i = 1
    while i <= 5:
        print('*' * i)
        i += 1


# 函数调用
print_stars()


def add(a, b=10):
    print('a + b = %d' % (a + b))
    return a + b


# 位置参数，根据位置传参
add(1, 2)
print('add(1) result=%d' % add(1))
# 关键字参数，根据参数名传参
add(b=1, a=4)
