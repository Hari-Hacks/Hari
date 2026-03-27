import serial
import json

# 🔥 CHANGE THIS
ser = serial.Serial('COM9', 9600, timeout=1)

print("Reading...\n")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        if not line:
            continue

        print("RAW:", line)   # 🔥 debug line (important)

        data = json.loads(line)

        left = data["left"]
        right = data["right"]

        if left == 1 and right == 1:
            print("BOTH\n")
        elif left == 1:
            print("LEFT\n")
        elif right == 1:
            print("RIGHT\n")
        else:
            print("NONE\n")

    except Exception as e:
        print("Error:", e)