from PIL import Image # import pillow library (can install with "pip install pillow")
im = Image.open("char_black.png")

w, h = im.size

r, c = 16, 16

s = int(w/16)

for i in range(r):
    for j in range(c):
        nm = im.crop( (j*s, i*s, (j+1)*s, (i+1)*s) ) # previously, image was 826 pixels wide, cropping to 825 pixels wide
        nm.save(f"{i*r + j}.png") # saves the image