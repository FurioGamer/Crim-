import tkinter as tk
from components.Window import Window
from components.Button import ButtonImage


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.attributes("-fullscreen", True)

        window = Window(self.root, "./assets/main_background.png")
        self.canvas = window.canvas

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        logoImages = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2),
            y=(self.screen_height // 2) - 300,
            img_normal_path="./assets/icons.png",
            img_hover_path="./assets/icons.png",
            width=500,
            height=190,
            command=None
        )

        play_button = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2),
            y=(self.screen_height // 2) - 70,
            img_normal_path="./assets/main/play_btn.png",
            img_hover_path="./assets/main/play_btn_hover.png",
            width=500,
            height=110,
            command=self.on_play_click
        )

        credits_btn = ButtonImage(
            parent_canvas=window.canvas,
            x=(self.screen_width // 2),
            y=(self.screen_height // 2) + 50,
            img_normal_path="./assets/main/credits_btn.png",
            img_hover_path="./assets/main/credits_btn_hover.png",
            width=500,
            height=110,
            command=self.on_credits_click
        )

        close_btn = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2),
            y=(self.screen_height // 2) + 170,
            img_normal_path="./assets/main/quit_btn.png",
            img_hover_path="./assets/main/quit_btn_hover.png",
            width=500,
            height=110,
            command=self.root.destroy
        )
    
    def on_play_click(self):
        from interface.Maps import Maps
        self.canvas.destroy()
        Maps(self.root)

    def on_credits_click(self):
        from interface.Credits import Credits
        self.canvas.destroy()
        Credits(self.root)