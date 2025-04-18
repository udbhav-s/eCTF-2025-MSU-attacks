import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

# Latest channel 0 frame
ch0_frame = {"channel": 0, "timestamp": 1741212001193158, "encoded": "00000000c64ccf829f2f060039ec3083248e1d463ee1d2becf7b628ed486281c96869c48942b34149fea51220eed5a90d1389eb49b971708e94acdc19fd72ba105fdd3621dd589816a133e2b15a8face7efb8ecd205e7949f38ac62cb8fbb64eee027397bb78583d4894f610b96853b70f6d640f36b55acd"}

# Earlier channel 1 frame
ch1_frame = {"channel": 1, "timestamp": 1741211991511696, "encoded": "0100000090923b829f2f0600a032eb6e0516bd6f85d57d98bf88ce3934edaea833137d237e38348b051400c1a3835446ad5c9a8198b3d539902aeea6d015c6160267991778df06573112b3f24c8077943d62e883e2075f66d8ecddbbdd207f88b5daf7e99d287880b6bea5dd7f5f3ead1b72cf7c83ca46f9"}

def gen_subscription(device_id, start, end, channel):
    return struct.pack("<IQQI", device_id, start, end, channel)

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(bytes.fromhex(ch0_frame["encoded"]))

    decoder.decode(bytes.fromhex(ch0_frame["encoded"]))

    print("Successfully decoded earlier frame")
