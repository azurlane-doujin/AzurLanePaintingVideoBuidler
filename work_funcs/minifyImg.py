import cv2
import numpy as np

cv = cv2


def edgeBlack(image_array, blur=3):
    """
    进行轮廓加粗的方法
    :param image_array: 输入的图像 np.array
    :param blur: 加粗参数
    :return: 处理后图像
    ：:return np.array
    """
    # 使用3X3内核进行高斯滤波
    blurred = cv.GaussianBlur(image_array, (3, 3), 0)
    # 转换为灰度图像
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)

    # 使用 sobel算子计算，x方向,y方向
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # 使用canny算子查找边缘
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    if blur:
        # 使用指定内核进行高斯滤波
        blurred = cv.GaussianBlur(edge_output, (blur, blur), 0)
    else:
        blurred = edge_output
    # 进行阈值处理，使用二值化
    ret, mask = cv2.threshold(blurred, 5, 255, cv2.THRESH_BINARY)
    # 生成空白矩阵
    black = np.zeros((image_array.shape[0], image_array.shape[1], 3), dtype=np.uint8)

    # 进行反选
    blackCanny = cv2.bitwise_not(mask)
    # blackCannyRGB = cv2.cvtColor(blackCanny, cv2.COLOR_GRAY2BGR)
    # 进行图像混合
    o = cv.add(image_array, black, mask=blackCanny)

    return o


def minify(image_array, W=37, H=22):
    """
    将输入图像重映射到画板大小
    :param image_array: 输入图片 np.array
    :param W: 绘制区域宽度
    :param H: 绘制区域高度
    :return: np.array 进行缩放后的图像
    """
    h, w, _ = image_array.shape
    # 缩放比例
    wr = w / W
    hr = h / H
    if hr > wr:
        r = hr

        h = H
        w = round(w / r)
    else:
        r = wr
        h = round(h / r)
        w = W
    # 进行缩放
    img2 = cv2.resize(image_array, (w, h), cv2.INTER_AREA)

    return img2


def make(img_path, w=37, h=22, blur=3):
    """
    读入图片，进行初步处理（线条加粗，通道转换）
    :param img_path: 输入图像地址
    :param w: 水平画板数量
    :param h: 竖直画板数量
    :param blur: 轮廓加粗
    :return:
    """
    if isinstance(img_path, str):
        img_path = cv2.imread(img_path, -1)
    # print(img)
    # 如果通道数为4 （RGBA）转换为RGB
    if (img_path.shape[2]) == 4:
        img_path = cv2.cvtColor(img_path, cv2.COLOR_BGRA2BGR)
    if blur:
        # 如果blur不为0
        edge_black_img = edgeBlack(img_path, blur)
    else:
        edge_black_img = img_path
    out_array = minify(edge_black_img, w, h)
    return out_array


if __name__ == '__main__':
    img = cv.imread("test.png")
    edgeBlackImg = edgeBlack(img)
    out = minify(edgeBlackImg, 92, 55)

    cv2.imwrite("out.png", out)
    cv.waitKey(0)
