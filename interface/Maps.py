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

        firstScene = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2) - 100,
            y=(self.screen_height // 2) - 180,
            img_normal_path="./assets/main/round_parc.png",
            img_hover_path="./assets/main/round_hover_parc.png",
            width=200,
            height=200,
            command=self.firstScene
        )

        secondScene = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2) + 100,
            y=(self.screen_height // 2) - 180,
            img_normal_path="./assets/main/round_serveur.png",
            img_hover_path="./assets/main/round_hover_serveur.png",
            width=200,
            height=200,
            command=self.secondScene
        )


    def backBtnCLick(self):
        from interface.MainMenu import MainMenu
        self.canvas.destroy()
        MainMenu(self.root)
    
    def firstScene(self):
        from components.SceneInit import SceneInit
        self.canvas.destroy()
        SceneInit(self.root, "scene_parc", [])

    def secondScene(self):
        from components.SceneInit import SceneInit
        self.canvas.destroy()
        SceneInit(self.root, "scene_serveur", [])