# Authors: Robert Layton <robertlayton@gmail.com>
#          Olivier Grisel <olivier.grisel@ensta.org>
#          Mathieu Blondel <mathieu@mblondel.org>
#
# License: BSD 3 clause

""""""

import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle


def make(imgPath, n_color=8):
    """
    生成画板的图像像素参数组
    :param imgPath:输入的图像
    :param n_color:
    :return:生成的图像
    """
    if isinstance(imgPath, str):
        if not imgPath[-3:] == "png":
            rawImage = cv2.imread(imgPath)
        else:
            rawImage = cv2.imread(imgPath, -1)
    else:
        rawImage = imgPath
    # 映射为浮点数
    rawImage = np.array(rawImage, dtype=np.float64) / 255
    w, h, d = tuple(rawImage.shape)
    # 确保通道数为3（RGB）
    assert d == 3
    # 生成一条3通道的
    image_array = np.reshape(rawImage, (w * h, d))

    image_array_sample = shuffle(image_array, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_color, random_state=0).fit(image_array_sample)
    labels = kmeans.predict(image_array)
    # 生成最终画板图像像素参数组
    out_image = recreate_image(kmeans.cluster_centers_, labels, w, h)
    return out_image


def recreate_image(code_book, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    d = code_book.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = code_book[labels[label_idx]]
            label_idx += 1
    return image


if __name__ == '__main__':
    n_colors = 3
    outImg = make("testimg/ysxb.jpg", n_colors)
    outImg *= 255
    outImg = np.array(outImg, dtype='uint8')
    cv2.imshow(f"{n_colors}colors", outImg)
    cv2.waitKey(0)
# plt.figure(2)
# plt.clf()
# plt.axis('off')
# plt.title(f'Quantized image ({n_colors} colors, K-Means)')
