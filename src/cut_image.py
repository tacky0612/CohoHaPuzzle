from PIL import Image
import os
import sys


def ImgSplit(im):
    height = 294
    width = 294

    buff = []
    # 縦の分割枚数
    for h1 in range(4):
        # 横の分割枚数
        for w1 in range(4):
            w2 = w1 * height
            h2 = h1 * width
            c = im.crop((w2, h2, width + w2, height + h2))
            buff.append(c)
    return buff


if __name__ == '__main__':
    im = Image.open('../image/answer.png')
    ig = ImgSplit(im)
    for i in range(len(ig)):
        ig[i].save("../image/" + str(i) + ".png", "PNG")
