import os
from flask import Flask, render_template_string, jsonify, send_from_directory

app = Flask(__name__)

# Config paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INFERENCE_FOLDER = os.path.join(BASE_DIR, "inference")
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

# Manually add CORS to allow the HTML file to work if opened directly (file://)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/")
def dashboard():
    html_path = os.path.join(BASE_DIR, "dashboard.html")
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    return "dashboard.html not found.", 404

@app.route("/api/data")
def get_data():
    # Get latest image
    images = []
    if os.path.exists(INFERENCE_FOLDER):
        images = [f for f in os.listdir(INFERENCE_FOLDER) if f.endswith(".jpg")]
        # Sort by modification time to ensure we get the absolute latest
        images.sort(key=lambda x: os.path.getmtime(os.path.join(INFERENCE_FOLDER, x)), reverse=True)
    
    latest_image = images[0] if images else None
    total_images = len(images)
    
    # Get logs
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    
    # Filter out empty lines
    logs = [log.strip() for log in logs if log.strip()]
    
    recent_logs = logs[-50:]
    recent_logs.reverse() # Newest first
    
    return jsonify({
        "latest_image": latest_image,
        "total_images": total_images,
        "total_alerts": len(logs),
        "logs": recent_logs
    })

@app.route("/inference/<path:filename>")
def get_inference_image(filename):
    return send_from_directory(INFERENCE_FOLDER, filename)

if __name__ == "__main__":
    print("Starting IIoT Dashboard on http://0.0.0.0:5001")
    app.run(host="0.0.0.0", port=5001, debug=False)
