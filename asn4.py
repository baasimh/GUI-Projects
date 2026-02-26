import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class FoodViewer:
    def __init__(self):
        self.root = Tk()
        self.root.title("Food Viewer")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.img_frame = Frame(self.root)
        self.img_frame.pack()

        self.rbdBtn_frame = Frame(self.root)
        self.rbdBtn_frame.pack()

        image_size = (350, 250)

        self.imgOne = self.load_image("chicken.jpg", image_size)
        self.imgTwo = self.load_image("pie.jpg", image_size)
        self.imgThree = self.load_image("pizza.jpg", image_size)
        self.imgFour = self.load_image("steak.jpg", image_size)

        self.lbl = Label(self.img_frame, image=self.imgOne)
        self.lbl.pack()

        self.var = IntVar()
        self.var.set(1)

        Radiobutton(self.rbdBtn_frame, text="Chicken",
                    variable=self.var, value=1,
                    command=self.on_radio_select).pack(side="left", padx=10)

        Radiobutton(self.rbdBtn_frame, text="Pie",
                    variable=self.var, value=2,
                    command=self.on_radio_select).pack(side="left", padx=10)

        Radiobutton(self.rbdBtn_frame, text="Pizza",
                    variable=self.var, value=3,
                    command=self.on_radio_select).pack(side="left", padx=10)

        Radiobutton(self.rbdBtn_frame, text="Steak",
                    variable=self.var, value=4,
                    command=self.on_radio_select).pack(side="left", padx=10)

        self.root.mainloop()

    def load_image(self, filename, size):
        img = Image.open(filename)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)

    def on_radio_select(self):
        choice = self.var.get()

        if choice == 1:
            self.lbl.config(image=self.imgOne)
        elif choice == 2:
            self.lbl.config(image=self.imgTwo)
        elif choice == 3:
            self.lbl.config(image=self.imgThree)
        elif choice == 4:
            self.lbl.config(image=self.imgFour)

if __name__ == "__main__":
    FoodViewer()