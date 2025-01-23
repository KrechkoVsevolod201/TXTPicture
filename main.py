from PIL import Image
import numpy as np
import cv2


def bw_convert():
    a = np.asarray(Image.open('Picture/But.jpg'), dtype='uint8')
    b = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums, 3).reshape(a.shape)
    Image.fromarray(k).save('Picture/res.png')
    img = cv2.imread("Picture/res.png")
    pic = Image.open("Picture/res.png")
    width, height = pic.size
    width = width * 1.7
    proportion = height / width
    wi = int((1 / proportion) * 150)
    hei = int(proportion * 150)
    print(wi, hei, width, height)
    res = cv2.resize(img, dsize=(wi, hei), interpolation=cv2.INTER_CUBIC)
    Image.fromarray(res).save('Picture/res.png')


def img_pix():
    img = Image.open("Picture/res.png")
    obj = img.load()
    pix, pix1, pix2 = obj[1, 1]
    width, height = img.size
    print(pix, width, height)
    with open('AsistFiles/FileWay.txt', 'r') as my_file:
        filename = my_file.read()
        filename1 = str(filename)
    my_file.close()
    print(filename)


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


def text_generator_one_bit():
    img = Image.open("Picture/res.png")
    obj = img.load()
    width, height = img.size
    i = 1
    j = 1
    with open('File/readme.txt', 'w') as f:
        while j < height:
            while i < width:
                pix, pix1, pix2 = obj[i, j]
                if (pix >= 0) and pix <= 31:
                    f.write('1 ')
                elif (pix >= 32) and pix <= 255:
                    f.write('0 ')
                print(i)
                i = i + 1
            i = 1
            j = j + 1
            f.write('\n')
    f.close()

def pixel_generator_one_bit():
    img = Image.open("Picture/res.png")
    obj = img.load()
    width, height = img.size

    # Создаем новое изображение с теми же размерами
    new_img = Image.new("L", (width, height))  # "L" - режим для черно-белого изображения
    new_obj = new_img.load()

    for j in range(height):
        for i in range(width):
            pix, pix1, pix2 = obj[i, j]
            if (pix >= 0) and (pix <= 50):
                new_obj[i, j] = 0  # Белый цвет
            elif (pix >= 32) and (pix <= 255):
                new_obj[i, j] = 255  # Черный цвет

    # Сохраняем новое изображение
    new_img.save('File/readme.jpg')


def gui_runner(filename):
    a = np.asarray(Image.open(filename), dtype='uint8')
    b = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums, 3).reshape(a.shape)
    Image.fromarray(k).save('Picture/res.png')
    img = cv2.imread("Picture/res.png")
    pic = Image.open("Picture/res.png")
    width, height = pic.size
    width = width * 1.7
    proportion = height / width
    wi = int((1 / proportion) * 150)
    hei = int(proportion * 150)
    print(wi, hei, width, height)
    res = cv2.resize(img, dsize=(wi, hei), interpolation=cv2.INTER_CUBIC)
    Image.fromarray(res).save('Picture/res.png')
    text_generator()


def gui_runner_2(filename):
    a = np.asarray(Image.open(filename), dtype='uint8')
    b = np.array([[[0.2989, 0.587, 0.114]]])
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums, 3).reshape(a.shape)
    Image.fromarray(k).save('Picture/res.png')
    img = cv2.imread("Picture/res.png")
    pic = Image.open("Picture/res.png")
    width, height = pic.size
    width = width * 1.7
    proportion = height / width
    wi = int((proportion) * 200)
    hei = int(proportion * 200)
    print(wi, hei, width, height)
    res = cv2.resize(img, dsize=(wi, hei), interpolation=cv2.INTER_CUBIC)
    Image.fromarray(res).save('Picture/res.png')
    text_generator()


def gui_runner_3(filename):
    # Открываем изображение и преобразуем его в массив
    a = np.asarray(Image.open(filename), dtype='uint8')

    # Проверяем, есть ли альфа-канал, и если есть, то берем только первые три канала
    if a.shape[2] == 4:
        a = a[:, :, :3]  # Убираем альфа-канал

    # Определяем коэффициенты для преобразования в оттенки серого
    b = np.array([[[0.2989, 0.587, 0.114]]])

    # Применяем преобразование
    sums = np.round(np.sum(a * b, axis=2)).astype(np.uint8)
    k = np.repeat(sums[:, :, np.newaxis], 3, axis=2)  # Повторяем для трех каналов

    # Сохраняем результат
    Image.fromarray(k).save('Picture/res.png')

    # Читаем изображение без изменения размера
    img = cv2.imread("Picture/res.png")

    # Сохраняем изображение без изменения размера
    Image.fromarray(img).save('Picture/res.png')

    pixel_generator_one_bit()


if __name__ == '__main__':
    gui_runner_3("Picture/space.png")