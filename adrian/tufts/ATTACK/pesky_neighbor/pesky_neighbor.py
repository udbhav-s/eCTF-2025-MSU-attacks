import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

# Latest channel 0 frame
ch0_frame = {"channel": 0, "timestamp": 2019123066186019, "encoded": "131caadb5c75abc019ee9443aedf155eec62d970c16f932045c514271d294291b1b0e8e99a2f17ed047ef1857b36554874e3ddcfbfaa8a9a255067235b259c7d077ff005b658a7a33ccab0045e7ec6009f7bb1edea095c90909901160412671e75ff639734ff05cb54ae521f66790cf0902ee37870a703e810d6436fc08fd2deafcff52be29fc8363c4b6cd2bc5a6c237f917cb6a1d10aee63e68f3b4d872bb1"}

# Earlier channel 1 frame
ch1_frame = {"channel": 1, "timestamp": 2019123130983546, "encoded": "1662607b3b8d76e99cf9820f643109b0fbfd2a99920cdba05b1163caeb460c45151c4046abe464c392c9acec9c49d93b06afb10f9d027331c16f3b59d7b50757765472c8e21b641b3942623aa10f61440769ccddaecc7fe76eb62d3dc4a4eef7e09b3081b325feaeab9c2fada7a0f4e7b5290295b6adc60695c1684ce0d79114f8a54bd175594763366aaf01f1ff6f3f6ff0589be960d7e6740374a2b73e3b36"}

def gen_subscription(device_id, start, end, channel):
    return struct.pack("<IQQI", device_id, start, end, channel)

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(bytes.fromhex(ch1_frame["encoded"]))

    decoder.decode(bytes.fromhex(ch0_frame["encoded"]))

    print("Successfully decoded earlier frame")
