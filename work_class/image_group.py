import collections
import os
from work_class import image_handle


class ImageGroup(list):
    def __init__(self, items: collections.abc.Iterable = None):
        super(ImageGroup, self).__init__()

        self.board_wide = 1
        self.board_high = 1
        self.blur = 0
        self._type = 0

        self._for_show = []

        if items is not None:
            list(map(lambda x: self.append(x), items))

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def for_show(self):
        return self._for_show

    def to_list(self):
        return list([val for val in self])

    def append(self, obj_input) -> None:
        if isinstance(obj_input, image_handle.ImageHandle):
            obj_input.parent = self
            self._for_show.append(f"{len(self)+1}、{os.path.split(obj_input.path)[-1]}")
            super(ImageGroup, self).append(obj_input)
        else:
            pass

    def set_board_size(self, width, height):
        self.board_wide = width
        self.board_high = height

    def set_blur(self, blur):
        self.blur = blur

    def set_type(self, view_type):
        self.type = view_type

    def clear(self):
        list(map(lambda x: x.clear(), self))
