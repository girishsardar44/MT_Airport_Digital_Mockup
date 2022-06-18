from tkinter import Image
import cv2
import pytesseract
import numpy as np
import pandas as pd
from PIL import Image
img= Image.open('coruna.png').convert('L')
ret,img = cv2.threshold(np.array(img),125,255, cv2.THRESH_BINARY)
img = Image.fromarray(img.astype(np.uint8))
text = pytesseract.image_to_data(img, config='--psm 6', output_type= 'data.frame')
print(text)
text = pd.DataFrame(text)
# print(text)
# text = text.split('\n')
with open('out.csv','w') as f:
    print(text,file=f)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
