# -*- coding: utf-8 -*-
import os
import time
import csv


class MemMonitor:
    def __init__(self):
        self.data = []
        self.counter = 3

    def get_meminfo(self):
        cmd = "adb shell dumpsys meminfo | findstr com.lingan.seeyou"
        resp = os.popen(cmd)
        for index, line in enumerate(resp):
            if index == 0:
                data = line.split()[0][:-1]
                # print(data)
                self.data.append(data)

    def run(self):
        i = 0
        while i <= self.counter:
            time.sleep(1)
            self.get_meminfo()
            i += 1

    def save_data(self):
        """ 把数据存成csv，可以在excel中用数据插入图表 """
        with open('mem.csv', 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.data)


if __name__ == '__main__':
    print('=== 开始采集内存信息 ===')
    m = MemMonitor()
    m.run()
    m.save_data()
    print(m.data)
