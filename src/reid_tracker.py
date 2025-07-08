import os
import cv2
import numpy as np
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

#Paths
MODEL_PATH = "yolo11s.pt"
VIDEO_PATH = "../videos/15sec_input_720p.mp4"
OUTPUT_PATH = "../output/output_with_ids.mp4"

# Load Models
if not os.path.exists(MODEL_PATH):
    print("Downloading YOLO model...")
    YOLO(MODEL_PATH)

model = YOLO(MODEL_PATH)

tracker = DeepSort(
    max_age=20,
    n_init=3,
    max_cosine_distance=0.35
)

GOALKEEPER_ID = 79  # Set this to the correct keeper ID after video inspection
player_positions = {}

#Load Video
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Could not open video.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

os.makedirs("../output", exist_ok=True)
out = cv2.VideoWriter(OUTPUT_PATH, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

CONFIDENCE_THRESHOLD = 0.5
MIN_BOX_SIZE = 30  # in pixels

print("Running Player Re-ID...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    boxes = results[0].boxes.xyxy.cpu().numpy()
    confs = results[0].boxes.conf.cpu().numpy()

    detections = []
    for i, box in enumerate(boxes):
        conf = float(confs[i])
        if conf < CONFIDENCE_THRESHOLD:
            continue

        x1, y1, x2, y2 = map(int, box)
        w, h = x2 - x1, y2 - y1

        # Filter out small or nearly square boxes 
        if w < MIN_BOX_SIZE or h < MIN_BOX_SIZE:
            continue
        aspect_ratio = w / float(h)
        if aspect_ratio < 0.3 or aspect_ratio > 1.2:
            continue

        detections.append(([x1, y1, w, h], conf, 'person'))

    print(f"Frame detections: {len(detections)}")

    tracks = tracker.update_tracks(detections, frame=frame)

    for track in tracks:
        if not track.is_confirmed():
            continue

        track_id = track.track_id
        x1, y1, x2, y2 = map(int, track.to_ltrb())

        # Save current position for minimap
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        player_positions[track_id] = (center_x, center_y)

        # Color: Red for goalkeeper, White for others
        try:
            if int(track_id) == int(GOALKEEPER_ID):
                color = (0, 0, 255)  # Red
            else:
                color = (255, 255, 255)  # White
        except:
            color = (255, 255, 255)  # Fallback to white if conversion fails


        #bounding box and label
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    # Player count overlay
    cv2.putText(frame, f"Players Tracked: {len(tracks)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    #Minimap 
    minimap_h, minimap_w = 150, 260
    minimap = np.zeros((minimap_h, minimap_w, 3), dtype=np.uint8)

    # Green field background
    minimap[:] = (34, 139, 34)

    # Midline and center circle
    cv2.line(minimap, (minimap_w // 2, 0), (minimap_w // 2, minimap_h), (255, 255, 255), 1)
    cv2.circle(minimap, (minimap_w // 2, minimap_h // 2), 20, (255, 255, 255), 1)

    for pid, (px, py) in player_positions.items():
        x_mini = int((px / width) * minimap_w)
        y_mini = int((py / height) * minimap_h)

        if pid == GOALKEEPER_ID:
            cv2.circle(minimap, (x_mini, y_mini), 4, (0, 0, 255), -1)  # Red dot
        else:
            cv2.circle(minimap, (x_mini, y_mini), 3, (255, 255, 255), -1)

    # Place minimap at bottom-right
    x_offset = width - minimap_w - 10
    y_offset = height - minimap_h - 10
    frame[y_offset:y_offset + minimap_h, x_offset:x_offset + minimap_w] = minimap

    out.write(frame)

cap.release()
out.release()
print(f"Output saved to: {OUTPUT_PATH}")
