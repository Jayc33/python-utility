import cv2
import os

path = "MARTIAL PEAK CHAPTER 2321-2325 MT"

files = []
if os.path.isdir(path):
    for file in os.listdir(path):
        if not file.endswith('.ini') and os.path.isfile(os.path.join(path, file)) :
            files.append(file)

images = []
for filename in files[0:10]:
    img = cv2.imread(path + "/" + filename)
    images.append(img)
    
print(files)

stitcher = cv2.Stitcher_create()

status, result = stitcher.stitch(images)
print(status)

cv2.imwrite(f'{path}.png', result)
