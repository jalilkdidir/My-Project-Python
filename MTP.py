import serial
import time

def send_at_command(ser, command, delay=1):
    ser.write((command + '\r\n').encode('utf-8'))
    time.sleep(delay)
    response = ser.read_all().decode('utf-8')
    return response.strip()

def main():
    serial_port = 'COM3'
    baud_rate = 9600

    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Serial port {serial_port} opened successfully.")

        # Send AT command to check if the modem is responding
        response = send_at_command(ser, 'AT')
        print("Response to AT command:", response)

        # Send AT command to get modem information
        response = send_at_command(ser, 'ATI')
        print("Modem information:")
        print(response)

    except serial.SerialException as e:
        print(f"Error opening serial port {serial_port}: {e}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    finally:
        try:
            ser.close()
            print(f"Serial port {serial_port} closed.")
        except (NameError, serial.SerialException):
            pass  # Handle the case where 'ser' was not defined or could not be closed

if __name__ == "__main__":
    main()