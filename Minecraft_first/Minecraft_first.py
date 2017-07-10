# -*- coding: utf-8 -*-

import sys
import math
from mcpi.minecraft import Minecraft
from PIL import Image

mc = Minecraft.create()
mc.postToChat(__file__)

# wool color BGR
woolColors = [
    [221,221,221], # 0: White
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

#print("ファイル名を入力")
#file = input()

file = "sagiri.jpg"
print(file)

img = Image.open(file,"r")
img.thumbnail((128, 128))
#img.show()

img_x, img_y = img.size
print(img_x, img_y)


woolList = [[0 for j in range(img_y)] for i in range(img_x)]


for i in range(img_x):
    for j in range(img_y):
        img_r, img_g, img_b = img.getpixel((i,j))
        #print(img_r, img_g, img_b)

        min_l = -1
        min_pixel_l = 10000

        for k in range(16):

            pixel_l = math.sqrt((img_b - woolColors[k][0])**2 + (img_g - woolColors[k][1])**2 + (img_r - woolColors[k][2])**2)

            if min_pixel_l > pixel_l:

                min_l = k
                min_pixel_l = pixel_l

        woolList[i][j] = min_l
        #print(i, j)
    
#pos_x, pos_y, pos_z = [0,0,0] 
pos_x, pos_y, pos_z = mc.player.getPos()

for i in range(img_x):
    for j in range(img_y):

        mc.setBlock(pos_x + i, pos_y-1, pos_z + j, 35, woolList[i][j])
        #print(i, j, woolList[i][j])

mc.postToChat("Create Image")