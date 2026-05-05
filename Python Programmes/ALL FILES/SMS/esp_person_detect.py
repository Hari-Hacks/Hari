import os
import cv2
from ultralytics import YOLO
import time

def log_event(filename):
    with open("log.txt", "a") as f:
        f.write(f"[ALERT] Person detected in {filename} at {time.ctime()}\n")

def alert():
    print("⚠️ SAFETY ALERT: Person detected in restricted zone!")

# Load model
model = YOLO("yolo11n.pt")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "inference"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

processed_files = set()
counter = 1

print("🚀 Monitoring started...")

while True:
    files = sorted(os.listdir(UPLOAD_FOLDER))

    for file in files:
        if file.endswith(".jpg") and file not in processed_files:

            filepath = os.path.join(UPLOAD_FOLDER, file)
            frame = cv2.imread(filepath)

            if frame is None:
                continue

            results = model(frame)

            person_detected = False

            for r in results:
                for box in r.boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])

                    if cls == 0:  # person class
                        person_detected = True

                        x1, y1, x2, y2 = map(int, box.xyxy[0])

                        # Draw bounding box
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f"Person {conf:.2f}",
                                    (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    0.6, (0, 255, 0), 2)

            # 🚨 Safety logic
            if person_detected:
                alert()
                log_event(file)

            # Save output with sequential naming
            output_name = f"infer_{counter:04d}.jpg"
            output_path = os.path.join(OUTPUT_FOLDER, output_name)

            cv2.imwrite(output_path, frame)

            print(f"Processed: {file} → {output_name}")

            processed_files.add(file)
            counter += 1