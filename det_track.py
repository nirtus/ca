from ultralytics import YOLO

# Config
model = YOLO("_models/200SGD32-2/best.pt")  # load a pretrained model
cfg_tracker = "_cfg/botsort.yaml"
camera_source = "_data/test_video.mp4"
video_source = "_data/test_video.mp4"

# Tracking
def track(mdl, tracker, source):
    mdl.track(source=source, show=True, tracker=tracker, line_thickness=2)


# Track either camera or saved video
#camera_track = track(model, cfg_tracker, camera_source)
video_track = track(model, cfg_tracker, video_source)