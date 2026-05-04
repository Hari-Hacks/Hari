from flask import Flask, request, send_from_directory
import os, time

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return "ESP32-CAM upload server is running."

@app.route("/upload", methods=["POST"])
def upload():
    img_bytes = request.data

    ts = int(time.time())
    filename = os.path.join(UPLOAD_FOLDER, f"cam_{ts}.jpg")

    with open(filename, "wb") as f:
        f.write(img_bytes)

    print(f"Saved image: {filename} ({len(img_bytes)} bytes)")
    return "OK\n"

@app.route("/uploads/<filename>")
def get_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)