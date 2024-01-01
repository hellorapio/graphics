import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageClipperApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FCI TU Graphics Project, Made with Love")

        self.image_path = None
        self.image = None
        self.rect = None
        self.preview_image = None
        
        self.create_widgets()

    def create_widgets(self):
        open_btn = tk.Button(self.master, text="Open Image", command=self.load_image)
        open_btn.pack(pady=10)

        self.canvas = tk.Canvas(self.master, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        clip_btn = tk.Button(self.master, text="Clip Image", command=self.crop_image)
        clip_btn.pack(pady=10)

        self.master.mainloop()

    def load_image(self):
        file_path = filedialog.askopenfilename()

        if file_path:
            try:
                self.image = Image.open(file_path)

                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()

                if self.image.width > screen_width or self.image.height > screen_height:
                    self.image.thumbnail((screen_width, screen_height))

                photo = ImageTk.PhotoImage(self.image)
                self.canvas.config(width=photo.width(), height=photo.height())
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.image = photo

                self.image_path = file_path

                if self.rect:
                    self.canvas.delete(self.rect)
                if self.preview_image:
                    self.canvas.delete(self.preview_image)

                self.canvas.bind("<ButtonPress-1>", self.on_press)
                self.canvas.bind("<B1-Motion>", self.on_drag)
            except Exception as e:
                messagebox.showerror("Error", f"Error loading image: {e}")

    def crop_image(self):
        if self.image_path is None:
            messagebox.showerror("Error", "No image loaded.")
            return

        if not self.rect:
            messagebox.showerror("Error", "Please draw a rectangle.")
            return

        x1, y1, x2, y2 = self.canvas.coords(self.rect)

        try:
            cropped_image = self.image.crop((x1, y1, x2, y2))

            photo = ImageTk.PhotoImage(cropped_image)
            self.canvas.config(width=photo.width(), height=photo.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo

            cropped_image.save("output_cropped_image.jpg")

            self.canvas.delete(self.rect)
            self.canvas.delete(self.preview_image)
        except Exception as e:
            messagebox.showerror("Error", f"Error cropping image: {e}")

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)
        if self.preview_image:
            self.canvas.delete(self.preview_image)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_drag(self, event):
        cur_x = self.canvas.canvasx(event.x)
        cur_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

        preview_cropped_image = self.image.crop((self.start_x, self.start_y, cur_x, cur_y))
        preview_photo = ImageTk.PhotoImage(preview_cropped_image)

        if self.preview_image:
            self.canvas.delete(self.preview_image)
        self.preview_image = self.canvas.create_image(self.start_x, self.start_y, anchor=tk.NW, image=preview_photo)
        self.canvas.preview_image = preview_photo

root = tk.Tk()
app = ImageClipperApp(root)