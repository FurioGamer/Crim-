import tkinter as tk
from tkinter import messagebox
from components.Window import Window
from components.Button import ButtonImage
import time
import random

class SceneInit:
    def __init__(self, root, scene_name, result_final):
        self.root = root
        self.result_final = result_final
        self.indice_trouve = []

        self.timer = 10

        self.images = "./assets/scene/" + scene_name + ".png"
        self.window = Window(self.root, self.images)
        self.canvas = self.window.canvas

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.label = tk.Label(text=self.timer, font=('Poppins', 40), fg="orange", background="blue")
        self.label.place(x=self.screen_width//2, y= self.screen_height//2)

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

        random.randint(1, 9)
            

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