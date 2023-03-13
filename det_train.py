from ultralytics import YOLO
from torch.utils.data import DataLoader
import shutil
import os
from _utils.helpers import *

if __name__ == '__main__':
    epochs = 1  # number of epochs to train for
    optimizer = 'Adam'  # optimizer to use
    batch_size = 48  # batch size
    save_period = 50 # save every 50 epochs
    device = 0 # CPU None, CUDA 0
    data_version = 4
    name = str(epochs) + optimizer + str(batch_size) + '-' + str(data_version)
    data_path = f'/Development/_ca/vehicles-{data_version}/data.yaml'
    model_source = f'runs/detect/{name}/'
    model_destination = f'_models/{name}/'

    # Prepare data
    from roboflow import Roboflow
    rf = Roboflow(api_key="oLeOSPCOjN2R94Eo6679")
    project = rf.workspace("codeacademy-kwv2t").project("vehicles-pol8y")
    dataset = project.version(data_version).download("yolov8")

    # Load a model
    model = YOLO('yolov8n.yaml')  # build a new model from scratch
    #model = YOLO(f'runs/detect/{name}/weights/best.pt')  # for resumed training if unfinished
  
    # Train model
    model.train(
        device=device,
        name=name, 
        data=data_path,
        optimizer=optimizer,
        save_period=save_period,
        batch=batch_size,
        epochs=epochs,
        workers=4,
        resume=True,
        verbose=True,
        cache=True,
        exist_ok=True,
        val=True,
        pretrained=True,
        close_mosaic=True,
    )

    # Export model and training results
    if not os.path.exists(model_destination):
        os.makedirs(model_destination)

    shutil.copy2(f'{model_source}/weights/best.pt', model_destination)
    shutil.copy2(f'{model_source}/results.png', model_destination)
    shutil.copy2(f'{model_source}/confusion_matrix.png', model_destination)

    resize_image(f'{model_destination}/results.png', 30)
    resize_image(f'{model_destination}/confusion_matrix.png', 30)
