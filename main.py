from PIL import Image
import numpy as np
import cv2


def bw_convert():
    a = np.asarray(Image.open('Picture/Anime.jpg'), dtype='uint8')
    b = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums, 3).reshape(a.shape)
    Image.fromarray(k).save('Picture/res.png')
    img = cv2.imread("Picture/res.png")
    pic = Image.open("Picture/res.png")
    width, height = pic.size
    width = width * 1.7
    proportion = height / width
    wi = int((1 / proportion) * 250)
    hei = int(proportion * 250)
    print(wi, hei, width, height)
    res = cv2.resize(img, dsize=(wi, hei), interpolation=cv2.INTER_CUBIC)
    Image.fromarray(res).save('Picture/res.png')


def img_pix():
    img = Image.open("Picture/res.png")
    obj = img.load()
    pix, pix1, pix2 = obj[1, 1]
    width, height = img.size
    print(pix, width, height)


def text_generator():
    img = Image.open("Picture/res.png")
    obj = img.load()
    width, height = img.size
    i = 1
    j = 1
    with open('File/readme.txt', 'w') as f:
        while j < height:
            while i < width:
                pix, pix1, pix2 = obj[i, j]
                if pix >= 0 | pix <= 31:
                    f.write('@')
                elif pix >= 32 | pix <= 63:
                    f.write('%')
                elif pix >= 64 | pix <= 95:
                    f.write('$')
                elif pix >= 96 | pix <= 127:
                    f.write('0')
                elif pix >= 128 | pix <= 159:
                    f.write('<')
                elif pix >= 160 | pix <= 191:
                    f.write('+')
                elif pix >= 192 | pix <= 223:
                    f.write('=')
                elif pix >= 224 | pix <= 255:
                    f.write('-')
                i = i + 1
            i = 1
            j = j + 1
            f.write('\n')
    f.close()


if __name__ == '__main__':
    bw_convert()
    img_pix()
    text_generator()
