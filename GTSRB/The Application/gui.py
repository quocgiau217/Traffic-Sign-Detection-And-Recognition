import tkinter as tk
from tkinter import filedialog
from processing import process_image, process_video, process_camera
from PIL import ImageTk, Image

from sign_description import get_sign_description

def choose_and_process():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.mp4")])

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png')):
        process_image(file_path)
    elif file_path.lower().endswith('.mp4'):
        process_video(file_path)

def use_camera():
    process_camera()

root = tk.Tk()
root.title("Traffic Sign Detection")
root.geometry('800x600')  # Đã thay đổi kích thước
root.configure(background='grey')
# Label for displaying the uploaded image

button = tk.Button(root, text="Choose and Process", command=choose_and_process)
button.pack(pady=20)

camera_button = tk.Button(root, text="Use Camera", command=use_camera)
camera_button.pack(pady=20)
root.mainloop()
