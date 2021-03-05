from tkinter import *
import cv2
from PIL import Image, ImageTk
import time

class Visualization:

    def __init__(self,take_one,ten_in_a_row):
        window = Tk()
        window.title('my window')
        window.geometry('1300x700')

        canvas1 = Canvas(window, height=600, width=1300)
        image_file = PhotoImage(file='visualize_img/胡桃池图.png')
        canvas1.create_image(0, 0, anchor='nw', image=image_file)
        canvas1.place(x=0,y=0)
        self.image_file2 = PhotoImage(file='visualize_img/祈愿1次.png')
        self.image_file3 = PhotoImage(file='visualize_img/祈愿10次.png')
        self.visualize_extractor(take_one, ten_in_a_row, window)

        window.mainloop()

    def visualize_extractor(self,take_one,ten_in_a_row,window):
        self.danchouButton = Button(window, width=225,height=46,text='单抽慢性死亡', command=lambda:self.outcome_show(window,take_one),image=self.image_file2)
        self.danchouButton.place(x=776,y=524)

        self.shilianButton = Button(window, width=225,height=46,text='十连瞬间暴毙', command=lambda:self.outcome_show(window,ten_in_a_row),image=self.image_file3)
        self.shilianButton.place(x=1030,y=524)

    def video_loop(self,win,extractor_way):
        (animation_path,img_path),baodi_info = extractor_way()
        vc = cv2.VideoCapture('pray_animation/'+animation_path+'.mp4')
        canvas = Canvas(win, height=700, width=1300)
        canvas.place(x=0, y=0)
        while 1:
            ref,frame = vc.read()
            if ref:
                cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pilImage = Image.fromarray(cvimage)
                pilImage = pilImage.resize((1300, 700))
                picture1 = ImageTk.PhotoImage(image=pilImage)
                canvas.create_image(0,0,anchor='nw',image=picture1)
                win.update()
            else:
                canvas.destroy()
                break
        return img_path,baodi_info

    def outcome_show(self,win,extractor_way):
        img_path,baodi_info = self.video_loop(win,extractor_way)
        canvas_list = [i for i in range(10)]
        image_file_list = [i for i in range(10)]
        if len(img_path) == 1:
            canvas = Canvas(win, height=100, width=1000)
            image_file = PhotoImage(file=img_path)
            canvas.create_image(0, 0, anchor='nw', image=image_file)
            canvas.place(x=300, y=600)

        else:
            for i,path in enumerate(img_path):
                canvas_list[i] = Canvas(win, height=100, width=100,)
                image_file_list[i] = PhotoImage(file=path)
                canvas_list[i].create_image(0, 0, anchor='nw', image=image_file_list[i])
                canvas_list[i].place(x=300+i*100, y=600)
        baodi_label = Label(win, height=6, width=37, text=baodi_info, bg='yellow',font=('Arial,25'))
        baodi_label.place(x=0,y=600)
        win.mainloop()

