import numpy as np
from scipy.ndimage import convolve

def solve(img, algo, enhancements):
    bin2dec = 2**np.arange(9).reshape(3,3)
    for _ in range(1, enhancements+1):
        img = algo[convolve(img, bin2dec)]
    return img.sum()

def Main():
    algo, _, *image = open("2021/day20/input.txt").read().splitlines()

    algo = np.array([int(p=="#") for p in algo])
    image = np.pad([[int(p=="#") for p in row]
                for row in image], (51,51), 
                mode='constant')

    print(f'Part 1: {solve(image, algo,  2)}\nPart 2: {solve(image, algo, 50)}')

if __name__ == '__main__':
    Main()