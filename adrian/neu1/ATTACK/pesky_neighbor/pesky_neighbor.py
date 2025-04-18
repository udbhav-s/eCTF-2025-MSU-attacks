import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

# Latest channel 0 frame
ch0_frame = {"channel": 0, "timestamp": 1655042623031355, "encoded": "00000000b8058519f4ef5cd8031a5ac8baffbea2fd82874eb0a98442515a3f1eccb5e86581823e783dd12484b33842626d79685efff407b6d656fb643a901f363b52e89340e01deb4015859f14ae7d2e3dade03142630b798cfa78309ef5513b2fad07539655e74faa46b1845a10bd91007be1d122afc11d418b21a58afd3fcd1bd7fe0f70f8fce013e1c2e38c71b4e14952b8bd90e0a5d8a715e7cbc903406fd0a00eaf2c7e320bf2b9455c78f68200"}

# Earlier channel 1 frame
ch1_frame = {"channel": 1, "timestamp": 1655042617518004, "encoded": "01000000a88ba8529490e2f3457ec3d9c3f72ba1a9a3b5f5ed5af5179ac574cebcc22e20d5f9809288ea0788c1c9ddd65d9279340ed6fa3c7aeefed8dbf7df7f73d987bfdf23210a38e580f04027eef1e6bef2d7d6603da2f98eecacb3117f14d4afd20c873e567f1eaadc83cc923a82d8c6ef339ce533c079897df4df4ce4b00a5fc30b91c8187cb9837515b6d5318b48ab20df5cb6a350f4385a43c07459d5b6d6df0fb60d170cc4f1db43ac53650f"}

def gen_subscription(device_id, start, end, channel):
    return struct.pack("<IQQI", device_id, start, end, channel)

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(bytes.fromhex(ch0_frame["encoded"]))

    decoder.decode(bytes.fromhex(ch1_frame["encoded"]))

    print("Successfully decoded earlier frame")
