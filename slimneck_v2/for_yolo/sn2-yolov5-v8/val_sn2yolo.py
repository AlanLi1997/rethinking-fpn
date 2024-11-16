from ultralytics import YOLO

# slim_neck_v2(SN) for yolo
if __name__ == '__main__':
    model = YOLO("runs/sn2-yolo/weights/best.pt")  # model.yaml config
    results = model.val(
        data="ultralytics/yolo/data/datasets/coco128.yaml",  # datasets
        device='0',
        imgsz=640,
        batch=64,
        workers=16,
        name='sn2-yolo-val',
        half=False,
    )