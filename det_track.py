from ultralytics import YOLO
import csv


# Clear file
with open('_data/_tracks/tracks.csv', mode='w', newline='') as file:
    file.write('')

# Config
model = YOLO("_models/200SGD32-2/best.pt")  # load a pretrained model
cfg_tracker = "_cfg/botsort.yaml"
source_camera = 0
source_video = "_data/test_video3.mp4"

# Tracking
def track(mdl, tracker, source):
    mdl.track(source=source, show=True, tracker=tracker, line_thickness=2)


# Track either camera or saved video
camera = track(model, cfg_tracker, source_camera)
#video = track(model, cfg_tracker, source_video)


