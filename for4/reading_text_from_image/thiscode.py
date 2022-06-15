from cv2 import imread
from pytesseract import pytesseract, image_to_string

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path = 'testimage.png'
img = imread(img_path)
print(type(img))

extracted_data = image_to_string(img)
print(extracted_data.strip())