from ultralytics import YOLO
from pathlib import Path
import os
import cv2 as cv
import numpy as np

def inferance_model():
    #model = YOLO('/Users/arthurlamard/Documents/ISEN5/reco_formes/best.pt')
    model = YOLO('/Users/arthurlamard/Documents/ISEN5/reco_formes/runs/segment/yolov8n_seg_custom3/weights/best.pt')


    img= '/Users/arthurlamard/Desktop/isen.png'

    results = model.predict(img, save=True, imgsz=640, save_crop=False)

    saving_path = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(saving_path):
        os.makedirs(saving_path)
    print(saving_path)

    # iterate detection results
    for r in results:
        print(r)
        img = np.copy(r.orig_img)
        img_name = Path(r.path).stem

        # iterate each object contour
        for ci, c in enumerate(r):
            label = c.names[c.boxes.cls.tolist().pop()]

            b_mask = np.zeros(img.shape[:2], np.uint8)

            # Create contour mask
            contour = c.masks.xy.pop().astype(np.int32).reshape(-1, 1, 2)
            _ = cv.drawContours(b_mask, [contour], -1, (255, 255, 255), cv.FILLED)

            isolated = np.dstack([img, b_mask])



            cv.imwrite(os.path.join(saving_path, f'{img_name}_{label}_{ci}.png'), isolated)

