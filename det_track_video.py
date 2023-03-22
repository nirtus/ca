from ultralytics import YOLO

# Load a model
model = YOLO("_models/200SGD32-2/best.pt")  # load a pretrained model

def test():
    model.track(source="_data/_video/test_video.mp4", show=True, tracker="_cfg/botsort.yaml", line_thickness=2)

test()