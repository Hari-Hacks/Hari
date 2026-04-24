import qrcode
import json
import random
import time
import os

GRID_SIZE = 3
JSON_FILE = "scanned_data.json"
QR_FILE = "current_qr.png"


# ----------------------------
# Get Valid Moves
# ----------------------------
def get_valid_moves(x, y):
    moves = []

    if y < GRID_SIZE:
        moves.append("front")
    if x < GRID_SIZE:
        moves.append("right")
    if x > 1:
        moves.append("left")

    return moves


# ----------------------------
# Generate QR Code
# ----------------------------
def generate_qr(data):
    qr = qrcode.make(data)
    qr.save(QR_FILE)
    os.startfile(QR_FILE)


# ----------------------------
# Wait for JSON update
# ----------------------------
def wait_for_scan(previous_time):
    print("📂 Waiting for QR to be scanned...")

    while True:
        if os.path.exists(JSON_FILE):
            current_time = os.path.getmtime(JSON_FILE)

            if current_time != previous_time:
                print("✅ Scan detected (JSON updated)")
                return current_time

        time.sleep(1)


# ----------------------------
# Choose Next Move
# ----------------------------
def choose_move_from_json():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)

    return random.choice(data["valid_moves"])


# ----------------------------
# Apply Move
# ----------------------------
def apply_move(x, y, move):
    if move == "front":
        y += 1
    elif move == "right":
        x += 1
    elif move == "left":
        x -= 1

    return x, y


# ----------------------------
# MAIN PROGRAM
# ----------------------------
def main():
    x, y = 1, 1
    last_modified_time = 0

    print("🤖 Bot Started")
    print("----------------------------")

    while True:

        print(f"\n📍 Current Position: ({x},{y})")

        if (x, y) == (3, 3):
            print("🎯 Destination (3,3) Reached!")
            break

        valid_moves = get_valid_moves(x, y)

        qr_data = json.dumps({
            "cell": [x, y],
            "valid_moves": valid_moves
        })

        # Display QR
        generate_qr(qr_data)
        print("📱 QR Code displayed.")

        # Wait for scan
        last_modified_time = wait_for_scan(last_modified_time)

        # Wait 2 seconds after scan
        print("⏳ Processing move in 2 seconds...")
        time.sleep(2)

        # Choose and apply move
        move = choose_move_from_json()
        print(f"➡️ Move chosen: {move}")

        x, y = apply_move(x, y, move)
        print(f"📌 New Position: ({x},{y})")
        print("----------------------------")


if __name__ == "__main__":
    main()
