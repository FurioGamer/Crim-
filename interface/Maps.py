import tkinter as tk
from components.Window import Window
from components.Button import ButtonImage

class Maps:
    def __init__(self, root, counter=0):
        self.root = root
        self.counter = counter

        window = Window(self.root, "./assets/main_background.png")
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


        play_button = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2) - 100,
            y=(self.screen_height // 2) - 180,
            img_normal_path="./assets/main/round.png",
            img_hover_path="./assets/main/round_hover.png",
            width=200,
            height=200,
            command=None
        )



    def backBtnCLick(self):
        from interface.MainMenu import MainMenu
        self.canvas.destroy()
        MainMenu(self.root)
        
        # from components.SceneInit import SceneInit
        # self.canvas.destroy()
        # SceneInit(self.root, "scene_parc", [])
