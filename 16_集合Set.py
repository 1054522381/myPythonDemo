"""
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""

# set的两种定义方式
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
basket = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
print(basket)

# 空set
dic = {}
print('dic的类型：', type(dic))
empty_set = set()
print('empty_set的类型：', type(empty_set), '值：', empty_set)

# 添加元素
empty_set.add('hello')
empty_set.add(123)
print(empty_set)

# 一次添加多个元素
empty_set.update('world', [456, 890])
print(empty_set)

# 移除指定元素，如果元素不存在，会报错
empty_set.remove('hello')
print('hello被移除：', empty_set)

# 移除指定元素，如果元素不存在，不报错
empty_set.discard('xxxx')
print('被移除的元素不存在：', empty_set)

# 元素个数
print('元素个数：', len(empty_set))

# 随机获取其中一个元素，并将元素从集合剔除，如果集合为空会报错。
element = empty_set.pop();
print('随机剔除一个元素：', element, '\n集合：', empty_set)

# 判断元素是否在集合中存在
print('ttt是否为集合元素：', 'ttt' in empty_set)

a = {1, 3, 5, 7}
b = {1, 2, 3, 4, 5}

# a 和 b 的差集
print(f'差集：{b - a}')
print(f'并集：{a | b}')
print(f'交集：{a & b}')
print(f'a 和 b 中不同时存在的元素：{a ^ b}')

# 清空集合
empty_set.clear()
print('集合已清空：', empty_set)

