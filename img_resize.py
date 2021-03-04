# -*- coding:utf8 -*-
from PIL import  Image
import os.path

def convertjpg(pngfile,outir,width = 100 ,height = 100):
    img = Image.open(pngfile)
    try:
        new_img = img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outir,os.path.basename(pngfile)))
    except Exception as e:
        print(e)



