import tkinter as tk
from tkinter import messagebox
from components.Window import Window
from components.Button import ButtonImage
import time
import random
from components.Music import PlayDing

class SceneInit:
    def __init__(self, root, scene_name, result_final):
        self.root = root
        self.result_final = result_final
        self.indice_trouve = []

        self.timer = 10

        self.counter = 0

        self.images = "./assets/scene/" + scene_name + ".png"
        self.window = Window(self.root, self.images)
        self.canvas = self.window.canvas

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.label = tk.Label(text=self.timer, font=('Poppins', 40), fg="orange", background="blue")
        self.label.place(x=(self.screen_width//2) - 20, y=50)

        
        self.labelCount = tk.Label(text=self.counter, font=('Poppins', 40), fg="orange", background="blue")
        self.labelCount.place(x=50, y=50)

        let = ["object_cahier.png", "object_chaise.png", "object_livre.png", "object_loupe.png", 
               "object_plaque.png", "object_sablier.png", "object_sac.png", "object_stylo.png"]

        for i in range(len(let)):
            
            btnImage = ButtonImage(
                parent_canvas=self.canvas,
                x=random.randint(0, self.screen_width - 100),
                y=random.randint(0, self.screen_height - 100),
                img_normal_path="./assets/material/" + let[i],
                img_hover_path="./assets/material/" + let[i],
                width=130,
                height=90,
                command=self.clickObject
            )

        self.updateClock()

    
    def updateClock(self):
        if self.timer > 0:
            self.label.configure(text = self.timer)
            self.timer -= 1
            self.root.after(1000, self.updateClock)
        else:
            self.showFinalModal()
    
    
    def showFinalModal(self):
        myLine = self.canvas.create_rectangle(0, 0, self.screen_width, self.screen_height, fill='black', stipple="gray50")

        back_btn = ButtonImage(
            parent_canvas=self.canvas,
            x=(self.screen_width // 2) - 100,
            y=(self.screen_height) - 100,
            img_normal_path="./assets/main/back_btn.png",
            img_hover_path="./assets/main/back_btn.png",
            width=200,
            height=85,
            command=self.backBtnCLick
        )


    def gameIsFinish(self, suspects, waypon):
        if self.isTheCriminal(suspects) and self.isTheWaypon(waypon):
            return True
        else:
            return False
    
    def isTheCriminal(self, suspects):
        if suspects == self.result_final[0]:
            return True
        else:
            return False

    def isTheWaypon(self, waypon):
        if waypon == self.result_final[1]:
            return True
        else:
            return False
    
    def backBtnCLick(self):
        from interface.MainMenu import MainMenu
        self.canvas.destroy()
        MainMenu(self.root)
    
    def clickObject(self):
        PlayDing("./assets/ding_music.mp3")
        self.counter += 1
        self.labelCount.configure(text = self.counter)