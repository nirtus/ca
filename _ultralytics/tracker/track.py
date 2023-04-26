# Ultralytics YOLO 🚀, GPL-3.0 license

import torch
import csv
import datetime

from ultralytics.yolo.utils import IterableSimpleNamespace, yaml_load
from ultralytics.yolo.utils.checks import check_requirements, check_yaml

check_requirements('lap')  # for linear_assignment

from .trackers import BOTSORT, BYTETracker

TRACKER_MAP = {'bytetrack': BYTETracker, 'botsort': BOTSORT}


def on_predict_start(predictor):
    tracker = check_yaml(predictor.args.tracker)
    cfg = IterableSimpleNamespace(**yaml_load(tracker))
    assert cfg.tracker_type in ['bytetrack', 'botsort'], \
        f"Only support 'bytetrack' and 'botsort' for now, but got '{cfg.tracker_type}'"
    trackers = []
    for _ in range(predictor.dataset.bs):
        tracker = TRACKER_MAP[cfg.tracker_type](args=cfg, frame_rate=30)
        trackers.append(tracker)
    predictor.trackers = trackers


def on_predict_postprocess_end(predictor):
    bs = predictor.dataset.bs
    im0s = predictor.batch[2]
    im0s = im0s if isinstance(im0s, list) else [im0s]

    for i in range(bs):
        det = predictor.results[i].boxes.cpu().numpy()
        if len(det) == 0:
            continue
        tracks = predictor.trackers[i].update(det, im0s[i])
        
# CUSTOM
        write_to_csv(tracks)
# EOF CUSTOM

        if len(tracks) == 0:
            continue
        predictor.results[i].update(boxes=torch.as_tensor(tracks[:, :-1]))

        if predictor.results[i].masks is not None:
            idx = tracks[:, -1].tolist()
            predictor.results[i].masks = predictor.results[i].masks[idx]

# CUSTOM
def detection_center_point(x1, y1, x2, y2):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return (round(center_x), round(center_y))

def detection_track(input):
    slice = []
    #print(input)
    for i in input:
        x1, y1, x2, y2 = i[0], i[1], i[2], i[3]
        obj_id = int(i[4])
        obj_type = int(i[6])
        center_temp = detection_center_point(x1, y1, x2, y2)
        center_x = center_temp[0]
        center_y = center_temp[1]
        current_time = datetime.datetime.now()
        unix_timestamp = current_time.timestamp()

        slice.append([obj_id, obj_type, center_x, center_y, unix_timestamp])
        #print(id, center)
    return slice

def write_to_csv(tracks):
        slice_objects = detection_track(tracks)
        # Open the CSV file in append mode
        with open('_data/_tracks/tracks.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(slice_objects)
# EOF CUSTOM

def register_tracker(model):
    model.add_callback('on_predict_start', on_predict_start)
    model.add_callback('on_predict_postprocess_end', on_predict_postprocess_end)
