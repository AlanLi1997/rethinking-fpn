from ultralytics import YOLO

# slim_neck_v2(SN) for yolo
if __name__ == '__main__':
    model = YOLO("models-cfg/sn2-yolov8n.yaml")  # model.yaml config
    results = model.train(
        data="ultralytics/yolo/data/datasets/coco128.yaml",  # datasets
        device='0',
        epochs=400,
        imgsz=640,
        batch=64,
        workers=16,
        # amp=False,
        optimizer='SGD',
        cache=True,
        name='sn2-yolo',
        resume=False,
        half=False,
    )