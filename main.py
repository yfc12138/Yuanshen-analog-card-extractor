import random
import keyboard
import time

three_stars_weapons="*弹弓 *鸦羽弓 *讨龙英杰谭 *黑缨枪 *沐浴龙血的剑 *飞天御剑 *冷刃 *神射手之誓 *翡玉法球 *魔岛绪论 *以理服人 *铁影阔剑 *黎明神剑".split()
four_stars_figures ="**雷泽 **香菱 **北斗 **行秋 **菲谢尔 **诺艾尔 **重云 **迪奥娜 **砂糖 *辛炎 **芭芭拉 **凝光 **班尼特".split()
four_stars_weapons ="**西风剑 **笛剑 **祭礼剑 **匣里龙吟 **西风大剑 **钟剑 **祭礼大剑 **雨裁 **匣里灭辰 **西风长枪 **西风秘典 **流浪乐章 **祭礼残章 **昭心 **西风烈弓 **绝弦 **祭礼弓 **弓藏".split()
four_stars = four_stars_weapons + four_stars_figures
five_stars_figures ="***琴 ***迪卢克 ***七七 ***莫娜 ***刻晴".split()


def random_gen(max_index) -> int:
        return random.randint(0,max_index)

four_stars_count = 0
five_stars_count = 0
four_stars_miss = False
five_stars_miss = False

def five_stars_func():
    global five_stars_miss
    global five_stars_count
    global four_stars_count
    four_stars_count = 0
    five_stars_count = 0
    num = random_gen(1)
    if five_stars_miss == True:
        five_stars_miss = False
        return five_stars_figures[-1]
    elif num==1:
        return five_stars_figures[-1]
    else:
        num2 = random_gen(3)
        five_stars_miss = True
        return five_stars_figures[num2]

def four_stars_func():
    global four_stars_miss
    global four_stars_count
    global five_stars_count
    four_stars_count = 0
    five_stars_count = five_stars_count + 1
    num = random_gen(1)
    num2 = random_gen(2)
    num3 = random_gen(27)
    if four_stars_miss == True:
        four_stars_miss = False
        return four_stars[-num2]
    elif num==1:
        return four_stars[-num2]
    else:
        four_stars_miss = True
        return four_stars[-num3]

def three_stars_func():
    global four_stars_count
    global five_stars_count
    four_stars_count=four_stars_count + 1
    five_stars_count=five_stars_count + 1
    num = random_gen(12)
    return three_stars_weapons[num]

def extractor():
    num = random_gen(9999)
    if five_stars_count == 89:
        return five_stars_func()
    elif four_stars_count == 9:
        return four_stars_func()
    elif num<60:
        return five_stars_func()
    elif num<570:
        return four_stars_func()
    else:
        return three_stars_func()

def ten_in_a_row():
    result = []
    for i in range(10):
        result.append(extractor())
    print(result)
    return result

if __name__=='__main__':
    while 1:
        if keyboard.is_pressed('q'):
            ten_in_a_row()
            time.sleep(0.1)



