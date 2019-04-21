import cv2
import numpy as np
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from functools import lru_cache

import time

from work_funcs import c16

cs_rgb = [
    [49, 40, 41],
    [255, 255, 255],
    [255, 211, 115],
    [115, 255, 173],
    [115, 130, 255],
    [247, 105, 90],
    [255, 215, 198],
    [181, 174, 165]
]


def color_diff(x, y):
    """
    转换为sRGB 返回差值
    :param x:
    :param y:
    :return:
    """
    color1_rgb = sRGBColor(x[2], x[1], x[0], is_upscaled=True)
    color2_rgb = sRGBColor(y[0], y[1], y[2], is_upscaled=True)

    color1_lab = convert_color(color1_rgb, LabColor)
    color2_lab = convert_color(color2_rgb, LabColor)
    return delta_e_cie2000(color1_lab, color2_lab)


@lru_cache(65535)
def to8color(r, g, b):
    """
    查找颜色最近的，返回BGR和索引
    :param b: blue
    :param g: green
    :param r: red
    :return:
    """
    ret = [0, 0, 0]
    min_d = 1145141919810
    mini_index = 0
    for index, color in enumerate(cs_rgb):
        t = color_diff([r, g, b], color)
        if t < min_d:
            min_d = t
            ret = color
            mini_index = index
    return np.array(ret[::-1], dtype='uint8'), mini_index


def make(img):
    """
    返回大致颜色和对应颜色区块索引
    :param img: 输入图像 如果为路径就加载
    :returns:大致颜色图像，颜色区块索引
    """
    if isinstance(img, str):
        img = cv2.imread(img, -1)
    # 转换为RGB
    if (img.shape[2]) == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    img = c16.make(img, 16)
    # 由浮点数映射为255
    img *= 255
    # 图像面积
    imgLen = img.shape[0] * img.shape[1]

    img2Arr = []
    img2ArrFollow = []

    for x in img.reshape(imgLen, 3):
        # 转换为8色
        color, index = to8color(*x)
        img2Arr.append(color)
        img2ArrFollow.append(index)

    img2ArrFollow = np.array(img2ArrFollow).reshape(img.shape[:2])
    img2 = np.array(img2Arr, dtype='uint8').reshape(img.shape)
    return img2, img2ArrFollow


if __name__ == '__main__':
    t0 = time.perf_counter()
    # img = cv2.imread("output12.bmp", -1)
    # if (img.shape[2]) == 4:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    # print(img.shape)
    # print(img.shape[0] * img.shape[1])
    # img2 = np.array([to8color(x[0], x[1], x[2]) for x in img.reshape(-1, 3)]).reshape(img.shape)
    # cv2.imwrite('sysfout12.png', img2)
    img8 = make("test.png")
    cv2.imshow("img8", img8)
    print(time.perf_counter() - t0)
    cv2.waitKey(0)
