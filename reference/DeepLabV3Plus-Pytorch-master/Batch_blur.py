import matplotlib.pyplot as plt
import cv2
import os

root = "./datasets/data/cityscapes/leftImg8bit"
num = os.listdir(root)
for dir in os.listdir(root):
    path1 = os.path.join(root,dir)
    for dirname in os.listdir(path1):
        path = os.path.join(path1,dirname)
        for filename in os.listdir(path):
            file = os.path.join(path,filename)
            img = plt.imread(file)
            img = cv2.GaussianBlur(img,(31,31),15,15)
            plt.imsave(file,img)