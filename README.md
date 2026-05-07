# PRODIGY_CS_02
Pixel manipulation for image encryption

# 🔐 Image Encryption & Decryption Tool using XOR Cipher

# 📌 Project Overview

This project is a GUI-based Image Encryption & Decryption Tool developed using Python, Tkinter, and Pillow (PIL). The application encrypts and decrypts images using XOR (Exclusive OR) pixel manipulation techniques.

The tool allows users to:
* Select an image from the system
* Encrypt the image using a user-defined XOR key
* Decrypt the encrypted image using the same key
* Save encrypted/decrypted images at a preferred location

The application supports multiple image formats including PNG, JPG, JPEG, BMP, and WEBP.

# 🚀 Features

✅ GUI-based desktop application using Tkinter

✅ XOR-based image encryption and decryption

✅ User-defined encryption key (0–255)

✅ Multiple image format support

✅ Fullscreen responsive GUI

✅ File browser for image selection

✅ Save encrypted/decrypted image anywhere in the system

✅ Wrong key detection during decryption

✅ Embedded key verification using reserved image pixel

✅ Error handling for invalid inputs and image paths

# 🔧 Techniques Used
* XOR Cipher Encryption
* Pixel Manipulation
* Image Processing using Pillow (PIL)
* GUI Development using Tkinter
* Embedded Key Verification
* Basic Steganographic Key Embedding
* RGBA Image Processing
* Error Handling & Input Validation

# 🧠 Explanation of Techniques
## 🔹 XOR Cipher Encryption

Used XOR operation to encrypt and decrypt image pixel values.

For encryption:

EncryptedPixel=Pixel⊕Key

For decryption:

(Pixel⊕Key)⊕Key=Pixel

The same XOR key must be used for successful decryption.

## 🔹 Pixel Manipulation

Accessed and modified RGB pixel values directly using:

getpixel()
putpixel()

## 🔹 Embedded Key Verification

The encryption key is embedded inside a reserved image pixel (0,0) during encryption.
During decryption, the application reads the stored key and verifies it before decrypting the image.

## 🔹 Basic Steganographic Key Embedding

The project incorporates a basic steganographic concept by embedding verification data inside image pixels.

## 🔹 RGBA Image Processing

All images are converted to RGBA format for consistent pixel handling across multiple image types.

## 🔹 Error Handling & Validation

Implemented exception handling and input validation to improve stability and user experience.

# 🛠️ Technologies Used
Python

Tkinter

Pillow (PIL)
# 📂 Supported Image Formats
PNG

JPG

JPEG

BMP

WEBP

Note: PNG format is recommended for encrypted images because it preserves exact pixel values without compression loss.

# 🧠 How the Project Works
## 🔐 Encryption Process
* User selects an image.
* User enters an XOR key between 0 and 255.
* The image is converted into RGBA format.
* The encryption key is stored inside the first reserved pixel (0,0).
* Remaining image pixels are encrypted using XOR operation.
* User selects a location to save the encrypted image.
## 🔓 Decryption Process
* User selects the encrypted image.
* User enters the XOR key.
* The application reads the stored key from the reserved pixel.
* If the entered key matches the stored key:
* image is decrypted successfully
* Otherwise:decryption is blocked with an error message
* User selects location to save the decrypted image.
# ▶️ How to Run the Project
## 1️⃣ Install Required Library
pip install pillow
## 2️⃣ Run the Program
python task2.py
# 📸 Screenshots
* GUI Interface
<img width="1920" height="1080" alt="gui" src="https://github.com/user-attachments/assets/cb6522c2-6373-4ea6-bf5d-5280fa6fe561" />

* Encrypted Image
<img width="1920" height="1080" alt="encrypted_image" src="https://github.com/user-attachments/assets/7dffd73c-557f-45dc-9f47-d3d067db841e" />

* Decrypted Image
<img width="1920" height="1080" alt="decrypted_image" src="https://github.com/user-attachments/assets/e000aea8-3466-4e04-9a9a-55592287d325" />


# ⚠️ Limitations
* XOR encryption is intended for educational purposes and is not military-grade encryption.
* If encrypted images are heavily modified or compressed, decryption may fail.
* PNG format is preferred for accurate pixel preservation.
* Current verification checks embedded key validity but not full image integrity.

# 🔮 Future Improvements
* Implement SHA-256 hash-based integrity verification
* Add drag-and-drop image upload
* Improve GUI design and themes
* Add image preview functionality
* support batch image encryption
* Implement advanced encryption algorithms like AES
* Add dark mode interface

# 👩‍💻 Author
Harshini Yekkaladevi
