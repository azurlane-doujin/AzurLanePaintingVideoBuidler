import os
import asyncio

__Author__ = "Jacky"

"""
    GUI界面的窗口类
    MainFrame ->主窗口
    
"""

import wx

from work_class import video_handle, image_handle, build_class


class MainFrame(build_class.MainFrame):
    def __init__(self, parent, path=os.getcwd(), args=None):
        super(MainFrame, self).__init__(parent)

        self.args = args
        self.path = path
        self.dialog = None
        self.parent = parent
        self._type = None
        # type=1 ->video
        # type=2 ->images
        self.item = None
        self.bitmap = None

        self._broad_size = [1, 1]
        self._blur = 0

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        assert not (value == 0 or value == 1)
        if value == 1 and not isinstance(self.item, video_handle.VideoHandle):
            self.item = video_handle.VideoHandle()
        elif value == 2 and not isinstance(self.item, image_handle.ImageGroup):
            self.item = image_handle.ImageGroup()

        self._type = value

    # both
    def set_blur(self, event):
        val: str = event.GetString()
        if val.isdigit():
            self.item.set_blur(int(val))
            self._blur = int(val)

    def blur_wheel(self, event):
        angle = event.GetWheelRotation()

        val = angle / 120

        if (val + self._blur) % 2 != 0:
            val = val + self._blur
        else:
            val = val + self._blur + 1 * (val / abs(val))
        if val <= 0:
            val = 0

        val = int(val)
        if self.type == 1:
            self.m_textCtrl_blur.SetValue(str(val))
        else:
            self.m_textCtrl_blur_img.SetValue(str(val))

    def set_high(self, event):
        val: str = event.GetString()
        if val.isdigit():
            self._broad_size[1] = int(val)
            self.item.set_board_size(*self._broad_size)

    def high_wheel(self, event):
        angle = event.GetWheelRotation()
        val = angle / 120
        val = self._broad_size[1] + val
        if val <= 1:
            val = 1
        val = int(val)

        if self.type == 1:
            self.m_textCtrl_high.SetValue(str(val))
        else:
            self.m_textCtrl_high_img.SetValue(str(val))

    def set_wide(self, event):
        val: str = event.GetString()
        if val.isdigit():
            self._broad_size[0] = int(val)
            self.item.set_board_size(*self._broad_size)

    def wide_wheel(self, event):
        angle = event.GetWheelRotation()
        val = angle / 120
        val = self._broad_size[0] + val
        if val <= 1:
            val = 1
        val = int(val)

        if self.type == 1:
            self.m_textCtrl_wide.SetValue(str(val))
        else:
            self.m_textCtrl_wide_img.SetValue(str(val))

    def view_select(self, event):
        self.item.type = event.GetSelection()

    # image handle
    def load_image(self, event):
        """
        加载图像
        :param event:
        :return:
        """
        self.dialog = wx.FileDialog(self, "加载图片（可多选）", self.path, '', "所有文件|*.*||*.png||*.jpg||*.jpeg||*.bmp",
                                    wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE | wx.FD_OPEN)

        if self.dialog.ShowModal() == wx.ID_OK:
            self.type = 2
            list(map(lambda x: self.item.append(image_handle.ImageHandle.load_from_file(x)), self.dialog.GetPaths()))

            self.m_listBox_input_image.Clear()
            self.m_listBox_input_image.Set(self.item.for_show)

    def view_img(self, event):
        """显示图像"""
        select = event.GetSelection()
        self.item.clear()
        value: image_handle.ImageHandle = self.item[select]
        size = self.m_bitmap_show.GetSize()

        asyncio.run(self.main(value, size), debug=True)
        self.m_staticText_info.SetLabel("处理中")

    async def main(self, value, size):
        image = await value.view_size(size[0], size[1])

        self.bitmap = wx.Bitmap.FromBuffer(size[0], size[1], image)
        self.m_bitmap_show.SetBitmap(self.bitmap)
        self.m_staticText_info.SetLabel("完成")
