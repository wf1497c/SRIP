import zipfile

# with zipfile.ZipFile("leftImg8bit_trainvaltest.zip","r") as zip_ref:
#     zip_ref.extractall("./datasets/data/cityscapes/")

with zipfile.ZipFile("gtFine_trainvaltest.zip","r") as zip_ref:
    zip_ref.extractall("./datasets/data/cityscapes/")

with zipfile.ZipFile("leftImg8bit_blurred.zip","r") as zip_ref:
    zip_ref.extractall("./datasets/data/cityscapes/")