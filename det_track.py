import os
from ultralytics import YOLO

# Config
model_name = '200Adam64-4'
tracker = '_cfg/botsort.yaml' # select tracker configuration
save_tracks_to = '_data/_tracks'

# Video source - path to video file or camera device number (f.e. 0)
video = '_data/_video/test_video3.mp4'
# Available prerecorded videos:
# - test_video.mp4
# - test_video2.mp4
# - test_video3.mp4

# Create or clear tracks csv file
with open(f'{save_tracks_to}/tracks.csv', mode='w', newline='') as file:
    file.write('')

# Tracking
# Give time to buffer frames (approx. 30 seconds)
model = YOLO(f'_models/{model_name}/best.pt')  # select a pretrained model
model.track(source=video, show=True, tracker=tracker, line_thickness=2)

# Save track to csv file
def save_tracks_to_file(filename):
    # Remove old file if exists
    if os.path.exists(f'{save_tracks_to}/{filename}.csv'):
        os.remove(f'{save_tracks_to}/{filename}.csv')
   
    os.rename(f'{save_tracks_to}/tracks.csv', f'{save_tracks_to}/{filename}.csv')
    print(f'Tracks saved to: {save_tracks_to}/{filename}.csv')

# Name track file depending on video source
if video != 0:
    video_name = video.split('/')[-1].split('.')[0]
    save_tracks_to_file(f'{video_name}_{model_name}')
else:
    save_tracks_to_file(f'0_{model_name}')