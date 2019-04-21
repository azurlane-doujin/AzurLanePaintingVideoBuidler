import cv2

from work_class import image_handle


class VideoHandle(cv2.VideoCapture):
    def __init__(self, video_path: str = None):
        self.video_path = video_path

        super(VideoHandle, self).__init__(video_path)

        assert self.isOpened()

        self._fps = self.get(cv2.CAP_PROP_FPS)
        self._coder = self.get(cv2.CAP_PROP_FOURCC)
        self._counts = self.get(cv2.CAP_PROP_FRAME_COUNT)
        self._width = self.get(cv2.CAP_PROP_FRAME_WIDTH)
        self._height = self.get(cv2.CAP_PROP_FRAME_HEIGHT)

        self.now_frame = 1

        self._time = self._counts / self._fps / 60

    def __iter__(self):
        return self

    def __next__(self):
        if self.get(cv2.CAP_PROP_POS_AVI_RATIO) == 1:
            raise StopIteration
        else:
            rat, frame = self.read()
            self.now_frame += 1
            if rat:
                val = image_handle.ImageHandle()
                val.frame = frame
                return val
            else:
                raise StopIteration

    def __getitem__(self, item):
        item = item + 1
        self.set(cv2.CAP_PROP_POS_FRAMES, item)
        rat, frame = self.read()
        self.set(cv2.CAP_PROP_POS_FRAMES, self.now_frame)
        if rat:
            val = image_handle.ImageHandle()
            val.frame = frame

            return val
