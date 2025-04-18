import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

ch3_frame = {"channel": 3, "timestamp": 2047018172095339, "encoded": "f0f38a7176b7a1f0bc253c69c5baab357e24c90b83bb96619915b05a899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9d75c2324a402ee3c1e85291d8e3eeb528cba5705e8b89a4bcef525c0dce15ca9d22fb23277e2d8ac48bc"}
ch4_frame = {"channel": 4, "timestamp": 2047018172095396, "encoded": "f7f38a71b9b7a1f0bc253c699eb8a0322d20980b80ef943f9a40b101899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9800a2324a402ee3c1e857749863dbe588aef5101b3ea9817cff0c0a2c5cf1c17c43574972d081cf66030"}
ch1_frame = {"channel": 1, "timestamp": 2047018172095064, "encoded": "f2f38a7145b6a1f0bc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a1125fa0a5f282cad4062324a402ee3c1e852e49da6ebb0e82ba0752b8ed9f4b94f0ff842d5fffea96bfaa5c3248705b1dd2"}
ch2_frame = {"channel": 2, "timestamp": 2047018172095273, "encoded": "f1f38a7134b7a1f0bc253c69c9eda83c79769a5987ea95609a45b053899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9d3072324a402ee3c1e85761bd93aec5cdfe8540eb9eb9d1bc7f47794509f853423017ad8a10b645722cf"}
ch0_frame = {"channel": 0, "timestamp": 2047018173619389, "encoded": "f3f38a71a0f048f1bc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a1125fa3f2a286c8835a2324a402ee3c1e85794ddc6bb95bd8ed0050bae49f1cc2f1f44acc515c75d227c691d3bbc0215610"}

pirated_subscription = open("pirated.sub", "rb").read()

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.subscribe(pirated_subscription)
    decoder.decode(bytes.fromhex(ch3_frame["encoded"]))

    print("Successfully decoded earlier frame")
