import warnings

import wx
import work_class.frame_class


def getArgs():
    import argparse
    parser = argparse.ArgumentParser(description='碧蓝航线绘图日记像素画生成工具')
    parser.add_argument('-input', metavar='input', type=str, help='input file path', default="")
    parser.add_argument('-o', '--output', type=str, help='output file path. image end by .png,video end by .avi')
    parser.add_argument('-m', '--mode', type=str, help='mode to run this program',
                        choices=["video", "image"], default=None)

    parser.add_argument('-b', '--bold', type=int, help='bold of lines of images,integer', default=0)
    parser.add_argument('-x', '--width', type=int, help='width to run', default=1)
    parser.add_argument('-y', '--height', type=int, help='height to run', default=1)
    parser.add_argument('-c', '--cutFrames', type=int,
                        help='extrace one frame in cutFrame(your input num) frames,mode video only', default=1)
    parser.add_argument("-t", "--type", type=str, help="pregame running type,include {Console,Desktop},if use Desktop "
                                                       "it will ignore other values",
                        choices=("Console", "Desktop"), default="Desktop")
    args = parser.parse_args()
    return args


def mainFunc(args):
    import os

    # 当地址不存在，退出
    if not os.path.exists(args.input):
        warnings.warn("error: input file not found!")
        return
    # 当没有传递 mode,根据文件扩展名判断
    if args.mode == None:
        # 获取文件扩展名
        fileTypeS = args.input.split(".")[-1]
        imageTypes = ("png", "jpg", "jpeg", "bmp")
        videoTypes = ("flv", "mp4", "avi", "mkv", "wma", "rmvb", "mov")

        # 全部转为小写
        fileTypeSLower = fileTypeS.lower()

        if fileTypeSLower in imageTypes:
            args.mode = "image"
        elif fileTypeSLower in videoTypes:
            args.mode = "video"
        else:
            warnings.warn("Warn: con't identify you input file mode,please appoint mode by -m argument")

    # 当为图片处理类型
    if args.mode == "image":
        print(f"start draw image {args.input}......")
        from work_funcs import paint

        # 生成像素画
        o = paint.drawN(args.input, w=args.width, h=args.height, blur=args.bold)
        if args.output is not None:
            oPath = args.output

        else:
            # 当没有传递output时
            warnings.warn("WARN ：'output' path is no find")
            import time
            absInputPath = os.path.abspath(args.input)
            oPaths = os.path.split(absInputPath)
            # 获取输入的文件名
            rawFileName = oPaths[1]
            # 获取input文件名
            outFileName = f"{rawFileName.split('.')[0]}-{int(time.time())}.png"
            oPath = os.path.join(oPaths[0], outFileName)

        o.save(oPath, "PNG")
        print(f"image drawn completed -> {oPath}")
    elif args.mode == "video":
        from work_funcs import analyseVideo

        if not args.output is None:
            oPath = args.output

        else:
            import time

            absInputPath = os.path.abspath(args.input)
            oPaths = os.path.split(absInputPath)
            outFileName = f"{oPaths[1].split('.')[0]}-{int(time.time())}.avi"
            oPath = os.path.join(oPaths[0], outFileName)

        print(f"start handdle video {args.input}......")
        analyseVideo.makeVideo(inputVideoPath=args.input, output=oPath, cutFrames=args.cutFrames, w=args.width,
                               h=args.height, blur=args.bold)
        print(f"video handdled completed -> {oPath}")


if __name__ == '__main__':
    try:
        args = getArgs()
        if args.type.lower() == "console":
            mainFunc(args)
        else:
            app = wx.App()
            frame = work_class.frame_class.MainFrame(None)
            frame.Show()
            app.MainLoop()
    except:
        pass
