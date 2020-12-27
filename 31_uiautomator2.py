# -*- coding: utf-8 -*-
import uiautomator2 as u2

# 连接手机
device = u2.connect()

# 安装app
# url = "http://xx/xxxx.apk"
# device.app_install(url)

# 定位app图标，打开app
device(text='京东').click()
# device(resourceId='com.lemon.lemonban:id/navigation_my').click()
# my_icon = device(resourceId='com.lemon.lemonban:id/navigation_my').child(resourceId='com.lemon.lemonban:id/icon')
# my_icon.sibling(className='android.view.View')
# 点击绝对坐标位置
# device.click(688, 1553)
# 点击位置百分比
# device.click(0.765, 0.971)
# 滑动 4个参数：startx,starty,endx,endy，通常用来滑动到指定的位置
# device.swipe(800, 500, 100, 500)
# 扩展版的滑动
device.swipe_ext('left', scale=0.9)

# 输入内容
device(resourceId='xx').send_keys('17850505000')
# 清除输入
device(resourceId='xx').clear_text()

# 启动app
# device.app_start('com.p1.mobile.putong')

# 获取正在运行的app的包名
# print(f'当前app的包名=>{device.app_current()}')

# 获取设备信息
print(f'设备信息=>{device.info}')
print(f'设备详细信息=>{device.device_info}')

# 获取屏幕大小，返回一个元组如：(1080, 1920)
print(f'屏幕大小=>{device.window_size()}')

# 获取所有正在运行的app的包名
# print(f'所有正在运行的app的包名=>{device.app_list_running()}')

# 获取toast
# print(device.toast.get_message())

# 截屏
# device.screenshot(r'd:/t.png')
# from PIL import ImageFilter
#
# # 截屏操作进阶 pillow、cv2
# im = device.screenshot()
# im.save('hello.png')
# # 模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('helloblur.png')
# # 指定截图大小
# im3 = im.resize(200, 400)
# im3.save('helloresize.png')

# # 智能等待，默认超时时间为20s
# device.wait_timeout = 30
# device.implicitly_wait(30)
# device.app_start('com.xxzb.fenwoo', wait=True)
# # 等待页面加载完成
# device.wait_activity()
# # 等待元素出现
# device(...).wait()
# # 等待元素消失
# device(...).wait_gone()
# # 等待元素是否存在
# device(...).exists()
# # click等待
# device(...).click(timeout=50)
# # 输入等待
# device(...).set_text(timeout=50)  # 同send_keys方法
# device(...).clear_text(timeout=50)

# 推送文件
# device.push(f'd:/demo.txt', f'/data/local/tmp/demo.txt')

# 拉取文件
# device.pull(r'/data/local/tmp/demo.txt', 'demo.txt')

# 按键操作
# device.screen_off()
# device.screen_on()
# device.press('power')
# device.press('volume_mute')
# device.press('recent')

# 停止app
# device.app_stop('com.p1.mobile.putong')

# 卸载app
# device.app_uninstall('com.p1.mobile.putong')

# 清除app数据
# device.app_clear('com.p1.mobile.putong')

if __name__ == '__main__':
    pass
