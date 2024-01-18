from ultralytics import YOLO
import torch

# 0 : Shaft
# 1 : Head
# 3 : Grip (hands)


def training():
    print(torch.backends.mps.is_available())
    model = YOLO('yolov8n-seg.pt')

    # Training.
    print(model.device)
    results = model.train(
        data='/Users/arthurlamard/Documents/ISEN5/reco_formes/Buildings_Instance_Segmentation/data.yaml',
        imgsz=340,
        epochs=70,
        batch=32,
        name='yolov8n_seg_custom',

    )