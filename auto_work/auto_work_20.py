import pyautogui,time
#获取全窗口的大小
'''wh = pyautogui.size()'''
#鼠标的运动，以画一个正方形为例子
'''for i in range(10):
    pyautogui.moveTo(1000,100,duration=0.25)
    pyautogui.moveTo(1100,100,duration=0.25)
    pyautogui.moveTo(1000,200,duration=0.25)
    pyautogui.moveTo(1100,200,duration=0.25)'''
# 程序的睡眠时间，以秒为单位
'''time.sleep(2)'''
#鼠标的左键点击
# pyautogui.click(898,1059)
#鼠标的拖拽，以向右，左，上，下为例子
'''pyautogui.drag(100,0,duration=0.2)  #向右
pyautogui.drag(-100,0,duration=0.2)    #向左
pyautogui.drag(0,100,duration=0.2)     #向下
pyautogui.drag(0,-100,duration=0.2)    #向上
'''
#规划鼠标运动的记录工具
# pyautogui.mouseInfo()