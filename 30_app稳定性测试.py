# -*- coding: utf-8 -*-
import os
import re


class MonkeyTop100:
    """
    monkey跑top100的app稳定性思路：
    1.获取apk包的路径
    2.根据路径安装apk
    3.获取每个apk的包名
    4.调用monkey进行操作
    5.获取并分析日志
    6.检查日志并判断是否存在ANR或Crash等关键字，并标识结果
    7.卸载apk
    """

    def get_apk_path(self):
        path = []
        for filename in os.listdir(r'D:\apks'):
            path.append('D:\\apks\\' + filename)
        return path

    def install_apk(self, apk_path):
        print("正在安装...")
        cmd = "adb install " + apk_path
        resp = os.popen(cmd)
        return 'Success' in resp.read()

    def get_pkg_name(self, apk_path):
        cmd = "aapt dump badging " + apk_path
        resp = os.popen(cmd)
        # 解决乱码问题：先读二进制，再用指定的字符集解码
        content = resp.buffer.read().decode(encoding='utf8')
        result = re.findall("name='(.*?)'", content)
        return result[0]

    def monkey_op(self, pkg_name):
        print("正在测试...")
        cmd = f"adb shell monkey -p {pkg_name} --monitor-native-crashes --pct-touch 50 --pct-motion 50 --pct-syskeys 0 --throttle 300 -v -v -v 1000"
        resp = os.popen(cmd)
        if 'exception' in resp.read().lower():
            return 'fail'
        return 'pass'

    def uninstall_apk(self, pkg_name):
        print("正在卸载...")
        cmd = f"adb uninstall {pkg_name}"
        resp = os.popen(cmd)
        print('卸载结果：' + resp.read())


if __name__ == '__main__':
    m = MonkeyTop100()
    result_dic = {}
    for apk_path in m.get_apk_path():
        if m.install_apk(apk_path):
            pkg_name = m.get_pkg_name(apk_path)
            result = m.monkey_op(pkg_name)
            result_dic[pkg_name] = result
            m.uninstall_apk(pkg_name)
        else:
            print('安装失败')

    print(result_dic)

