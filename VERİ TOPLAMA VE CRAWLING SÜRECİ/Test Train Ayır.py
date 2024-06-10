import os
import random
import shutil

# Kaynak ve hedef klasör yollarını belirleyin
source_folder = "C:\\Users\\elifo\\Desktop\\MAKİNE ÖĞRENMESİNE GİRİŞ\\Sulak Zemin_Son"
train_folder = "C:\\Users\\elifo\\Desktop\\MAKİNE ÖĞRENMESİNE GİRİŞ\\Sulak Zemin_TRAIN"
test_folder = "C:\\Users\\elifo\\Desktop\\MAKİNE ÖĞRENMESİNE GİRİŞ\\Sulak Zemin_TEST"
# Eğitim ve test klasörlerini oluşturun
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Dosya uzantılarını belirleyin
valid_extensions = ('.png', '.jpg', '.jpeg')

# Kaynak klasördeki geçerli dosyaları alın
files = [file for file in os.listdir(source_folder) if file.endswith(valid_extensions)]
random.shuffle(files)  # Dosyaları karıştır

# Test ve eğitim için kullanılacak dosyaların yüzdesini belirleyin
test_percentage = 0.2

# Toplam dosya sayısını ve test için gereken dosya sayısını hesaplayın
total_files = len(files)
test_size = int(total_files * test_percentage)

# Test ve eğitim dosyalarını ayırarak taşıyın
for i, file_name in enumerate(files):
    source_file_path = os.path.join(source_folder, file_name)
    if i < test_size:
        destination_folder = test_folder
    else:
        destination_folder = train_folder
    destination_file_path = os.path.join(destination_folder, file_name)
    shutil.move(source_file_path, destination_file_path)

print("Veri seti eğitim ve test kümelerine başarıyla taşındı.")


