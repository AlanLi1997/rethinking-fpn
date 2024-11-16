from ultralytics import YOLO

if __name__ == '__main__':
    # 初始训练
    model = YOLO("slimneck_v2/for_yolo/sn2-yolov5-v8/models-cfg/sn2-yolov8n.yaml") # 加载预训练模型，如果本地没有会自动下载
    results = model.train(
        data="slimneck_v2/for_yolo/sn2-yolov5-v8/ultralytics/yolo/data/datasets/coco128.yaml",
        # task='segment',
        # model='ultralytics/models/v8/seg/yolov8n-seg.yaml',
        device='0',
        epochs=200,
        imgsz=640,
        batch=16,
        workers=16,
        #amp=False,
        optimizer='SGD',
        cache=True,
        name='sn2-yolo',
        resume=False,
        half=False,

    )