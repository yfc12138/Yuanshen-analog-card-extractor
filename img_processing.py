import os
from PIL import  Image
import os.path

def img_show(results):
    img_path = [('all_imgs_resize/'+result+'.png') for result in results]
    return img_path


def lists_gen(root):         #通过检查imgs分类生成各个人物、武器列表
    list = os.listdir(root)
    name_list = [name[:-4] for name in list]
    return name_list

def convertjpg(pngfile,outir,width = 100 ,height = 100):
    img = Image.open(pngfile)
    try:
        new_img = img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outir,os.path.basename(pngfile)))
    except Exception as e:
        print(e)