from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Watermark Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=500, height=500)
canvas.grid(row=0, column=1)


def merge(im1, im2):
    w = im1.size[0]
    h = im1.size[1]
    if im2.size[0] >= w-100:
        w2 = int(w/im2.size[0] * im2.size[0] - 200)
        h2 = int(w2*im2.size[1]/im2.size[0])
        im2_r = im2.resize((w2, h2))
        print(im2_r.format, im2_r.size, im2_r.mode)
        im = Image.new("RGBA", (w, h))
        im.paste(im1)
        im.paste(im2_r, ((w - im2_r.size[0] - 50), (h - im2_r.size[1] - 50)))

    else:
        im = Image.new("RGBA", (w, h))
        im.paste(im1)
        im.paste(im2, ((w-im2.size[0]-50), (h - im2.size[1] - 50)))

    return im


def upload_image():
    img1 = askopenfilename()
    image_file = Image.open(img1)
    try:
        im2 = Image.open("logo.png")
    except:
        messagebox.showerror(title="Missing Logo!!!", message="Please select a logo.")
        upload_logo()
        im2 = Image.open("logo.png")

    img = merge(im1=image_file, im2=im2)
    arr = img1.split("/")
    filename = arr[len(arr)-1].split(".")[0]
    img.save(f"img/{filename}.png")
    window.after(2000)
    image = Image.open(f"img/{filename}.png")
    img_resized = image.resize((500, int(image.size[1]*500/image.size[0])))  # new width & height
    img_r = ImageTk.PhotoImage(img_resized)
    b2 = Label(window, image=img_r)  # using Button
    b2.grid(row=0, column=1)

def upload_logo():
    logo = askopenfilename()
    image_file = Image.open(logo)
    image_file.save("logo.png")
    window.after(2000)
    image = Image.open("logo.png")
    img_resized = image.resize((100, int(image.size[1]*100/image.size[0])))  # new width & height
    img_r = ImageTk.PhotoImage(img_resized)
    b2 = Label(window, image=img_r)  # using Button
    b2.grid(row=1, column=1)


gen_button = Button(text="Upload Image", command=upload_image)
gen_button.grid(row=3, column=2)
logo_button = Button(text="Upload Logo", command=upload_logo)
logo_button.grid(row=3, column=0)


window.mainloop()
