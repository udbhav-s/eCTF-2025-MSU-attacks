import time
import sys
import json

from ectf25.utils.decoder import DecoderIntf

if __name__ == "__main__":
    print("Running pirated subscription attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    with open("frames.json") as f:
        frames = json.loads(f.read())

    # Load pirated subscription
    # with open("pirated.sub", "rb") as f:
    #     contents = f.read()

    #     decoder.subscribe(contents)

    # decoder.list()

    # Load expired subscription
    try:
        with open("expired.sub", "rb") as f:
            contents = f.read()

            decoder.subscribe(contents)
    except Exception as e:
        print(e)

    decoder.list()

    # Expired sub
    try:
        decoder.decode(bytes.fromhex(frames["ch2_frame"]["encoded"]))
    except Exception as e:
        print(e)

    # Pirated sub
    try:
        decoder.decode(bytes.fromhex(frames["ch3_frame"]["encoded"]))
    except Exception as e:
        print(e)

    # No sub
    try:
        decoder.decode(bytes.fromhex(frames["ch4_frame"]["encoded"]))
    except Exception as e:
        print(e)

    print("End of test")
