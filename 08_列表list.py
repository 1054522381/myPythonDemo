"""
列表的特点：
根据索引查找的效率很高，根据关键字查找的效率很低。
在指定位置插入和删除元素，会造成数据元素的移动，效率低。尾部插入和删除元素，效率较高。

"""

# 列表可以存放不同类型的元素，建议存相同类型的数据
my_list = ['aaa', 123, True, None, [1, 2, 3]]
print(my_list)
print('根据下标取元素：', my_list[1])
print('切片：', my_list[:3])
print('列表长度：', len(my_list))

# 遍历列表里的列表
for o in my_list:
    if isinstance(o, list) and len(o) > 0:
        for num in o:
            print(num, end=' ')
print()

# 指定位置插入元素
my_list.insert(0, 'first')
print('指定位置添加元素：', my_list)

# 尾部插入元素，比指定位置插入元素的效率高
my_list.append('last')
print('尾部添加元素：', my_list)

# 删除元素：位置删除和值删除
del my_list[3]
print('del删除指定位置元素：', my_list)
my_list.pop(0)
print('pop删除指定位置元素：', my_list)

my_list.pop()
print('pop默认删除末尾元素：', my_list)
my_list.remove('aaa')
print('删除第一个出现的aaa值：', my_list)

# 清空列表
my_list.clear()
print('清空后的列表：', my_list)
