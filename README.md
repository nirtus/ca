# Object detection and tracking
## About
Object detection model trained using [YOLOv8](https://docs.ultralytics.com).

Object tracking realised using [BoT-SORT](https://github.com/NirAharon/BoT-SORT) and [ByteTrack](https://github.com/ifzhang/ByteTrack).

## How to use
- Training is initiated by launching det_train.py
- Tracking is initiated by launding det_track.py

## Data
Data augmented with [RoboFlow](https://app.roboflow.com).

The dataset includes 862 images.
Vehicles are annotated in YOLOv8 format.

The following augmentation was applied to create 3 versions of each source image:
- Random rotation of between -10 and +10 degrees
- Random Gaussian blur of between 0 and 4 pixels
- Grayscale: Apply to 40% of images

Example 1
![Example 1](/_models/100Adam48-4/train_batch0.jpg)

[Example 2](/_models/100Adam48-4/train_batch1.jpg)

[Example 3](/_models/100Adam48-4/train_batch2.jpg)


## Training
Hyper parameters used during training:
| Parameter | Value |
| --------- | ----- |
| patience | 50 |
| close_mosaic | true |
| mask_ratio | 4 |
| iou | 0.7 |
| max_det | 300 |
| vid_stride | 1 |
| lr0 | 0.01 |
| lrf | 0.01 |
| momentum | 0.937 |
| weight_decay | 0.0005 |
| warmup_epochs | 3.0 |
| warmup_momentum | 0.8 |
| warmup_bias_lr | 0.1 |
| box | 7.5 |
| cls | 0.5 |
| dfl | 1.5 |
| nbs | 64 |
| hsv_h | 0.015 |
| hsv_s | 0.7 |
| hsv_v | 0.4 |
| translate | 0.1 |
| scale | 0.5 |
| fliplr | 0.5 |
| mosaic | 1.0 |

- Adam, epochs 100 , batch 48, data_ver 4
![Adam, epochs 100 , batch 48, data_ver 4](/_models/100Adam48-4/results.png)
- [Adam, epochs 200 , batch 32, data_ver 2](/_models/200Adam32-2/results.png)
- [Adam, epochs 200 , batch 48, data_ver 4](/_models/200Adam48-4/results.png)
- [Adam, epochs 200 , batch 64, data_ver 4](/_models/200Adam64-4/results.png)
- [SGD, epochs 200 , batch 32, data_ver 2](/_models/200SGD32-2/results.png)
- [SGD, epochs 200 , batch 48, data_ver 4](/_models/200SGD48-4/results.png)
- [SGD, epochs 200 , batch 64, data_ver 4](/_models/200SGD64-4/results.png)



## Confusion matrix

- Adam, epochs 100 , batch 48, data_ver 4
    ![Adam, epochs 100 , batch 48, data_ver 4](/_models/100Adam48-4/confusion_matrix.png)
- [Adam, epochs 200 , batch 32, data_ver 2](/_models/200Adam32-2/confusion_matrix.png)
- [Adam, epochs 200 , batch 48, data_ver 4](/_models/200Adam48-4/confusion_matrix.png)
- [Adam, epochs 200 , batch 64, data_ver 4](/_models/200Adam64-4/confusion_matrix.png)
- [SGD, epochs 200 , batch 32, data_ver 2](/_models/200SGD32-2/confusion_matrix.png)
- [SGD, epochs 200 , batch 48, data_ver 4](/_models/200SGD48-4/confusion_matrix.png)
- [SGD, epochs 200 , batch 64, data_ver 4](/_models/200SGD64-4/confusion_matrix.png)


## Validation
Predictions
![Predictions](/_models/100Adam48-4/val_batch0_pred.jpg)
[Labels](/_models/100Adam48-4/val_batch0_labels.jpg)


## Tracking
Webcamera feed was used as input for tracking.

Results in video:

[![Prediction and tracking](https://img.youtube.com/vi/8dvHar8VCfk/0.jpg)](https://www.youtube.com/watch?v=8dvHar8VCfk)

