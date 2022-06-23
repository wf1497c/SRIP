import zipfile
import os

if(os.path.isfile("leftImg8bit_trainvaltest.zip")):
    with zipfile.ZipFile("leftImg8bit_trainvaltest.zip","r") as zip_ref:
        zip_ref.extractall("./datasets/data/cityscapes/")

if(os.path.isfile("gtFine_trainvaltest.zip")):
    with zipfile.ZipFile("gtFine_trainvaltest.zip","r") as zip_ref:
        zip_ref.extractall("./datasets/data/cityscapes/")

if(os.path.isfile("leftImg8bit_blurred.zip")):
    with zipfile.ZipFile("leftImg8bit_blurred.zip","r") as zip_ref:
        zip_ref.extractall("./datasets/data/cityscapes/")