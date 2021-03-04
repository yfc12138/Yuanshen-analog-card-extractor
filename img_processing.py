import os


def img_show(results):
    img_path = [('all_imgs_resize/'+result+'.png') for result in results]
    return img_path


def lists_gen(root):         #通过检查imgs分类生成各个人物、武器列表
    list = os.listdir(root)
    name_list = [name[:-4] for name in list]
    return name_list