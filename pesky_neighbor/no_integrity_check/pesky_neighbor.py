# Execution of a "Pesky Neighbor" attack against a team

import time
import sys
import json

from ectf25.utils.decoder import DecoderIntf

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    with open("frames.json") as f:
        frames = json.loads(f.read())

    ch1_frame = frames["ch1_frame"]

    # In UCF, a frame is encoded_frame = channel (4) + iv (12) + body (64)
    # Where body is max of size 80 (with 16 bytes padding)
    frame_data = bytes.fromhex(ch1_frame["encoded"])
    frame_data = frame_data[:50] + bytes([frame_data[50] ^ 0xff]) + frame_data[51:]

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(frame_data)

    print("Successfully decoded modified frame")
