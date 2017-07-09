# -*- coding: utf-8 -*-

import sys
from mcpi.minecraft import Minecraft
from PIL import Image

#mc = Minecraft.create()
#mc.postToChat(__file__)

# wool color BGR
woolColors = [
    [221,221,221],  # 0: White
    [62,125,219], # 1: Orange
    [188,80,179], # 2: Magenta
    [201,138,107], # 3: Light blue
    [39,166,177], # 4: Yellow
    [56,174,65], # 5: Lime
    [153,132,208], # 6: Pink
    [64,64,64], # 7: Gray
    [161,161,154], # 8: Light gray
    [137,110,46], # 9: Cyan
    [181,61,126], # 10: Purple
    [141,56,46], # 11: Blue
    [31,50,79], # 12: Brown
    [27,70,53], # 13: Green
    [48,52,150], # 14: Red
    [22,22,25] # 15:Black
]


print("ファイル名を入力")

file = input()
#print(file)

img = Image.open(file,"r")
img.thumbnail((128, 128))
img.show()

