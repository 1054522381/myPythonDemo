"""
元组不支持修改，只支持查询和遍历，元组就相当于是不能修改的列表。
元组比列表更节省空间
"""

# 元组定义
first_tuple = (100, 234, 354)

# 如果元组只有一个元素，定义的时候需要在元素后面加逗号
one_tuple = (35, )
one_tuple = ((35,), )

# 元组支持嵌套
my_tuple = ((43, 45), ('aa', 'bb'))
print(my_tuple)

# 计算元素出现的次数
print('值234出现的次数：', first_tuple.count(234))

# 元素的位置
print('元素234的位置：', first_tuple.index(234))

# 判断元素是否存在
print('234是否是元组中的元素：', 234 in first_tuple)

print('切片：', first_tuple[:2])
