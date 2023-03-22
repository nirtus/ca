# Multiple detection and tracking

Object detection model trained using [YOLOv8](https://docs.ultralytics.com).

Object tracking realised using [BoT-SORT](https://github.com/NirAharon/BoT-SORT) and [ByteTrack](https://github.com/ifzhang/ByteTrack).

## Data

Data augmented with [RoboFlow](https://app.roboflow.com).

Augmentations:
- Rotation: Between -10° and +10°
- Grayscale: Apply to 40% of images
- Blur: Up to 4px

Example 1
    ![Example 1](/_models/100Adam48-4/train_batch0.jpg)

[Example 2](/_models/100Adam48-4/train_batch1.jpg)

[Example 3](/_models/100Adam48-4/train_batch2.jpg)

## Validation
Predictions
    ![Predictions](/_models/100Adam48-4/val_batch0_pred.jpg)
[Labels](/_models/100Adam48-4/val_batch0_labels.jpg)

## Training results
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


## Tracking
As tracking input webcamera feed was used. Results are displayed in video.

[![Prediction and tracking](https://img.youtube.com/vi/8dvHar8VCfk/0.jpg)](https://www.youtube.com/watch?v=8dvHar8VCfk)

