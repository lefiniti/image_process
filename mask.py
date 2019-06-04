import numpy as np
from PIL import Image
import random
import os

def method(depts, start, end):
    '''
    :param depts: 马瑟克块元素大小
    :param start: 马赛克横坐标起点元组
    :param end: 马赛克纵坐标起始点元组
    :return:
    主要通过中间值的rgb对局部范围块的rgb做修改，depts值越小越精确
    '''
    im1 = np.array(Image.open(r"D:\job\image_mask\image\mask0.jpg"))
    for i in range(start[0], start[1], depts):
        for j in range(end[0], end[1], depts):
            im1[i:i + depts, j:j + depts] = im1[i + (depts // 2)][j + (depts // 2)]
    im2 = Image.fromarray(im1.astype("uint8"))
    im2.show()
    im2.save(r"D:\job\image_mask\image\test_mask.png")


if __name__ == '__main__':
    
    '''方法2（通过选中范围的中间值颜色数组打马赛克）'''
    method(5, (217, 246), (162, 231))
