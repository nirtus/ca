from ultralytics import YOLO

# Clear file
with open('_data/_tracks/tracks.csv', mode='w', newline='') as file:
    file.write('')

# Config
model = YOLO("_models/200Adam64-4/best.pt")  # load a pretrained model
cfg_tracker = "_cfg/botsort.yaml"
source_camera = 0
#source_video = "_data/_video/test_video3.mp4" #predict_and_track
source_video = "_data/_backup/street_view2.mp4" #predict_and_track

# Tracking
def track(mdl, tracker, source):
    mdl.track(source=source, show=False, tracker=tracker, line_thickness=2)

# Track either camera or saved video
camera = track(model, cfg_tracker, source_camera)
#video = track(model, cfg_tracker, source_video)


