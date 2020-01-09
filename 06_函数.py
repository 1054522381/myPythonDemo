# 定义函数
def print_stars():
    """鼠标放在函数调用的位置，按ctrl+Q，函数文档在这里写"""
    i = 1
    while i <= 5:
        print('*' * i)
        i += 1


# 函数调用
print_stars()

# help查看函数文档
print(help(print_stars))


# 定义带缺省参数的函数，缺省参数位置之后定义的形式参数都必须带缺省值
def add(a, b=10):
    """在这里简单描述函数功能

    :param int a: 加法操作数
    :param int b: 加法操作数
    :return: 返回值
    """
    if not isinstance(a, int) or not isinstance(b, int):
        print('参数类型应该为数字！')
        return None
    print('a + b = %d' % (a + b))
    return a + b


# 位置参数，根据位置传参
add(1, 2)
print('add(1) result=%d' % add(1))
# 关键字参数，根据参数名传参
add(b=1, a=4)
# 既有位置参数又有关键字参数，位置参数需要放在关键字参数前面
add(5, b=5)

add(None)


# 不定长参数
def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print("printinfo输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


