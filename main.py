from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os


def open_output_folder():
    folder_path = r"C:\Users\HUAWEI\Pictures\Watermarked Images"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    os.system(f'explorer "{folder_path}"')


def create_watermark_img(inputImg, outputImg, watermarkImage, position):
    baseImg = Image.open(inputImg)
    watermark = Image.open(watermarkImage)
    baseImg.paste(watermark, position, mask=watermark)
    baseImg.save(outputImg)

    return baseImg

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        original_entry.delete(0, tk.END)
        original_entry.insert(0, file_path)

def select_watermark():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        watermark_entry.delete(0, tk.END)
        watermark_entry.insert(0, file_path)



def show_preview(modified_img_path):
    modified_image = Image.open(modified_img_path)
    modified_image.thumbnail((300, 300))
    modified_image = ImageTk.PhotoImage(modified_image)

    preview_label.config(image=modified_image)
    preview_label.image = modified_image


def apply_watermark():
    original_img = original_entry.get()
    file_name = original_img.split('/')[-1].split('.jpg')[0]

    watermark_img = watermark_entry.get()
    if original_img and watermark_img:
        output_img = fr"C:\Users\HUAWEI\Pictures\Watermarked Images\{file_name} watermarked.jpg"
        create_watermark_img(original_img, output_img, watermark_img, position=(0, 0))
        output_label.config(text="Watermark applied successfully!", fg='green')
        show_preview(output_img)


root = tk.Tk()
root.title('Image Watermarking')
root.geometry("1000x800")
root.resizable(False, False)


icon_path = r'C:\Users\HUAWEI\PycharmProjects\Image_Watermark\app_icon.png'
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(True, icon_photo)

frame_left = tk.Frame(root)
frame_left.place(relx=0.1, rely=0.5, anchor="w")

original_label = tk.Label(frame_left, text="Select original image:")
original_label.pack(pady=(10, 5), anchor="w")

original_entry = tk.Entry(frame_left, width=50)
original_entry.pack(pady=5, anchor="w")

original_button = tk.Button(frame_left, text="Browse", command=select_image)
original_button.pack(pady=5, anchor="w")

watermark_label = tk.Label(frame_left, text="Select watermark image:")
watermark_label.pack(pady=(10, 5), anchor="w")

watermark_entry = tk.Entry(frame_left, width=50)
watermark_entry.pack(pady=5, anchor="w")

watermark_button = tk.Button(frame_left, text="Browse", command=select_watermark)
watermark_button.pack(pady=5, anchor="w")

apply_button = tk.Button(frame_left, text="Apply Watermark", command=apply_watermark)
apply_button.pack(pady=10, anchor="w")

output_label = tk.Label(frame_left, text="")
output_label.pack(pady=5, anchor="w")

canvas = tk.Canvas(root, width=1, height=600, bg="grey")
canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.01, relheight=0.9)
canvas.create_line(0, 0, 0, 600, fill="white")

frame_right = tk.Frame(root)
frame_right.place(relx=0.9, rely=0.5, anchor="e")

preview_label = tk.Label(frame_right)
preview_label.pack(pady=10, fill="both", expand=True)

root.mainloop()
