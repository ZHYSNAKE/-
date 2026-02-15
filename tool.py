import cv2
import numpy
import pyautogui
import time

def Click(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(1)

def Key(a,t1,t2):
    pyautogui.keyDown(a)
    time.sleep(t1)
    pyautogui.keyUp(a)
    time.sleep(t2)

def Find(picture_path):
    for i in range(10):
        #获取截屏
        screenshot_pil = pyautogui.screenshot()
        screenshot = cv2.cvtColor(numpy.array(screenshot_pil), cv2.COLOR_RGB2BGR)

        #获取模板
        img = cv2.imread(picture_path)
        if img is None:
            print(f"模板未找到")
            return
        height,width = img.shape[:2]

        #匹配
        result = cv2.matchTemplate(screenshot, img, cv2.TM_CCOEFF_NORMED)
        max_val = cv2.minMaxLoc(result)[1]
        find = False
        if max_val < 0.8:
            print(f"未匹配到")
        else:
            find = True
    
        #计算图片中心坐标
        up_left   = cv2.minMaxLoc(result)[3]
        low_right = (int(up_left[0] + width),int(up_left[1] + height) )
        location  = (int((up_left[0] + low_right[0])/2) , int((up_left[1] + low_right[1])/2))

        #移动并点击
        Click(location[0] , location[1])

        #检查找没找到
        if (find == True) :
            print(f"匹配成功"+picture_path)
            time.sleep(1)
            return   
        time.sleep(5)

# if __name__ == "__main__":
#     Click(-1000,521)
#     pass
    