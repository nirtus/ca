from ultralytics import YOLO

# Load a model
model = YOLO("_models/100Adam48-4/best.pt")  # load a pretrained model
#model.device('cuda')

model.track(device=0, source=0, show=False, tracker="botsort.yaml")




# def show_stream():
#     while True:
#         # Read a frame from the camera
#         ret, frame = video.read()
#         #results = model.track(source=0, show=True, tracker="botsort.yaml")
#         results = model.track(source=frame, show=True, tracker="bytetrack.yaml")
#         #results = model.predict(frame, device=0)
#         #boxes.plot_bboxes(frame, results[0].boxes.boxes, conf=0.6)


#         #results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True, tracker="bytetrack.yaml")
#         # predictions = model(frame)  # predict on an image

#         # for r in predictions:
#         #     #print(r.boxes.xyxy)
#         #     boxes = r.boxes.xyxy  # Boxes object for bbox outputs

#         #     for box in boxes:
#         #         x1, y1, x2, y2 = int(box[:1]), int(box[1:2]), int(box[2:3]), int(box[3:4])
#         #         #print(x1, y1, x2, y2)
#         #         cv2.rectangle(frame, (x1, y1), (x2, y2), (1, 255, 1), 2)

#         # # Display the frame to the user
#         # cv2.imshow('Video', frame)

#         # Exit the loop if the user presses the 'q' key
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera and destroy the window
#     video.release()
#     cv2.destroyAllWindows()


# show_stream()