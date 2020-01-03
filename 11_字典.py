"""
字典特点：根据关键字查找效率高，比较占空间。
字典的key不能重复，字典不支持索引和切片。
"""

my_dict = {'name': 'zhangsan', 'age': 31, 999: 'vvv'}
print(my_dict)

# 新增和修改元素值
my_dict['hello'] = 'world'
print(my_dict)

# 取值，如果key不存在会报错
print('取name的值：', my_dict['name'], '取999的值：', my_dict[999])

# 取值，如果key不存在，传默认值
print('取不存在的key的值：', my_dict.get('job', 'default value'))

# 删除元素
del my_dict[999]
print('999被删除：', my_dict)

# 遍历值列表，返回的类型为封装过的列表
print('值列表：', my_dict.values())

# list转列表类型
print('list类型的值列表：', list(my_dict.values()))

# 遍历键列表
print('键列表：', my_dict.keys())

# 遍历键值对列表，每一个键值对为一个元组
print('键值对：', my_dict.items())

# for循环遍历字典
print('====for====')
for key, value in my_dict.items():
    print(key, ':', value)

# 清空
my_dict.clear()
print('字典被清空：', my_dict)

# del删除变量
del my_dict
