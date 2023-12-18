import os
import random
import shutil

# Đường dẫn đến thư mục gốc chứa ảnh và nhãn
source_dir = "F:\\Traffic-Sign-Detection-And-Recognition\\ts"

# Đường dẫn đến thư mục chứa tập train, valid, và test
output_dir = "F:\Traffic-Sign-Detection-And-Recognition\data"

# Tỉ lệ phần trăm cho tập train, valid, và test
train_percent = 0.7
valid_percent = 0.15
test_percent = 0.15
# Tạo thư mục train, valid, và test
os.makedirs(os.path.join(output_dir, "train", "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "valid", "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "test", "images"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "train", "labels"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "valid", "labels"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "test", "labels"), exist_ok=True)

# Lấy danh sách tất cả các tệp ảnh trong thư mục gốc
image_files = [f for f in os.listdir(source_dir) if f.endswith(".jpg")]

# Lấy số lượng ảnh cho mỗi tập dựa trên tỉ lệ phần trăm
num_images = len(image_files)
num_train = int(num_images * train_percent)
num_valid = int(num_images * valid_percent)
num_test = num_images - num_train - num_valid

# Xáo trộn danh sách các tệp ảnh
random.shuffle(image_files)

# Chia ảnh và nhãn vào từng tập
for i, image_file in enumerate(image_files):
    source_image_path = os.path.join(source_dir, image_file)
    source_label_path = os.path.join(source_dir, image_file.replace(".jpg", ".txt"))

    if i < num_train:
        target_dir = os.path.join(output_dir, "train")
    elif i < num_train + num_valid:
        target_dir = os.path.join(output_dir, "valid")
    else:
        target_dir = os.path.join(output_dir, "test")

    target_image_path = os.path.join(target_dir, "images", image_file)
    target_label_path = os.path.join(target_dir, "labels", image_file.replace(".jpg", ".txt"))

    # Di chuyển tệp ảnh và nhãn đến thư mục tương ứng
    shutil.copy(source_image_path, target_image_path)
    shutil.copy(source_label_path, target_label_path)
