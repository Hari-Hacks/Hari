import os
import cv2
from ultralytics import YOLO
import time
import json

def log_event(filename):
    with open("log.txt", "a") as f:
        f.write(f"[ALERT] Person detected in {filename} at {time.ctime()}\n")

def alert():
    print("SAFETY ALERT: Person detected in restricted zone!")

# Load model
model = YOLO("yolo11n.pt")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "inference"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

processed_files = set()
counter = 1

print("Monitoring started...")

while True:
    try:
        files = sorted(os.listdir(UPLOAD_FOLDER))
    except Exception as e:
        time.sleep(1)
        continue

    for file in files:
        if file.endswith(".jpg") and file not in processed_files:

            filepath = os.path.join(UPLOAD_FOLDER, file)
            frame = cv2.imread(filepath)

            if frame is None:
                continue

            results = model(frame)

            person_detected = False
            boxes_data = []

            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])

                    if cls == 0:  # person class
                        person_detected = True
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        boxes_data.append({
                            "x1": x1, "y1": y1, "x2": x2, "y2": y2, "conf": conf
                        })

                        # We can still draw a faint box on the image, or leave it to the frontend.
                        # Let's draw a faint box in case the frontend misses it, but the frontend will overlay a vibrating red one.
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)

            # Safety logic
            if person_detected:
                alert()
                log_event(file)

            # Save output with sequential naming
            output_name = f"infer_{counter:04d}.jpg"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)
            cv2.imwrite(output_path, frame)
            
            # Save latest inference JSON for the dashboard to render dynamic boxes
            h, w = frame.shape[:2]
            with open("latest_inference.json", "w") as jf:
                json.dump({
                    "image": output_name,
                    "person_detected": person_detected,
                    "width": w,
                    "height": h,
                    "boxes": boxes_data
                }, jf)

            print(f"Processed: {file} -> {output_name}")

            processed_files.add(file)
            counter += 1
    
    time.sleep(0.5)