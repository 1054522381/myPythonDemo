# 创建一个包含了10个随机数的列表
import random
my_list = []
i = 0
while i < 10:
    random_number = random.randint(1, 100)
    my_list.append(random_number)
    i += 1
print('随机数列表：', my_list)

# 排序
my_list.reverse()
print('倒序后列表：', my_list)
my_list.sort()
print('默认升序后列表：', my_list)
my_list.sort(reverse=True)
print('降序后列表：', my_list)

# 查找值，找不到会报错
if 100 in my_list:
    print('100的下标是：', my_list.index(100))

# 将一个列表的所有元素追加到当前列表中
other_list = ['a', 'b']
my_list.extend(other_list)
print('合并后列表：', my_list)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
# 内存地址
print(id(list_a) == id(list_b))
