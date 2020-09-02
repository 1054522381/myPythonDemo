# 字符串定义
my_str = 'hello@itcast.com'
my_str = "world@itcast.com"
# my_str = """
#     保留制表符和
#     换行
# """
print(my_str)

# 用正负下标值访问字符
print(my_str[0])
print(my_str[-1])

# 访问子字符串 [start, end)
print(my_str[1:5])
# 步长
print('根据步长取子串：', my_str[1:5:2])
# 字符串逆序
print('逆序：', my_str[::-1])

print('@字符下标是：', my_str.find('@'))

print('字符串长度:', len(my_str))

print('重复字符串:', my_str * 2)

# 遍历
for char in my_str:
    print(char, end=' ')
print()

# 字符串替换
print((my_str * 2).replace('@', '#', 1))

# 拆分
print(my_str.split('@'))

# 计算子串出现的次数
print('@出现的次数：', my_str.count('@'))

# 去除两端空格
print(' hello world   '.strip())

# 判断是否全字母
print(my_str.isalpha())
print('是否全字母：', 'hello'.isalpha())

# 判断全数字
print('是否全数字', '3534587'.isdigit())

# 格式化
print('Hello, {}'.format('world'))
print('Hello, {0} {1}'.format('aaa', 'bbb'))
print('Hello, {x} {y}'.format(x=123, y='bbb'))

# 0.21%
print('%.2f%%' % (float(10575 / 5074480) * 100))
# round(x [,n])，浮点数x四舍五入，舍入到小数点后的n位数。
print(f'{round(float(10575 / 5074480) * 100, 2)}%')

# %s 字符串格式化
t = '%s, %s' % ('hello', 'world')
print(t)

# 整数格式化，如果变量长度不到6位则左边补0，长度大于等于6位则返回变量本身
t = '我的学号是：%06d' % 103
print(t)

# True=1 False=0 可以和数字运算
print('True + 12 =', True + 12)
print('False + 21 =', False + 21)
