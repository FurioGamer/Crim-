import tkinter as tk
from components.Window import Window
from components.Button import ButtonImage
from components.SceneInit import SceneInit

class Scene:
    def __init__(self, root, counter):
        self.root = root
        self.counter = counter

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()


        while self.root.mainloop():

            self.scene = SceneInit(self.root, SceneComponent[self.counter][0], SceneComponent[self.counter][1])


            while self.scene.gameIsFinish != True:
                print
            
            self.counter += 1

            from interface.Maps import Maps
            self.canvas.destroy()
            Maps(self.root, counter)
            

SceneComponent = [
    ["scene_classe", []],
    ["scene_manoir", []],
    ["scene_parc", []],
    ["scene_serveur", []],
    ["scene_train", []]
]