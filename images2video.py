import cv2
import numpy as np
import glob
import os, fnmatch


### Find dog frames in a directory
def find(pattern, path):
    results = []
    names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                results.append(os.path.join(root, name))
                names.append(name)
    return results, names


pattern = '*'
directory = '/home/am_zam/tokenflow/input/'
image_addresses, image_names = find(pattern, directory)

image_addresses.sort()
image_names.sort()

img_array = []


for i, image_address in enumerate(image_addresses):
    img = cv2.imread(image_address)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

height, width, layers = img_array[0].shape
size = (width,height)
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
