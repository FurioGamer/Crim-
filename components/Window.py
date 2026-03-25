import tkinter as tk
from PIL import Image, ImageTk

class Window:
    def __init__(self, root, bg_path):
        """
        Crée une fenêtre fullscreen avec background responsive.

        :param root: Tkinter root
        :param bg_path: Chemin de l'image de background
        """
        self.root = root
        self.root.title("TheDyl - Criminal Enquête")
        self.root.attributes("-fullscreen", True)

        self.bg_original = Image.open(bg_path)
        self.bg_image = None

        self.canvas = tk.Canvas(self.root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Configure>", self.on_resize)

    # =====================
    # Redimensionnement automatique
    # =====================
    def on_resize(self, event):
        resized = self.bg_original.resize((event.width, event.height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized)

        self.canvas.delete("bg")
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw", tags="bg")
        self.canvas.tag_lower("bg")

    # =====================
    # Ajouter un bouton (ou widget) sur le canvas
    # =====================
    def add_widget(self, widget, x, y):
        """
        Place un widget sur le canvas à la position (x, y)
        :param widget: widget Tkinter à placer
        :param x: coordonnée x
        :param y: coordonnée y
        """
        return self.canvas.create_window(x, y, window=widget)

    def clearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()