import tkinter as tk
from PIL import Image, ImageTk


class ButtonImage:
    def __init__(
        self,
        parent_canvas,
        x,
        y,
        img_normal_path,
        img_hover_path,
        width,
        height,
        command=None
    ):
        self.canvas = parent_canvas
        self.command = command

        # Charger et redimensionner les images
        normal_img = Image.open(img_normal_path).resize((width, height), Image.LANCZOS)
        hover_img = Image.open(img_hover_path).resize((width, height), Image.LANCZOS)

        self.normal_photo = ImageTk.PhotoImage(normal_img)
        self.hover_photo = ImageTk.PhotoImage(hover_img)

        # Créer l'image sur le canvas (PAS un Button)
        self.image_id = self.canvas.create_image(
            x,
            y,
            image=self.normal_photo,
            anchor="center"
        )

        # Bind events
        self.canvas.tag_bind(self.image_id, "<Enter>", self.on_hover)
        self.canvas.tag_bind(self.image_id, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.image_id, "<Button-1>", self.on_click)

    # =====================
    # EVENTS
    # =====================
    def on_hover(self, event):
        self.canvas.itemconfig(self.image_id, image=self.hover_photo)

    def on_leave(self, event):
        self.canvas.itemconfig(self.image_id, image=self.normal_photo)

    def on_click(self, event):
        if self.command:
            self.command()