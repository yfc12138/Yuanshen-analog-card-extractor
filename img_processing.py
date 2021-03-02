import os
import cv2
import numpy as np

class Imgs:                #

    def __init__(self,root):
        self.root = root

    def imgs_return(self,name):
        img_path = os.path.join(self.root,name)
        # img = cv2.imread(img_path)
        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), -1)  #读取图片中含中文路径需要先用numpy读取为uint8格式,再用imdecode解码
        img = cv2.resize(img,(100,100))
        return img

def lists_gen(root):         #通过检查imgs分类生成各个人物、武器列表
    list = os.listdir(root)
    name_list = [name[:-4] for name in list]
    return name_list

def img_show(results,Img):
    img = []
    for result in results:
        result = result + '.png'
        img.append(Img.imgs_return(result))
    res = np.hstack(img)
    cv2.imshow('result',res)
    cv2.waitKey(500)