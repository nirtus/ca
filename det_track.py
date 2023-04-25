from ultralytics import YOLO

# Config
model = YOLO("_models/200Adam64-4/best.pt")  # select a pretrained model
tracker = "_cfg/botsort.yaml" # select tracker configuration

# Video source
# Either path to video file or camera device number (f.e. 0)
# Prerecorded videos for testing:
# - test_video.mp4
# - test_video2.mp4
# - test_video3.mp4
video = "_data/_video/test_video3.mp4"

# Tracking
# Give time to buffer frames (approx. 30 seconds)
model.track(source=video, show=True, tracker=tracker, line_thickness=2)
