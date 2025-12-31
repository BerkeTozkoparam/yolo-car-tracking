# import Libraries
import cv2
import numpy as np
from ultralytics import YOLO
# Define the assistant function
def get_line_side(x,y, line_start, line_end):
    return np.sign((line_end[0]-line_start[0])*(y-line_start[1]) - (line_end[1]-line_start[1])*(x-line_start[0]))
# Load the YOLO model
model = YOLO('yolov8n.pt')
# Initialize video capture
cap = cv2.VideoCapture('IMG_5268.MOV')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
# Define the line coordinates
line_start = (int(frame_width * 0.5), 0)
line_end = (int(frame_width * 0.5), frame_height)
# Initialize variables
counts = {'car': 0, 'truck': 0, 'bus': 0, 'motorcycle': 0, 'bicycle': 0}
counted_id = set()
object_last_side = {}
while True:
    success, frame = cap.read()
    if not success:
        print("Failed to read video")
        break
    # Run YOLO tracking
    results = model.track(frame, persist=True, tracker="bytetrack.yaml", conf=0.3, iou=0.5)
    # Process detections and count crossings
    if results[0].boxes.id is not None:
        boxes = results[0].boxes
        for box in boxes:
            cls = int(box.cls[0])
            id = int(box.id[0])
            if model.names[cls] in counts:
                x1, y1, x2, y2 = box.xyxy[0]
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                current_side = get_line_side(cx, cy, line_start, line_end)
                if id not in object_last_side:
                    object_last_side[id] = current_side
                else:
                    if object_last_side[id] != current_side:
                        if id not in counted_id:
                            counts[model.names[cls]] += 1
                            counted_id.add(id)
                    object_last_side[id] = current_side
                # Draw bounding box and label
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                cv2.putText(frame, f'{model.names[cls]} ID:{id}', (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    # Draw the counting line
    cv2.line(frame, line_start, line_end, (0, 255, 0), 2)
    # Display counts
    y_offset = 30
    for key, value in counts.items():
        cv2.putText(frame, f'{key}: {value}', (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        y_offset += 30
    out.write(frame)
    cv2.imshow("Araç Takip", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()   