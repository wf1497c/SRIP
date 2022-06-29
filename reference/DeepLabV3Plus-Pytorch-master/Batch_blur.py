import matplotlib.pyplot as plt
import skimage
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
            img = skimage.filters.gaussian(img, sigma=(5, 5), multichannel=False)
            plt.imsave(file,img)