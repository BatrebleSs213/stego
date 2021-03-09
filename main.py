# pip3 install -r requirements.txt
import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
from PIL import Image
import cv2


def check_lsb_channel(input_im, channel):
    output_im = np.copy(input_im)
    for x in range(0, input_im.shape[0]):
        for y in range(0, input_im.shape[1]):
            r = input_im[x,y][0]
            g = input_im[x,y][1]
            b = input_im[x,y][2]

            rgb = (r, g, b)
      
            binary = '{0:b}'.format(rgb[channel])
            if(list(str(binary))[-1] == '1'):
                output_im[x,y] = (0, 0, 0)

    return output_im


if __name__ == '__main__':
    image_name = "test1"
    image = img.imread("images/" + image_name + ".jpg")
    image_check = np.copy(image)
    image[0, 0]
    image_check_r = check_lsb_channel(image, 0)
    image_check_g = check_lsb_channel(image, 1)
    image_check_b = check_lsb_channel(image, 2)

    concate = np.concatenate((image, image_check_r, image_check_g, image_check_b), axis = 1)
    plt.figure(figsize = (12,4))
    plt.imshow(concate)
    plt.show()
