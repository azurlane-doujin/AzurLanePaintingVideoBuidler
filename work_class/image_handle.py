import os
import warnings

import cv2
import numpy

from work_class.image_group import ImageGroup
from work_funcs.paint import drawN


class ImageHandle(object):
    def __init__(self):
        self._path = ''
        self._parent: ImageGroup = ...
        self._value: numpy.ndarray = ...

        self._view_width = 0
        self._view_height = 0

        self._scale_img: numpy.ndarray = ...
        self._draw_img: numpy.ndarray = ...
        self._draw_scale_img: numpy.ndarray = ...

    def __call__(self, *args, **kwargs):
        if self.depth == 4:
            return cv2.cvtColor(self._value, cv2.COLOR_BGRA2RGB)
        else:
            return cv2.cvtColor(self._value, cv2.COLOR_BGR2RGB)

    @staticmethod
    def load_from_file(file_path: str):
        if os.path.isfile(file_path):
            path = file_path
            image = ImageHandle()
            image.path = path
            return image

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, file_path):
        if os.path.isfile(file_path):
            self._path = file_path

    @property
    def frame(self):
        assert self._value is not Ellipsis, "未加载图像"
        return self._value

    @frame.setter
    def frame(self, value):
        if isinstance(value, numpy.ndarray):
            self._value = value

    @property
    def wide(self):
        assert self._value is not Ellipsis
        return self._value.shape[1]

    @property
    def high(self):
        assert self._value is not Ellipsis
        return self._value.shape[0]

    @property
    def depth(self):
        assert self._value is not Ellipsis
        return self._value.shape[2]

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        if isinstance(parent, ImageGroup):
            self._parent = parent

    def build_board_img(self):
        assert self._value is not Ellipsis

        val = drawN(self._value, self.parent.board_wide, self.parent.board_high,
                    self.parent.blur)
        self._draw_img = cv2.cvtColor(numpy.array(val), cv2.COLOR_RGB2BGR)

    async def view_size(self, wide, high) -> numpy.ndarray:
        """
        生成符合显示区域尺寸的图片
        :param wide: 显示区域宽
        :param high: 显示区域高
        :return: 生成的图片
        """
        if self._value is Ellipsis:
            self.frame = cv2.imread(self.path)

        self._view_height = high
        self._view_width = wide

        array = numpy.zeros((high, wide, 3), numpy.uint8)
        array.fill(255)

        scale = min(high / self.high, wide / self.wide)

        if self._parent.type == 0:
            img = cv2.resize(self._value, (round(self.wide * scale), round(self.high * scale)))
        else:
            self.build_board_img()
            img = cv2.resize(self._draw_img, (round(self.wide * scale), round(self.high * scale)))
        if self.depth == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        array[
        round((array.shape[0] / 2) - (img.shape[0] / 2)):
        round((array.shape[0] / 2) - (img.shape[0] / 2) + img.shape[0]),
        round((array.shape[1] / 2) - (img.shape[1] / 2)):
        round((array.shape[1] / 2) - (img.shape[1] / 2)) + img.shape[1]
        ] = img

        if array.shape[2] == 4:
            array = cv2.cvtColor(array, cv2.COLOR_BGRA2BGR)

        array = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)

        if self.parent.type == 0:
            self._scale_img = array
        else:
            self._draw_scale_img = array

        return array

    def clear(self):
        self._value = ...
        self._scale_img = ...
        self._draw_img = ...
        self._draw_scale_img = ...
