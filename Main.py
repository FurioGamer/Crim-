import tkinter as tk
from components.Music import PlayMusic
from interface.MainMenu import MainMenu


root = tk.Tk()

PlayMusic("./assets/main_music.mp3")

if __name__ == "__main__":
    MainMenu(root)

root.mainloop()