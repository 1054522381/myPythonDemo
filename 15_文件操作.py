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
# print('当前工作目录：', os.getcwd())

# 改变当前工作目录
# os.chdir('/abc/cde')

# 获取指定目录下的文件列表
# print('当前目录下的文件列表：', os.listdir())
#print('指定目录下的文件列表：', os.listdir('D:\\apks\\jingqi-7.8.8.0.28-zroTest-debug\\'))


def list_file_names(file_path):
    """ 取当前目录下所有 smali 打头的文件夹的所有子目录 """
    result = set()
    dirs = os.listdir(file_path)
    for temp_dir in dirs:
        if not temp_dir.startswith('smali'):
            continue
        # root：就是获取当前目录路径
        # dirs：就是获取当前路径下所有子目录
        # files： 就是获取当前路径下所有非目录子文件
        for root, dirs, files in os.walk(file_path + temp_dir):
            pkg = root.replace(file_path + temp_dir + '\\', '').replace(file_path + temp_dir, '').replace('\\', '.')
            result.add(pkg)
            # print("root=>" + root.replace(file_path + temp_dir + '\\', '').replace(file_path + temp_dir, '').replace('\\', '.'))
            # print(dirs)
            # print(files)
    result = list(result)
    result.sort()
    for t in result:
        if t:
            print(t)


def get_file_short_name(filename):
    """ 获取apk反编译后的文件夹path 比如：D:\\apks\\jingqi-7.8.8.0.28-zroTest-debug\\ """
    (directory, temp_file_name) = os.path.split(filename)
    (short_name, extension) = os.path.splitext(temp_file_name)
    # print(directory, short_name, extension)
    return directory + os.sep + short_name + os.sep


# 执行shell命令
os.system('java -version')
target_path = get_file_short_name("D:\\apks\\jingqi-7.8.8.0.28-zroTest-debug.apk")
list_file_names(target_path)
