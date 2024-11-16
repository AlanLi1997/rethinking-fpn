# ECCV 2024: [Rethinking Features-Fused-Pyramid-Neck for Object Detection](https://link.springer.com/chapter/10.1007/978-3-031-72855-6_5)

[English](README.md) | [简体中文](README-zh-CN.md)| [Paper PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/08386.pdf)

(事实上我想把这个工作称为 _Slim Neck V2_. 因为这是我继 [_Slim Neck by GSConv_](https://github.com/AlanLi1997/slim-neck-by-gsconv) 后的工作😀)

Cheems的生日是11月6日，我们会在11月16日——它生日的十天后——发布代码。

小彩蛋 - Cheems(Balltze)。23年初，在我对“特征融合”范式进行反思并计划进行深入研究时，Cheems开始频繁地出现在我的社交软件中。我很喜欢它的样子，每次看到它我都能获得一些快乐的能量，但是它在我还没完成这篇论文时就已经去了另一个世界。我把它最令我印象深刻的样子放在了论文中的主要图解中来纪念它。感谢像Cheems这样的可爱的小动物们治愈我们的心灵。

<p align="center">
  <img src="https://github.com/AlanLi1997/rethinking-fpn/blob/main/figs/sni.png" alt="" width="500" />
</p>

**摘要**<br />
(英译汉简化非正式版)
多头检测器例行采用特征融合金字塔或类似方法用于多尺度检测并在业界中被广泛使用。
但是，现存的类似方法在融合来自不同层级的分辨率不同的特征(表征时)面临特征不对齐问题。
可是这个问题却一直被研究人员们忽视长达7年之久，搞不懂.....
为了证明我们的发现，我们首先设计了一个完全不使用任何类FPN的特征融合方案的结构——层间独立金字塔(IHP)来反向评估特征融合金字塔的效果。
然后，设计了软上采样方法(SNI)来缓解特征不对齐问题，并针对特征对齐捕获和实时推理设计了扩展的窗口特征选择下采样和一些轻量化方法。
最后，给以上解决方案综合地取了个名字——辅助特征对齐方案(SA)。
为什么要轻量化？这延续了部分[_Slim Neck by GSConv_](https://github.com/AlanLi1997/slim-neck-by-gsconv) 的工作。
事实上我一直觉得现在的实时感知模型脖子和头还是太粗了(天鹅颈应该是比头大脖子粗漂亮一些...)。
结果，我们的发现被实验证实了：IHP反直觉地提高了模型精度。SA以更少的成本实现了SOTA。

## 准备数据集和运行环境
1.数据集
```
├── rethinking-fpn
│   ├── datasets
│   │   ├── coco
│   │   │   ├──images
│   │   │   │  ├──1.jpg
│   │   │   │  ├──...
│   │   │   ├──labels
│   │   │   │  ├──1.txt
│   │   │   │  ├──...
│   │   ├──VOC...
```

2.环境

    pip install requirements.txt
经过测试的工程可良好运行的环境:<br />
python==3.8.16<br />  pytorch==1.12.0(py3.8_cuda11.3_cudnn8.3.2_0)<br /> torchvision==0.13.0(py38_cu113)<br />


## 训练 sn2yolo 系列模型
    python ./slimneck_v2/for_yolo/sn2-yolov5-v8/train_sn2yolo.py

## 训练 sn2fpn(R-CNN) 系列模型
    python train_sn2fpn.py

## 验证 sn2yolo 系列模型
    python ./slimneck_v2/for_yolo/sn2-yolov5-v8/val_sn2yolo.py

## 训练权重
没有。<br>
租的服务器BMW出来那几天给我清了，但我在冲黄风岭八百里。(BMW不是车，是Black Myth WuKong) <br />
VOC上训练小模型可以轻松复现论文结果。<br>
训练SYolo成本贵，8张3090才可以跑coco的SOTA.但如果你有4090就快的多。

 ## 参考
  - https://github.com/AlanLi1997/slim-neck-by-gsconv
  - https://github.com/ultralytics/ultralytics
  - https://github.com/jwyang/fpn.pytorch
  - https://github.com/WongKinYiu/yolov7



## 引用此工作
@inproceedings{re-fpn,<br />
  title={Rethinking Features-Fused-Pyramid-Neck for Object Detection},<br />
  author={Li, Hulin},<br />
  editors={Leonardis, A., Ricci, E., Roth, S., Russakovsky, O., Sattler, T., Varol, G.}<br />
  booktitle={Computer Vision – ECCV 2024. ECCV 2024. Lecture Notes in Computer Science, vol 15125.},<br />
  pages={74-90},<br />
  year={2024},<br />
  publisher={Springer, Cham.}, <br />
  doi={10.1007/978-3-031-72855-6_5}, <br />
}