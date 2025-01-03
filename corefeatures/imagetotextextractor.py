from paddleocr import PaddleOCR, draw_ocr
import cv2
# Paddleocr supports Chinese, English, French, German, Korean and Japanese
# You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
# to switch the language model in order
ocr = PaddleOCR(use_angle_cls=False, lang='en') # need to run only once to download and load model into memory
pathtoSrcImg = '..\\static\\images\\propconceptview.png'
import os
# Get the directory of the current file
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Define the subfolder name
subfolder_name = 'static/images/propconceptview.png'
font_file_name='static/arial unicode.ttf'
print(parent_dir)
# Construct the full path to the subfolder
pathtoSrcImg = os.path.join(parent_dir, subfolder_name)
print(pathtoSrcImg)
if(os.path.isfile(pathtoSrcImg)==False):
    print('File does not exist')
    exit(0) 
# Print the subfolder path
print(pathtoSrcImg)

image = cv2.imread(pathtoSrcImg)
#Pil way of
#img_path = 'PaddleOCR/doc/imgs_en/img_12.jpg'
result = ocr.ocr(image, cls=False)
for idx in range(len(result)):
    res = result[idx]
    for line in res:
        print(line)
from PIL import Image, ImageDraw

# draw result
result = result[0]
image = Image.open(pathtoSrcImg).convert('RGB')
draw = ImageDraw.Draw(image)
draw.polygon(((100, 100), (200, 50), (125, 25)), fill="green")

   
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
font_path = os.path.join(parent_dir, font_file_name)

#for box in boxes:
    #draw.polygon((box[0],box[1]), fill="green")

im_show = draw_ocr(image, boxes, txts, scores,font_path=font_path)
#im_show = Image.fromarray(im_show)
cv2.imshow('Result', im_show)
cv2.waitKey(0) 
cv2.destroyAllWindows() 


