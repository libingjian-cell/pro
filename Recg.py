from paddleocr import PaddleOCR
ocr = PaddleOCR(det_model_dir='models/li_det_infer',use_gpu=False) # need to run only once to download and load model into memory
img_path = 'imgs/01.jpg'
result = ocr.ocr(img_path, det=False)
for line in result:
    print(line)