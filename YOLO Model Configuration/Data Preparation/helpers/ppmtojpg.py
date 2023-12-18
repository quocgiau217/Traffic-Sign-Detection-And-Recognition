import os
from PIL import Image

def ppm_to_jpg(input_path, output_path):
    try:
        img = Image.open(input_path)
        img.save(output_path, "JPEG")
        print(f"Conversion successful for {input_path}")
    except Exception as e:
        print(f"Error converting {input_path}: {e}")

def batch_convert_ppm_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ppm_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.ppm')]

    for ppm_file in ppm_files:
        ppm_path = os.path.join(input_folder, ppm_file)
        jpg_file = os.path.splitext(ppm_file)[0] + '.jpg'
        jpg_path = os.path.join(output_folder, jpg_file)
        ppm_to_jpg(ppm_path, jpg_path)

# Đường dẫn đến thư mục chứa các file .ppm và thư mục muốn lưu file .jpg
input_ppm_folder = "F:\Traffic-Sign-Detection-And-Recognition\FullJCNN2013"
output_jpg_folder = "F:\Traffic-Sign-Detection-And-Recognition\FullJCNN2013_jpg"

batch_convert_ppm_to_jpg(input_ppm_folder, output_jpg_folder)
