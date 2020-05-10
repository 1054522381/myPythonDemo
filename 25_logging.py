# !/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os.path
import time
from logging.handlers import TimedRotatingFileHandler
# import re
# from logging.handlers import RotatingFileHandler
"""
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
"""


def hello():
    """在控制台打印"""
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('----logging-----')
    logging.debug('---logging debug---')


def logfile():
    """在控制台和文件中打印"""
    # 第一步，创建一个logger
    logger = logging.getLogger()
    # Log等级总开关
    logger.setLevel(logging.INFO)

    # 第二步，创建一个handler，用于写入日志文件
    log_file_name = time.strftime('%Y%m%d', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/logs/'
    log_file_full_name = log_path + log_file_name + '.log'
    fh = logging.FileHandler(log_file_full_name, mode='w')
    # fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    # ch.setLevel(logging.INFO)

    # 第三步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第四步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.debug('---logger debug---')
    logger.info('---logger info---')
    logger.warning('---logger warning---')
    logger.error('---logger error---')

    try:
        a = 2/0
    except Exception as e:
        logger.info('---logger info---', exc_info=True)
        logger.error('---logger error---', exc_info=True)


def rotating():
    """根据时间产生独立的log文件"""
    # 创建TimedRotatingFileHandler对象
    log_file_handler = TimedRotatingFileHandler(filename="./output", when="M", interval=1, backupCount=30)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    # log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")

    # 日志打印格式
    log_fmt = '%(asctime)s File \"%(filename)s\" [line:%(lineno)d] %(levelname)s %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler.setFormatter(formatter)
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    log.addHandler(log_file_handler)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    log.addHandler(ch)

    # 循环打印日志
    log_content = "test log"
    count = 0
    while count < 30:
        log.error(log_content)
        time.sleep(20)
        count = count + 1
    # log.removeHandler(log_file_handler)


if __name__ == '__main__':
    # hello()
    # logfile()
    rotating()
