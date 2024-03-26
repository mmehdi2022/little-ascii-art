from PIL import Image as im
import cv2 as cv
import sys
import os
from colorama import Fore, init
import numpy as np

init(convert=True)


DENSITY = 'Ñ@W$9876543210?!abc;:+=-,._ '

BRIGHTNESS = {
" ": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
"_": [27, 28, 29, 30, 31, 32, 33, 34, 35],
".": [36, 37, 38, 39, 40, 41, 42, 43, 44],
",": [45, 46, 47, 48, 49, 50, 51, 52, 53],
"-": [54, 55, 56, 57, 58, 59, 60, 61, 62],
"=": [63, 64, 65, 66, 67, 68, 69, 70, 71],
"+": [72, 73, 74, 75, 76, 77, 78, 79, 80],
":": [81, 82, 83, 84, 85, 86, 87, 88, 89],
";": [90, 91, 92, 93, 94, 95, 96, 97, 98],
"c": [99, 100, 101, 102, 103, 104, 105, 106, 107],
"b": [108, 109, 110, 111, 112, 113, 114, 115, 116],
"a": [117, 118, 119, 120, 121, 122, 123, 124, 125],
"!": [126, 127, 128, 129, 130, 131, 132, 133, 134],
"?": [135, 136, 137, 138, 139, 140, 141, 142, 143],
"0": [144, 145, 146, 147, 148, 149, 150, 151],
"1": [152, 153, 154, 155, 156, 157, 158, 159],
"2": [160, 161, 162, 163, 164, 165, 166, 167],
"3": [168, 169, 170, 171, 172, 173, 174, 175],
"4": [176, 177, 178, 179, 180, 181, 182, 183],
"5": [184, 185, 186, 187, 188, 189, 190, 191],
"6": [192, 193, 194, 195, 196, 197, 198, 199],
"7": [200, 201, 202, 203, 204, 205, 206, 207],
"8": [208, 209, 210, 211, 212, 213, 214, 215],
"9": [216, 217, 218, 219, 220, 221, 222, 223],
"$": [224, 225, 226, 227, 228, 229, 230, 231],
"W": [232, 233, 234, 235, 236, 237, 238, 239],
"@": [240, 241, 242, 243, 244, 245, 246, 247],
"Ñ": [248, 249, 250, 251, 252, 253, 254, 255],
}

# def density_range(a, n):                                   to calculate brightness level of whatever you want
#     k, m = divmod(len(a), n)
#     return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

# d = list(density_range(list(range(256)), len(DENSITY)))
# for i,j in list(zip(reversed(DENSITY), d)):
#     print(f'"{i}": {j},')

# -------------------------------------------------------------------------------------------------------------------------------


def brightness_and_density(t):
    if type(t) == np.ndarray:
        brightness = (t[0] + t[1] + t[2]) / 3   # brightness level is the avrage of RGB
    else:
        brightness = t
    for key in BRIGHTNESS.keys():
        if int(brightness) in BRIGHTNESS[key]:
            return key
    raise SyntaxError


def get_pixel(image):
    image = im.fromarray(image)
    return np.asarray(tuple(image.getdata())), image.size
    

def main():
    vid = cv.VideoCapture(0)
    vid.set(3, 100)
    vid.set(4, 100)

    while True:
        frame = cv.flip(vid.read()[1], 1)
        pixels, size = get_pixel(frame)
        result = ''
        for i in range(size[0] * size[1]):
            if i % size[0] == 0:
                result += '\n'
            result += brightness_and_density(pixels[i])*2
        os.system('cls')
        print(result)
        if cv.waitKey(1) & 0XFF == ord('q'):
            break
    vid.release()



if __name__ == '__main__':
    main()


# crated by EDVARD
