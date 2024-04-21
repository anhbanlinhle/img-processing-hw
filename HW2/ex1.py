import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
import os


def read_img(img_path):
    """
        Read grayscale image
        Inputs:
        img_path: str: image path
        Returns:
        img: cv2 image
    """
    return cv2.imread(img_path, 0)


def padding_img(img, filter_size=3):
    h, w = img.shape[:2]
    pad = filter_size // 2

    padded_img = np.zeros((h + 2 * pad, w + 2 * pad), dtype=img.dtype)

    padded_img[pad : pad + h, pad : pad + w] = img

    for i in range(pad):
        padded_img[i, pad : pad+w] = img[0, :]
        padded_img[-i-1, pad : pad+w] = img[-1, :]
    
    for i in range(pad):
        padded_img[pad : pad+h, i] = padded_img[pad : pad+h, pad]
        padded_img[pad : pad+h, -i-1] = padded_img[pad : pad+h, -pad-1]
    
    padded_img[:pad, :pad] = img[0, 0]
    padded_img[:pad, -pad:] = img[0, -1]
    padded_img[-pad:, :pad] = img[-1, 0]
    padded_img[-pad:, -pad:] = img[-1, -1]

    return padded_img

def mean_filter(img, filter_size=3):
    padded_img = padding_img(img=img, filter_size=filter_size)
    h, w = img.shape[:2]
    
    smoothed_img = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            neighborhood = padded_img[i : i+filter_size, j : j+filter_size]
            mean_value = np.mean(neighborhood)
            smoothed_img[i, j] = mean_value
    
    return smoothed_img

def median_filter(img, filter_size=3):
    padded_img = padding_img(img=img, filter_size=filter_size)
    h, w = img.shape[:2]
    
    smoothed_img = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            neighborhood = padded_img[i : i+filter_size, j : j+filter_size]
            median_value = np.median(neighborhood)
            smoothed_img[i, j] = median_value
    
    return smoothed_img


def psnr(gt_img, smooth_img):
    mse = np.mean((gt_img - smooth_img) ** 2)

    if mse == 0:
        return 100
    
    max_pixel = 255.0
    psnr = 10 * math.log10((max_pixel * max_pixel) / mse)
    return psnr



def show_res(before_img, after_img, img_name):
    """
        Show the original image and the corresponding smooth image
        Inputs:
            before_img: cv2: image before smoothing
            after_img: cv2: corresponding smoothed image
        Return:
            None
    """
    plt.figure(figsize=(12, 9))
    plt.subplot(1, 2, 1)
    plt.imshow(before_img, cmap='gray')
    plt.title('Before')

    plt.subplot(1, 2, 2)
    plt.imshow(after_img, cmap='gray')
    plt.title('After')
    plt.savefig(f'out/ex1/{img_name}.png')
    plt.show()


if __name__ == '__main__':
    img_noise = "img/noise.png" # <- need to specify the path to the noise image
    img_gt = "img/original.png" # <- need to specify the path to the gt image
    img = read_img(img_noise)
    filter_size = 3

    # Mean filter
    mean_smoothed_img = mean_filter(img, filter_size)
    show_res(img, mean_smoothed_img, "mean_smoothed")
    print('PSNR score of mean filter: ', psnr(img, mean_smoothed_img))

    # Median filter
    median_smoothed_img = median_filter(img, filter_size)
    show_res(img, median_smoothed_img, "median_smoothed")
    print('PSNR score of median filter: ', psnr(img, median_smoothed_img))

