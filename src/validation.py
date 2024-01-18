from ultralytics import YOLO

def validation():
    model = YOLO('/Users/arthurlamard/Documents/ISEN5/reco_formes/best.pt')

    model.val(
    data='/Users/arthurlamard/Documents/ISEN5/reco_formes/Buildings_Instance_Segmentation/data.yaml',
    split='test',
    )

