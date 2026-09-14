import serial
import time

rates = [9600, 19200, 38400, 57600, 74880, 115200, 230400, 921600]
port = '/dev/ttyUSB0'

for baud in rates:
    print(f"\n--- Testing Baud Rate: {baud} ---")
    try:
        with serial.Serial(port, baud, timeout=2) as ser:
            # Send a newline to try and prompt a response
            ser.write(b'\r\n')
            time.sleep(0.5)
            # Read whatever comes back
            data = ser.read(200)
            if data:
                print(f"Received data: {data}")
            else:
                print("No data received.")
    except Exception as e:
        print(f"Could not open port: {e}")
