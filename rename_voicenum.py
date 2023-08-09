import os
import sys


def rename():
    path = input("请输入读取路径(例如D:\\\\picture)：")
    name = input("请输入命名前缀:")
    startNumber = input("请输入开始数:")
    fileType = input("请输入后缀名（如 .jpg、.txt等等）:")
    print("正在生成以" + name + startNumber + fileType + "迭代的文件名")
    count = 0
    filelist = os.listdir(path)
    for files in filelist:
        num = files.split(".")[0].split("_")[-1]
        filename_change = name + num.zfill(6) + fileType
        os.rename(os.path.join(path, files), os.path.join(path, filename_change))


rename()