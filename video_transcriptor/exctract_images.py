import cv2
import time
import pafy
import os

sec_to_skip = 32
URL = 'https://www.youtube.com/watch?v=trChro3guIE'

video = pafy.new(URL)
length = video.length
title = video.title

best = video.getbest()

try:
    os.mkdir(title)
except:
    print("directory already exists")  

cap = cv2.VideoCapture(best.url)
ct = 0
while ct/30 <= length:
    ret,frame = cap.read()
    print(ret)
    if ret:
        cv2.imwrite(f'{title}/{ct/30}.png', frame)
        ct += 30 * sec_to_skip
        cap.set(1, ct)
        cv2.waitKey(1)
    else :
        break
    time.sleep(1)

cap.release()
cv2.destroyAllWindows()