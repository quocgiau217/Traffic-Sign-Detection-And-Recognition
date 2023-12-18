import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import tensorflow as tf
import cv2
import os

# Set environment variable
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Initialize the Tkinter GUI
top = tk.Tk()
top.geometry('800x600')  # Đã thay đổi kích thước
top.title('Traffic Sign Recognition')
top.configure(background='grey')

# Label for displaying the sign description
label = Label(top, background='black', font=('arial', 25, 'bold'))
label.pack(pady=20)  # Đã thay đổi khoảng cách

# Label for displaying the uploaded image
sign_image = Label(top)
sign_image.pack(padx=20, pady=10)  # Đã thay đổi khoảng cách

# Load the pretrained model
classify_model = tf.keras.models.load_model('CNN_BEST.h5', compile=False)

# Dictionary to label all traffic signs classes
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',
            3:'Speed limit (50km/h)',
            4:'Speed limit (60km/h)',
            5:'Speed limit (70km/h)',
            6:'Speed limit (80km/h)',
            7:'End of speed limit (80km/h)',
            8:'Speed limit (100km/h)',
            9:'Speed limit (120km/h)',
           10:'No passing',
           11:'No passing veh over 3.5 tons',
           12:'Right-of-way at intersection',
           13:'Priority road',
           14:'Yield',
           15:'Stop',
           16:'No vehicles',
           17:'Veh > 3.5 tons prohibited',
           18:'No entry',
           19:'General caution',
           20:'Dangerous curve left',
           21:'Dangerous curve right',
           22:'Double curve',
           23:'Bumpy road',
           24:'Slippery road',
           25:'Road narrows on the right',
           26:'Road work',
           27:'Traffic signals',
           28:'Pedestrians',
           29:'Children crossing',
           30:'Bicycles crossing',
           31:'Beware of ice/snow',
           32:'Wild animals crossing',
           33:'End speed + passing limits',
           34:'Turn right ahead',
           35:'Turn left ahead',
           36:'Ahead only',
           37:'Go straight or right',
           38:'Go straight or left',
           39:'Keep right',
           40:'Keep left',
           41:'Roundabout mandatory',
           42:'End of no passing',
           43:'End no passing veh > 3.5 tons' }

# Preprocess an image for classification
def preprocess_image(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (32, 32))
    image = image / 255.0
    return image

# Function to classify input image
def process_image(image_path):
    frame = cv2.imread(image_path)
    input_image = preprocess_image(frame)
    pred = classify_model.predict(np.expand_dims(input_image, axis=0))
    sign = classes[np.argmax(pred[0]) + 1]
    label.configure(foreground='white', text=sign)

# Function to create a button for classifying input image
def show_classify_button(file_path):
    classify_b = Button(top, text="Classify image", command=lambda: process_image(file_path), padx=12, pady=5)
    classify_b.configure(background="#364156", foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.50, rely=0.18)  # Đã thay đổi vị trí

# Function for uploading the image
def upload_image():
    try:
        file_path = filedialog.askopenfilename()  # Open a file dialog to choose an image
        uploaded = Image.open(file_path)
        uploaded.thumbnail((10000, 10000))  # Đã thay đổi kích thước
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im

        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

# Creating button for uploading the input image
upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.place(relx=0.29, rely=0.18)  # Đã thay đổi vị trí
sign_image.pack(side= BOTTOM, padx=5, pady=70, expand=True)
label.pack(side=BOTTOM, padx=40, pady=70,fill= X, expand= True)

# Adding the heading
heading = Label(top, text="Which traffic sign is this?", pady=25, font=('arial', 20, 'bold'))
heading.configure(background='black', pady=7, padx=7, foreground='white')  # Đã thay đổi khoảng cách
heading.pack(padx=4, pady=3)  # Đã thay đổi khoảng cách

# Run the GUI
top.mainloop()
