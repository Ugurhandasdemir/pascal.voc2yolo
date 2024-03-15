import os
import shutil

# Etiketsiz görüntülerin taşınacağı dizin
unlabel_dir = "C:/Users/UGURHANDASDEMIR/Desktop/unlabel"

# Görüntülerin bulunduğu dizin
image_dir = "C:/Users/UGURHANDASDEMIR/Desktop/yolov888/train/images"

# Etiketlerin bulunduğu dizin
label_dir = "C:/Users/UGURHANDASDEMIR/Desktop/yolov888/train/labels"

# Görüntü dosyalarının uzantısı
image_ext = '.jpg'

# Etiket dosyalarının uzantısı
label_ext = '.txt'

# Dizinlerdeki dosyaları listele
image_files = os.listdir(image_dir)
label_files = os.listdir(label_dir)

# Her bir görüntü dosyası için kontrol et
for file in image_files:
    if file.endswith(image_ext):
        # Etiket dosyasının adını oluştur
        label_file = file.replace(image_ext, label_ext)

        # Eğer etiket dosyası yoksa
        if label_file not in label_files:
            # Görüntü dosyasını unlabeled_dir dizinine taşı
            shutil.move(os.path.join(image_dir, file), os.path.join(unlabel_dir, file))
            print(f'Etiketsiz dosya taşındı: {file}')
