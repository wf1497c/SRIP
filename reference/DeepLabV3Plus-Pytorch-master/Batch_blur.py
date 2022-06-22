import matplotlib.pyplot as plt
import cv2
import os

root = "./datasets/data/cityscapes/leftImg8bit/train"
for dirname in os.listdir(root):
    path = os.path.join(root,dirname)
    for filename in os.listdir(path):
        file = os.path.join(path,filename)
        img = plt.imread(file)
        img = cv2.GaussianBlur(img,(31,31),15,15)
        plt.imsave(file,img)