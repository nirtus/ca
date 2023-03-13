from ultralytics import YOLO
from torch.utils.data import DataLoader
import shutil
import os

if __name__ == '__main__':
    epochs = 200  # number of epochs to train for
    optimizer = 'Adam'  # optimizer to use
    batch_size = 32  # batch size
    save_period = 50 # save every 10 epochs
    name = str(epochs) + optimizer + str(batch_size)
    model_source = f'runs/detect/{name}/weights/best.pt'
    model_destination = f'_models/{name}/'

    # Prepare data
    # from roboflow import Roboflow
    # rf = Roboflow(api_key="oLeOSPCOjN2R94Eo6679")
    # project = rf.workspace("codeacademy-kwv2t").project("vehicles-66uwl")
    # dataset = project.version(1).download("yolov8")

    # Load a model
    model = YOLO('_models/yolov8n.yaml')  # build a new model from scratch
    #model = YOLO('runs/detect/200Adam32/weights/best.pt')  # load a pretrained model (for resumed training)
  
    # Train model
    model.train(
        device=0,
        name=name, 
        data='/Development/_ca/_data/data.yaml',
        optimizer=optimizer,
        save_period=save_period,
        batch=batch_size,
        epochs=epochs,
        workers=4,
        verbose=True,
        cache=True,
        exist_ok=True,
        val=True,
        close_mosaic=True,
    )

    # Validate the model
    model.val()

    # Export the model
    if not os.path.exists(model_destination):
        os.makedirs(model_destination)
        shutil.copy2(model_source, model_destination)
