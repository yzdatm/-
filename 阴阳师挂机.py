from PIL import ImageGrab
import pyautogui
import random
import time


def FoundImage(target_image):
    # 截取当前屏幕的截图
    screen = ImageGrab.grab()

    # 使用pyautogui库来查找图片在屏幕中的位置
    try:
        location = pyautogui.locate(target_image, screen, grayscale=False)
    except pyautogui.ImageNotFoundException:
        location=0

    # 如果找到了图片
    if location:
        # 输出图片在屏幕中的坐标范围
        left_top = (location.left, location.top)
        right_bottom = (location.left + location.width, location.top + location.height)
        # 生成随机坐标
        random_x = random.randint(left_top[0], right_bottom[0])
        random_y = random.randint(left_top[1], right_bottom[1])
        # 记录鼠标起始位置
        position1 = pyautogui.position()
        print(position1)
        # 鼠标移动
        pyautogui.doubleClick(random_x, random_y)
        print(random_x, random_y)
        #返回原来位置
        pyautogui.moveTo(position1.x , position1.y,0)
        time.sleep(2)
    else:
        time.sleep(2)


while True:
    target_image = 'zhunbei.png'
    FoundImage(target_image)
    time.sleep(3)
    target_image = 'jieshu.png'
    FoundImage(target_image)
    time.sleep(5)
