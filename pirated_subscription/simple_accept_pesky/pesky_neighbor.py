import time
import sys
import json

from ectf25.utils.decoder import DecoderIntf

if __name__ == "__main__":
    print("Running pirated subscription attack")

    time.sleep(1)

    # Load frames
    with open("frames.json") as f:
        frames = json.loads(f.read())

    decoder = DecoderIntf(sys.argv[1])

    # Load pirated subscription
    with open("pirated.sub", "rb") as f:
        contents = f.read()

        decoder.subscribe(contents)

    decoder.list()

    # Try to decode the channel from pirated subscription
    ch3_frame = bytes.fromhex(frames["ch3_frame"]["encoded"])

    out = decoder.decode(ch3_frame)

    print(out)

    print("Successfully decoded pirated channel frame")
