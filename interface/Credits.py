import tkinter as tk
from components.Window import Window
from components.Button import ButtonImage

class Credits:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)

        window = Window(self.root, "./assets/credits_background.png")
        self.canvas = window.canvas

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        back_btn = ButtonImage(
            parent_canvas=self.canvas,
            x=120,
            y=60,
            img_normal_path="./assets/main/back_btn.png",
            img_hover_path="./assets/main/back_btn.png",
            width=200,
            height=85,
            command=self.backBtnCLick
        )
    
    def backBtnCLick(self):
        from interface.MainMenu import MainMenu
        self.canvas.destroy()
        MainMenu(self.root)