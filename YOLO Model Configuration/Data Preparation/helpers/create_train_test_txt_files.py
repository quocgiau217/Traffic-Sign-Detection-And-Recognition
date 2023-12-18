import os
import random
from shutil import copyfile


def create_txt(img_path, choose_type):
    if not os.path.exists('../train_test_txt'):
        os.makedirs('../train_test_txt')
    for filename in os.listdir(img_path):
        if choose_type == "train":
            with open("../train_test_txt/train.txt", "a+") as outfile:
                outfile.write("/content/gdrive/MyDrive/Traffic_recognition/darknet/data/labels/" + filename)
                outfile.write("\n")
                outfile.close()
        else:
            with open("../train_test_txt/test.txt", "a+") as outfile:
                outfile.write("/content/gdrive/MyDrive/Traffic_recognition/darknet/data/labels/" + filename)
                outfile.write("\n")
                outfile.close()
        print(choose_type + "txt file created successfully")


create_txt("/Colab Notebooks/YOLO Model Configuration/Data Preparation/data/train", "train")
create_txt("/Colab Notebooks/YOLO Model Configuration/Data Preparation/data/test", "test")


