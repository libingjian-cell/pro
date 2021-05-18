import os

from paddleocr import PaddleOCR, draw_ocr

# 模型路径下必须含有model和params文件
ocr = PaddleOCR(det_model_dir='models/li_det_infer', use_gpu=False)
dir_path="D:/iiiiii/img_50/"
dir_path2="D:/result02/"
files = os.listdir(dir_path)
print(files)
for file in files :
    img_path = dir_path+str(file)
    result = ocr.ocr(img_path, rec=False)
    fo = open(dir_path2+str(file)[:-4]+".txt", "w")
    for line in result:
        fo.write(str(line) + "\n")
    fo.close()
from PIL import Image
image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
im_show = draw_ocr(image,  result,txts=None, scores=None,font_path='D:/paddle_pp/PaddleOCR/doc/simfang.ttf')
im_show = Image.fromarray(im_show)
