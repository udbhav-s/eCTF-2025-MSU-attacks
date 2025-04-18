import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(b'0'*200)

    print("Successfully decoded earlier frame")
