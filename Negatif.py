import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

# Path untuk gambar asli dan gambar negatif
path_asli = "C:\\Users\\Abdul\\OneDrive\\Documents\\TUGAS AMI\\PCD\\obama-lamar.jpeg"
path_negatif = "C:\\Users\\Abdul\\OneDrive\\Documents\\TUGAS AMI\\PCD\\obama-lamar-negatif.jpeg"

# Membaca gambar asli
image = img.imread(path_asli)

# Membuat gambar negatif
image_neg = 255 - image

# Menyimpan gambar negatif dengan nama yang berbeda untuk mencegah menimpa gambar asli
img.imwrite(path_negatif, image_neg)

# Membaca gambar negatif kembali untuk analisis histogram
image_neg = img.imread(path_negatif)

# Ekstraksi komponen warna merah (Red) dari gambar asli dan gambar negatif
r_image_asli = image[:, :, 0]
r_image_neg = image_neg[:, :, 0]

# Membuat histogram dari komponen warna merah gambar asli
hist_r_asli, bins_r_asli = np.histogram(r_image_asli.flatten(), bins=256, range=[0, 256])

# Membuat histogram dari komponen warna merah gambar negatif
hist_r_neg, bins_r_neg = np.histogram(r_image_neg.flatten(), bins=256, range=[0, 256])

# Membuat figure dengan 4 subplot untuk gambar dan histogram
plt.figure(figsize=(14, 10))

# Subplot 1: Menampilkan gambar asli
plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Gambar Asli")
plt.axis('off')  # Menghilangkan sumbu pada gambar

# Subplot 2: Menampilkan gambar negatif
plt.subplot(2, 2, 2)
plt.imshow(image_neg)
plt.title("Gambar Negatif")
plt.axis('off')  # Menghilangkan sumbu pada gambar

# Subplot 3: Histogram komponen warna merah dari gambar asli
plt.subplot(2, 2, 3)
plt.plot(hist_r_asli, color="red", label="Histogram R - Gambar Asli")
plt.title("Histogram Komponen Warna Merah - Gambar Asli")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.legend()

# Subplot 4: Histogram komponen warna merah dari gambar negatif
plt.subplot(2, 2, 4)
plt.plot(hist_r_neg, color="blue", label="Histogram R - Gambar Negatif")
plt.title("Histogram Komponen Warna Merah - Gambar Negatif")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.legend()

# Mengatur layout agar lebih rapi
plt.tight_layout()
plt.show()
