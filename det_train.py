import os
import shutil

from roboflow import Roboflow
from torch.utils.data import DataLoader
from ultralytics import YOLO

from _utils.helpers import *

if __name__ == '__main__':
    # Trainer
    def train(epochs, optimizer, batch_size, learning_rate, save_period, data_version):
        #epochs = epochs  # number of epochs to train for
        #optimizer = optimizer  # optimizer to use
        #batch_size = batch_size  # batch size
        #save_period = save_period # save every 50 epochs
        device = 0 # CPU None, CUDA 0
        data_version = data_version
        name = str(epochs) + optimizer + str(batch_size) + str(learning_rate) + '-' + str(data_version)
        data_path = f'/Development/_ca/vehicles-{data_version}/data.yaml'
        model_source = f'runs/detect/{name}/'
        model_destination = f'_models/{name}/'

        # Prepare data
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
            lr1=learning_rate,
            pretrained=False,
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

    # Train models
    # train(200, 'Adam', 48, 50, 4)
    # train(200, 'SGD', 48, 50, 4)

    # train(200, 'Adam', 64, 50, 4)
    # train(200, 'SGD', 64, 50, 4)

    train(20, 'Adam', 64, 0.01, 10, 1)
    train(20, 'SGD', 64, 0.01, 10, 1)
    train(20, 'Adam', 64, 0.01, 10, 2)
    train(20, 'SGD', 64, 0.01, 10, 2)
    train(20, 'Adam', 64, 0.01, 10, 4)
    train(20, 'SGD', 64, 0.01, 10, 4)

    train(20, 'Adam', 64, 0.05, 10, 1)
    train(20, 'SGD', 64, 0.05, 10, 1)
    train(20, 'Adam', 64, 0.05, 10, 2)
    train(20, 'SGD', 64, 0.05, 10, 2)
    train(20, 'Adam', 64, 0.05, 10, 4)
    train(20, 'SGD', 64, 0.05, 10, 4)