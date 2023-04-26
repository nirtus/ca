# Object detection and tracking
Project goal is to find out objects speed and objects count using custom trained models and tracking.

## Problem
Some vehicles, at first glance, appear to be driving above legal limit, especialy then traffic lights are about to change.

## Solution
Camera was installed to observe intersection exit and collect data.
Model was trained to recognise vehicles and track them.
Tracking results were saved to csv files. And objects speed in sector next to intersection exit was calculated.

### Examples of speed detection
test_video, object id 2
![test_video, object id 2](/_data/_images/scatter_speed_test_video_200Adam64-4.csv.png)

test_video3, object id 2
![test_video3, object id 2](/_data/_images/scatter_speed_test_video3_200Adam64-4.csv.png)

## Techstack
Object detection model trained using [YOLOv8](https://docs.ultralytics.com).

Object tracking realised using [BoT-SORT](https://github.com/NirAharon/BoT-SORT) and [ByteTrack](https://github.com/ifzhang/ByteTrack).

### Python libraries:
- csv
- pandas
- ast
- matplotlib
- PIL
- shapely
- os
- ultralytics
- shutil
- roboflow
- torch

## How to use 
### Training:
Training is initiated by launching **det_train.py**

Default parameters: epochs 100, optimizer 'Adam', batch size 64, lr 0.01, save every 20th epoch, dataset version 4

### Tracking:
Tracking is initiated by launching **det_track.py**

Default model: 200Adam64-4 (more pretrained models in can be found in "_models" direcory)

Default video source: _data/_video/test_video3.mp4

### Ploting:
Plotting is initiatd by launching **det_plot_file.py**

Default object id: 2 (0 - all objects, other than 0 - specific object by id)

Default detections file: test_video3_200Adam64-4.csv (more example detections can be found in "_data/_tracks" directory)

## Data
Data augmented with [RoboFlow](https://app.roboflow.com).

The dataset consists of 862 images.
Objects are annotated in YOLOv8 format.

The following augmentations were applied to create 3 dataset versions:
- Random rotation of between -10 and +10 degrees
- Random Gaussian blur of between 0 and 4 pixels
- Grayscale: Applied to 40% of images

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
To test detection and tracking webcamera feed was used as input.

Results can be seen in video:

[![Prediction and tracking](https://img.youtube.com/vi/8dvHar8VCfk/0.jpg)](https://www.youtube.com/watch?v=8dvHar8VCfk)

## Tracking Plots

Examples of detections in sequence of frames

Dots represent center points of detected objects.
![Figure 6](/_data/_images/Figure_6.png)
![Figure 7](/_data/_images/Figure_7.png)
[Figure 1](/_data/_images/Figure_1.png)
[Figure 2](/_data/_images/Figure_2.png)
[Figure 3](/_data/_images/Figure_3.png)
[Figure 4](/_data/_images/Figure_4.png)
[Figure 5](/_data/_images/Figure_5.png)
