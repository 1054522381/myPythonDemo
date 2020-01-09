import sys


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except OSError as err:
        print("OS error: {0}".format(err))
    # except ValueError:
    #     print("您输入的不是数字，请再次尝试输入！")
    # except (RuntimeError, TypeError, NameError):
    #     print("其他错误")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise MyError('exception occured')
    else:
        print('else no error')
    finally:
        print('finally')



