import serial
import time
import sys
import os
from parser_scripts.parser_mmw_demo import parser_one_mmw_demo_output_packet

# === Configuration ===
CLI_PORT = '/dev/ttyUSB0'
DATA_PORT = '/dev/ttyUSB1'
CFG_FILE = 'xwr68xxconfig.cfg'
BAUD_CLI = 115200
BAUD_DATA = 921600

RAW_OUTPUT_FILE = "raw_capture.csv"
BUFFER_SIZE = 4096

# === Initialize CLI port ===
def send_config(cli: serial.Serial):
    print("Sending config...")
    cli.write(b'sensorStop\n')
    time.sleep(0.1)
    with open(CFG_FILE) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('%'):
                cli.write((line + '\n').encode())
                print(">>", line)
                time.sleep(0.05)
    print("Radar configured.")


def main():
    print("Opening serial ports...")
    cli = serial.Serial(CLI_PORT, BAUD_CLI, timeout=1)
    data = serial.Serial(DATA_PORT, BAUD_DATA, timeout=1)

    send_config(cli)

    print("Starting data capture... Press Ctrl+C to stop.")
    start_time = time.time()
    frame = 0
    keys = None
    with open(RAW_OUTPUT_FILE, 'w') as f:
        try:
            while True:
                chunk = data.read(data.in_waiting or BUFFER_SIZE)
                print(f"Captured {len(chunk)} bytes")
                if chunk:
                    _, _, _, numDetObj, _, _, x_array, y_array, \
                        z_array, v_array, range_array, azimuth_array, \
                            elevAngle_array, snr_array, noise_array = parser_one_mmw_demo_output_packet(chunk, len(chunk))
                    for obj in range(numDetObj):
                        datadict = {
                            'frame': frame, 'x(m)': x_array[obj], 'y(m)': y_array[obj], 'z(m)': z_array[obj],
                            'velocity(m/s)': v_array[obj], 'range(m)': range_array[obj],
                            'azimuth(deg)': azimuth_array[obj], 'elevation(deg)': elevAngle_array[obj],
                            'SNR(dB)': snr_array[obj] / 10, 'noise(dB)': noise_array[obj] / 10,
                            'signal(dB)': snr_array[obj] / 10 + noise_array[obj] / 10}
                        if keys is None:
                            keys = datadict.keys()
                            f.write(','.join(keys) + '\n')
                        f.write(','.join(str(datadict[k]) for k in keys) + '\n')
                        f.flush()
                time.sleep(0.001)
                frame += 1
        except KeyboardInterrupt:
            print("Stopping capture...")
        finally:
            cli.write(b'sensorStop\n')
            cli.close()
            data.close()
            print("Serial ports closed.")
            print(f"Total capture time: {time.time() - start_time:.2f} seconds")

if __name__ == '__main__':
    main()
