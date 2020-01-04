import os

# 文件重命名
# os.rename('a_copy.txt', 'a_backup.txt')

# 文件删除
# os.remove('a_backup.txt')

# 创建目录
# os.mkdir('abc')

# 删除目录
# os.rmdir('abc')

# 获得当前工作目录 current working directory
print('当前工作目录：', os.getcwd())

# 改变当前工作目录
# os.chdir('/abc/cde')

# 获取指定目录下的文件列表
print('当前目录下的文件列表：', os.listdir())
print('指定目录下的文件列表：', os.listdir('C:/'))


