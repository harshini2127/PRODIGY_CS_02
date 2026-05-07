from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox


# Function to process image using XOR encryption/decryption
def process_image(image_path, key, output_path, mode):

    try:
        # Open image
        img = Image.open(image_path)

    except FileNotFoundError:
        messagebox.showerror("Error", "Image file not found!")
        return

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    # Convert image to RGBA
    img = img.convert("RGBA")

    # Validate key range
    if key < 0 or key > 255:
        messagebox.showerror("Error", "Key must be between 0 and 255")
        return

    width, height = img.size

    #ENCRYPTIION
    if mode == "encrypt":

        # Store key inside first reserved pixel
        img.putpixel((0, 0), (key, key, key, 255))

        # Loop through all pixels
        for x in range(width):
            for y in range(height):

                # Skip reserved pixel
                if x == 0 and y == 0:
                    continue

                pixel = img.getpixel((x, y))

                r, g, b, a = pixel

                # Apply XOR encryption
                encrypted_pixel = (
                    r ^ key,
                    g ^ key,
                    b ^ key,
                    a
                )

                # Replace original pixel
                img.putpixel((x, y), encrypted_pixel)

        # Save encrypted image
        img.save(output_path)

        messagebox.showinfo(
            "Success",
            f"Image encrypted successfully!\nSaved as:\n{output_path}"
        )

    #DECRYPTION 
    elif mode == "decrypt":

        # Read stored key from first pixel
        stored_pixel = img.getpixel((0, 0))

        stored_key = stored_pixel[0]

        # Verify key
        if key != stored_key:
            messagebox.showerror(
                "Error",
                "Wrong decryption key!"
            )
            return

        # Loop through all pixels
        for x in range(width):
            for y in range(height):

                # Skip reserved pixel
                if x == 0 and y == 0:
                    continue

                pixel = img.getpixel((x, y))

                r, g, b, a = pixel

                # Apply XOR decryption
                decrypted_pixel = (
                    r ^ key,
                    g ^ key,
                    b ^ key,
                    a
                )

                # Replace encrypted pixel
                img.putpixel((x, y), decrypted_pixel)

        # Restore reserved pixel
        img.putpixel((0, 0), (0, 0, 0, 255))

        # Save decrypted image
        img.save(output_path)

        messagebox.showinfo(
            "Success",
            f"Image decrypted successfully!\nSaved as:\n{output_path}"
        )


# Browse image function
def browse_image():

    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")
        ]
    )

    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_path)


# Encrypt image function
def encrypt_image():

    image_path = image_entry.get().strip().strip('"').strip("'")

    try:
        key = int(key_entry.get())

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid numeric key!"
        )
        return

    # Ask save location
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save Encrypted Image As"
    )

    if not save_path:
        return

    process_image(image_path, key, save_path, "encrypt")


# Decrypt image function
def decrypt_image():

    image_path = image_entry.get().strip().strip('"').strip("'")

    try:
        key = int(key_entry.get())

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid numeric key!"
        )
        return

    # Ask save location
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save Decrypted Image As"
    )

    if not save_path:
        return

    process_image(image_path, key, save_path, "decrypt")


# GUI WINDOW

root = tk.Tk()
root.title("Image Encryption Tool")

root.state("zoomed")

root.resizable(False, False)

root.configure(bg="lightgrey")

# HEADING 

heading = tk.Label(
    root,
    text="Image Encryption & Decryption Tool",
    font=("Arial", 25, "bold"),
    bg="lightblue",
    fg="black"
)

heading.pack(pady=50)

# IMAGE FRAME 

image_frame = tk.Frame(
    root,
    bg="lightgrey"
)

image_frame.pack(pady=15)

# Image label
image_label = tk.Label(
    image_frame,
    text="Select Image:",
    font=("Arial", 12, "bold"),
    bg="lightgrey",
    fg="black"
)

image_label.pack(side="left", padx=20)

# Image entry
image_entry = tk.Entry(
    image_frame,
    width=60,
    font=("Arial", 12)
)

image_entry.pack(side="left", padx=10)

# BROWSE BUTTON

browse_button = tk.Button(
    root,
    text="Browse Image",
    command=browse_image,
    bg="yellow",
    fg="black",
    font=("Arial", 11, "bold"),
    width=20,
    height=1
)

browse_button.pack(pady=20)

# KEY FRAME 

key_frame = tk.Frame(
    root,
    bg="lightgrey"
)

key_frame.pack(pady=40)

# Key label
key_label = tk.Label(
    key_frame,
    text="Enter XOR Key (0-255):",
    font=("Arial", 12, "bold"),
    bg="lightgrey",
    fg="black"
)

key_label.pack(side="left", padx=20)

# Key entry
key_entry = tk.Entry(
    key_frame,
    width=20,
    font=("Arial", 12)
)

key_entry.pack(side="left", padx=10)

# BUTTON FRAME

button_frame = tk.Frame(
    root,
    bg="lightgrey"
)

button_frame.pack(pady=40)

#ENCRYPT BUTTON 

encrypt_button = tk.Button(
    button_frame,
    text="Encrypt Image",
    command=encrypt_image,
    bg="orange",
    fg="black",
    font=("Arial", 15, "bold"),
    width=20,
    height=2
)

encrypt_button.pack(side="left", padx=20)

#DECRYPT BUTTON 

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt Image",
    command=decrypt_image,
    bg="lightgreen",
    fg="black",
    font=("Arial", 15, "bold"),
    width=20,
    height=2
)

decrypt_button.pack(side="left", padx=20)

root.mainloop()