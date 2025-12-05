import serial
import threading
import time


SERIAL_PORT = 'COM5'
BAUD_RATE = 115200

# Open serial port
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for ESP32 to initialize
    print("Serial port open and ready")
except Exception as e:
    print(f"Error opening serial port: {e}")
    ser = None

lock = threading.Lock()  # Prevent simultaneous writes from multiple requests

def send_command_to_esp32(command):
    """Send numeric command to ESP32 over a persistent serial connection"""
    if ser is None:
        print("Serial port not available")
        return
    with lock:  # Ensure only one thread writes at a time
        ser.write(f"{command}\n".encode())
        print(f"Sent command: {command}")
