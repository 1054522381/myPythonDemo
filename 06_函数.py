# 定义函数
def print_stars():
    """鼠标放在函数调用的位置，按ctrl+Q，函数文档在这里写"""
    i = 1
    while i <= 5:
        print('*' * i)
        i += 1


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


# 不定长参数，参数加了星号 * ，会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    """打印任何传入的参数"""
    print("printinfo输出: ")
    print(arg1)
    print(f"带一个*的不定长参数vartuple=>{vartuple}")


# 不定长参数，加了两个星号 ** 的参数会以字典的形式导入。
def printinfo2(arg1, **vardict):
    """打印任何传入的参数"""
    print("printinfo2输出: ")
    print(arg1)
    print(f"带两个*的不定长参数vardict=>{vardict}")
    return arg1, vardict


# 用lambda创建匿名函数，语法： lambda [arg1 [,arg2,.....argn]]:expression
fun = lambda arg1, arg2: arg1 + arg2

# 全局变量
scope = 'outter'


def test_scope():
    # 如果访问全局变量，要用global
    # global scope
    # print(f'scope=>{scope}')
    scope = 'inner'
    print(f'scope=>{scope}')  # inner


# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
if __name__ == '__main__':
    # 函数调用
    print_stars()

    # help查看函数文档
    print(help(print_stars))

    # 位置参数，根据位置传参
    add(1, 2)
    print('add(1) result=%d' % add(1))
    # 关键字参数，根据参数名传参
    add(b=1, a=4)
    # 既有位置参数又有关键字参数，位置参数需要放在关键字参数前面
    add(5, b=5)

    add(None)

    # 调用printinfo函数，参数被作为元组处理，函数不return会默认返回None
    t = printinfo(70, 60, 50)
    print(f'printinfo返回=>{t}')

    # 调用printinfo2函数，参数被作为字典处理，函数返回多个值，默认为元组类型
    t = printinfo2(1, a=2, b=3)
    print(f'printinfo2返回=>{t}')

    # 调用lambda匿名函数fun
    print("fun调用后的值为 : ", fun(10, 20))

    test_scope()
    print(f'scope=>{scope}')  # outter
