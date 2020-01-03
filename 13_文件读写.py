"""
文件打开分为读（w）、写（r）、追加（a）模式，这三种模式分别再分为文本模式和二进制模式（wb/rb/ab）。
w 模式：会覆盖文件原有的数据，如果文件不存在，会创建新文件。

mac系统：\r
windows：\r\n
linux：\n
如果用文本模式打开文件，会进行换行符的转换。
如果用二进制模式的话，不会进行换行符转换。
文件本质上都是以二进制的方式存储在磁盘上的。
"""

# write写文件
f = open('a.txt', 'w')
my_content = "hello world\n"
f.write(my_content)
f.close()

# writelines写文件
f = open('a.txt', 'w')
lines = ['aaa\n', 'bbb', 'ccc']
f.writelines(lines)
f.close()

# 读取文件所有数据
f = open('a.txt', 'r')
# read默认读取文件中的所有数据
my_content = f.read()
f.close()
print('读取文件所有数据---' + my_content + '---')

# 读一行数据
f = open('a.txt', 'r')
my_content1 = f.readline()
my_content2 = f.readline()
f.close()
print('读一行数据---' + my_content1 + '---')
print('读一行数据---' + my_content2 + '---')

# 读多行
f = open('a.txt', 'r')
lines = f.readlines()
f.close()
for line in lines:
    # 替换文件中的换行符，用print自带的换行
    if line[-1] == '\n':
        print(line[:-1])
    else:
        print(line)

# print('读多行数据---', end='')
# print(my_content, end='')
# print('---')
