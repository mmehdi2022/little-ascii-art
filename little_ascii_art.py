from PIL import Image as im
import cv2 as c
import sys
import os
from colorama import Fore, init


init(convert=True)


DENSITY = 'Ñ@W$9876543210?!abc;:+=-,._ '

BRIGHTNESS = {
    " ": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "_": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],     
    ".": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],     
    ",": [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],     
    "-": [40, 41, 42, 43, 44, 45, 46, 47, 48],
    "=": [49, 50, 51, 52, 53, 54, 55, 56, 57],
    "+": [58, 59, 60, 61, 62, 63, 64, 65, 66],
    ":": [67, 68, 69, 70, 71, 72, 73, 74, 75],
    ";": [76, 77, 78, 79, 80, 81, 82, 83, 84],
    "c": [85, 86, 87, 88, 89, 90, 91, 92, 93],
    "b": [94, 95, 96, 97, 98, 99, 100, 101, 102],      
    "a": [103, 104, 105, 106, 107, 108, 109, 110, 111],
    "!": [112, 113, 114, 115, 116, 117, 118, 119, 120],
    "?": [121, 122, 123, 124, 125, 126, 127, 128, 129],
    "0": [130, 131, 132, 133, 134, 135, 136, 137, 138],
    "1": [139, 140, 141, 142, 143, 144, 145, 146, 147],
    "2": [148, 149, 150, 151, 152, 153, 154, 155, 156],
    "3": [157, 158, 159, 160, 161, 162, 163, 164, 165],
    "4": [166, 167, 168, 169, 170, 171, 172, 173, 174],
    "5": [175, 176, 177, 178, 179, 180, 181, 182, 183],
    "6": [184, 185, 186, 187, 188, 189, 190, 191, 192],
    "7": [193, 194, 195, 196, 197, 198, 199, 200, 201],
    "8": [202, 203, 204, 205, 206, 207, 208, 209, 210],
    "9": [211, 212, 213, 214, 215, 216, 217, 218, 219],
    "$": [220, 221, 222, 223, 224, 225, 226, 227, 228],
    "W": [229, 230, 231, 232, 233, 234, 235, 236, 237],
    "@": [238, 239, 240, 241, 242, 243, 244, 245, 246],
    "Ñ": [247, 248, 249, 250, 251, 252, 253, 254, 255],
}

# def density_range(a, n):                                   to calculate brightness level of whatever you want
#     k, m = divmod(len(a), n)
#     return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

# d = list(density_range(list(range(256)), len(DENSITY)))
# for i,j in list(zip(reversed(DENSITY), d)):
#     print(f'"{i}": {j},')

# -------------------------------------------------------------------------------------------------------------------------------

def brightness_and_density(t):
    if type(t) == tuple:
        brightness = (t[0] + t[1] + t[2]) / 3   # brightness level is the avrage of RGB
    else:
        brightness = t
    for key in BRIGHTNESS.keys():
        if int(brightness) in BRIGHTNESS[key]:
            return key
    raise SyntaxError


def change_size(path:str, size:tuple=(50, 50)):
    image = c.imread(path)
    new_image = c.resize(image, size)
    if '.png' in path:
        path = path.replace('.png', '') + f'-{size}.png'
    elif '.jpg' in path:
        path = path.replace('.jpg', '') + f'-{size}.jpg'
    elif '.jpeg' in path:
        path = path.replace('.jpeg', '') + f'-{size}.jpeg'
    c.imwrite(path, new_image)
    return path


def get_pixel(path:str):
    image = im.open(path, 'r')
    return tuple(image.getdata()), image.size
    

def main():
    if len(sys.argv) < 2 and len(sys.argv) > 3:
        print(f'{Fore.RED}[*]{Fore.RESET} Input format is <file name> <size:50x50 -> optional>')
    path = sys.argv[1]
    try:
        size = tuple(map(int, sys.argv[2].split('x')))
    except:
        size = None
    if size:
        path = change_size(path=path, size=size)
    pixels, size = get_pixel(path)
    result = ''
    for i in range(size[0] * size[1]):
        if i % size[0] == 0:
            result += '\n'
        result += brightness_and_density(pixels[i])*2   # to make the result wider
    os.system("cls")
    print(result)


if __name__ == '__main__':
    main()


# crated by EDVARD
