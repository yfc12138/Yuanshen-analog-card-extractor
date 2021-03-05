import random
import time
import config
import cv2
import numpy as np
from visualize import Visualization
from img_processing import *

def random_gen(max_index) -> int:
        return random.randint(0,max_index)

four_stars_count = 0  #四星保底，10次必出，出了刷新
five_stars_count = 0  #五星保底，同上
four_stars_miss = False  #四星是否歪了
five_stars_miss = False  #五星是否歪了
take_one_status = None
ten_in_a_row_status = None

def five_stars_func():
    global five_stars_miss
    global five_stars_count
    global four_stars_count
    four_stars_count = 0
    five_stars_count = 0
    num = random_gen(1)
    num2 = random_gen(len(up_five_stars_figures)-1)
    num3 = random_gen(len(five_stars_figures) - 1)
    if five_stars_miss == True:
        five_stars_miss = False
        return up_five_stars_figures[num2]
    elif num==1:
        return up_five_stars_figures[num2]
    else:
        five_stars_miss = True
        return five_stars_figures[num3]

def four_stars_func():
    global four_stars_miss
    global four_stars_count
    global five_stars_count
    four_stars_count = 0
    five_stars_count = five_stars_count + 1
    num = random_gen(1)
    num2 = random_gen(len(up_four_stars_figures)-1)
    num3 = random_gen(len(four_stars)-1)
    if four_stars_miss == True:
        four_stars_miss = False
        return up_four_stars_figures[num2]
    elif num==1:
        return up_four_stars_figures[num2]
    else:
        four_stars_miss = True
        return four_stars[num3]

def three_stars_func():
    global four_stars_count
    global five_stars_count
    four_stars_count=four_stars_count + 1
    five_stars_count=five_stars_count + 1
    num = random_gen(len(three_stars_weapons)-1)
    return three_stars_weapons[num]

def extractor():
    num = random_gen(9999)
    if five_stars_count == 89:
        return five_stars_func()
    elif four_stars_count == 9:
        return four_stars_func()
    elif num<60+max((five_stars_count-50),0)*40:
        return five_stars_func()
    elif num<570+max((five_stars_count-50),0)*40:
        return four_stars_func()
    else:
        return three_stars_func()

def baodi(func):
    def wrapper(*args,**kw):
        result=func(*args, **kw)
        if five_stars_miss:
            baodi_text='当前距离大保底还剩%s发' % (90 - five_stars_count)
        else:
            baodi_text='当前距离小保底还剩%s发' % (90 - five_stars_count)
        return result,baodi_text
    return wrapper

@baodi
def take_one():
    global take_one_status
    result = extractor()
    if result in three_stars_weapons:
        take_one_status = '单抽三星'
    elif result in four_stars_weapons + four_stars_figures:
        take_one_status = '单抽四星'
    else:
        take_one_status = '单抽五星'
    img_path = img_show(result.split())
    print(result.split())
    return take_one_status,img_path

@baodi
def ten_in_a_row():
    global ten_in_a_row_status
    result = [extractor() for i in range(10)]
    ten_in_a_row_status = '十连四星'
    for i in result:
        if i in five_stars_figures+up_five_stars_figures:
            ten_in_a_row_status = '十连五星'
    img_path = img_show(result)
    print(result)
    return ten_in_a_row_status,img_path


if __name__=='__main__':

    opt = config.DefaultConfig()

    #生成武器，角色列表
    three_stars_weapons=lists_gen(opt.three_stars_weapons_root)
    four_stars_figures =lists_gen(opt.four_stars_figures_root)
    four_stars_weapons =lists_gen(opt.four_stars_weapons_root)
    four_stars = four_stars_weapons + four_stars_figures
    five_stars_figures =lists_gen(opt.five_stars_figures_root)
    # five_stars_weapons = lists_gen(opt.five_stars_weapons_root)

    #生成up武器和up角色
    up_five_stars_figures= opt.up_five_stars_figures.split()
    up_four_stars_figures= opt.up_four_stars_figures.split()


    #更新非up池
    for up in up_five_stars_figures:
        five_stars_figures.remove(up)
    for up in up_four_stars_figures:
        four_stars.remove(up)

    for jpgfile in os.listdir("all_imgs"):
        convertjpg("all_imgs/" + jpgfile, "all_imgs_resize")

    Visualization(take_one,ten_in_a_row)

