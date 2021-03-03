from tkinter import *
from img_processing import *
import cv2

class Visualization:

    def __init__(self,Img,take_one,ten_in_a_row):


        window = Tk()
        window.title('my window')
        window.geometry('1300x600')

        canvas1 = Canvas(window, height=600, width=1300)
        image_file = PhotoImage(file='visualize_img/胡桃池图.png')
        image = canvas1.create_image(0, 0, anchor='nw', image=image_file)
        canvas1.place(x=0,y=0)

        self.visualize_extractor(Img, take_one, ten_in_a_row, window)

        window.mainloop()


    def visualize_extractor(self,Img,take_one,ten_in_a_row,window):
        self.danchouButton = Button(window, width=30,height=2,text='单抽慢性死亡', command=lambda: take_one(Img))
        self.danchouButton.place(x=780,y=525)

        self.shilianButton = Button(window, width=30,height=2,text='十连瞬间暴毙', command=lambda :ten_in_a_row(Img))
        self.shilianButton.place(x=1035,y=525)



# # 图像转换，用于在画布中显示
# def tkImage(vc):
#     ref, frame = vc.read()
#     cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     pilImage = Image.fromarray(cvimage)
#     pilImage = pilImage.resize((image_width, image_height), Image.ANTIALIAS)
#     tkImage = ImageTk.PhotoImage(image=pilImage)
#     return tkImage
#
# def video_loop():
#     while True:
#         picture1 = tkImage(vc1)
#         canvas1.create_image(0, 0, anchor='nw', image=picture1)
#         win.update_idletasks()  # 最重要的更新是靠这两句来实现
#         win.update()
#
# # 图像的显示与更新
# def video():
#     video_loop()
#     win.mainloop()
#     # vc1.release()
#     # cv2.destroyAllWindows()