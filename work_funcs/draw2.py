from work_funcs import c8, minifyImg
import cv2
import numpy as np
import os

CWD = os.path.dirname(os.path.abspath(__file__))

pixlels = [cv2.imread(os.path.realpath(os.path.join(CWD, f"../assets/pixels/{x}.jpg"))) for x in range(8)]


def make(imgPath, w=37, h=22, blur=3):
    """
    返回大致图像，和区块索引
    :param imgPath: 输入的图像
    :param w:指定宽度
    :param h:指定高度
    :param blur:加粗滤波内核
    :returns:
    """
    # 对图像进行初步处理（缩放，轮廓加粗）
    imgMini = minifyImg.make(imgPath, w, h, blur)
    img8c, img8cFollow = c8.make(imgMini)
    return img8c, img8cFollow


def draw(imgPath, w=37, h=22, blur=3):
    """

    :param imgPath:
    :param w:
    :param h:
    :param blur:
    :return:
    """
    blank = np.zeros((h * 20, w * 20, 3), dtype='uint8')
    blank.fill(255)

    img, imgFollow = make(imgPath, w, h, blur)
    # 绘制区块
    startY = round((h - img.shape[0]) / 2)
    startX = round((w - img.shape[1]) / 2)
    # 绘制边线
    for y in range(startY):
        for x in range(w):
            blank[y * 20:y * 20 + 20, x * 20:x * 20 + 20, :] = pixlels[0]
    for x in range(startX):
        for y in range(h):
            blank[y * 20:y * 20 + 20, x * 20:x * 20 + 20, :] = pixlels[0]
    # 绘制区块
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            X = x + startX
            Y = y + startY
            p = imgFollow[y, x]
            # print("p",p)
            # print(pixlels[p])
            # print(blank[y:y+20,x:x+20,:])
            blank[Y * 20:Y * 20 + 20, X * 20:X * 20 + 20, :] = pixlels[p]
    for y in range(startY + img.shape[0], h):
        for x in range(w):
            blank[y * 20:y * 20 + 20, x * 20:x * 20 + 20, :] = pixlels[0]
    for x in range(startX + img.shape[1], w):
        for y in range(h):
            blank[y * 20:y * 20 + 20, x * 20:x * 20 + 20, :] = pixlels[0]
    return blank


if __name__ == '__main__':
    # img,imgF = make("test4.png")
    # cv2.imshow("img",img)
    # print(imgF)
    img = draw("testimg/54_raw.jpg", 37 * 4, 22 * 4, blur=0)
    cv2.imshow("img", img)
    cv2.imwrite("ooo.png", img)
    cv2.waitKey(0)
