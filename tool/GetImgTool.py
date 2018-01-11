# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 00:40
# @desc    : adb 获取截屏，截取图片


from PIL import Image
import os
import matplotlib.pyplot as plt


img = Image.open("../1.png")

# 用 matplot 查看测试分辨率，切割
#region = img.crop((50, 350, 1000, 560)) # 坚果 pro1
img = img.resize((1080, 1920))
region = img.crop((75, 315, 1167, 1200)) # iPhone 7P

im = plt.imshow(img, animated=True)
im2 = plt.imshow(region, animated=True)
plt.show()