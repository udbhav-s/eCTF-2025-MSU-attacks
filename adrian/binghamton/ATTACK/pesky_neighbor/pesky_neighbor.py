import time
import sys
import struct
import json

from ectf25.utils.decoder import DecoderIntf

# first set from satellite
ch3_frame = {"channel": 3, "timestamp": 2033768432850200, "encoded": "6e6c30bab03fef4bda5c07cec5606124f2fafec9552a0539b2da0dffc8e01df77fd7959b61e11c892e8efc65147a9c71ca432ba826ec43f7ef8c944961e4a8ba50d99ec39da2d1085dfe01d2d4e93389"}
ch1_frame = {"channel": 1, "timestamp": 2033768432849785, "encoded": "403841810aaf3e35c6c6fed3d7faca63f812acb499eb8a67e9e9c37dce86d0f1de992ff40f26b20c95424981f6ffbb21e0080769a28bbd036d239f9d4ee56d2edbba2cfa2a3e2659d27f9efb6c115e6b"}
ch4_frame = {"channel": 4, "timestamp": 2033768432850293, "encoded": "fd9bcb81e1677807cc5732acdc059c08c031a61b590265c597a69864eff80bd0083154f1221425033292ce3695240c53d627a588d26d2883426af6bde12cd1415cbf723b9b3fd3854ee152c86336d5b8"}
ch2_frame = {"channel": 2, "timestamp": 2033768432850084, "encoded": "38b0ede12875e25fb4cdf6f1566ae49b90037fafaeb25238cbbb06cb205aa7c4a2d99ad405a4b8b02972a802fbadc43913df5a648d38e74451193cd11da454f954a5f10e134dba768a66464d2400ae26"}
ch0_frame = {"channel": 0, "timestamp": 2033768433704603, "encoded": "d5e1d171a1d4b864ea91e5bb4c86041dffc41ebad294b7eef0ce110ebfdb912a44d8df392e1e24de1ac3c2c59106a744ea554b3a1ee6be7198077f4a303811bd40dee774593158750ca67280cf7a9d75"}

# second set from satellite
ch1_frame = {"channel": 1, "timestamp": 2033768441374841, "encoded": "eabddf0c9d0272dbdf22b76751dfc6a4f812acb499eb8a67e9e9c37dce86d0f1de992ff40f26b20c95424981f6ffbb215098efa4b775ad8013d4f9cce25017d233735e1f484a26a3790e43abd38ed2de"}
ch2_frame = {"channel": 2, "timestamp": 2033768441375152, "encoded": "7bfc6c4c67ef9141259f73145fc89bf390037fafaeb25238cbbb06cb205aa7c4a2d99ad405a4b8b02972a802fbadc439edbfe85837051bd430860b18973bd83c1963273d9a55f3369b86543d91f188c6"}
ch4_frame = {"channel": 4, "timestamp": 2033768441375358, "encoded": "95c879f6a1e059fd723aadb716043545c031a61b590265c597a69864eff80bd0083154f1221425033292ce3695240c53533136812cc4041343532ff720f96357a8d5e3f2387bc2754630e1d167650b57"}
ch3_frame = {"channel": 3, "timestamp": 2033768441375266, "encoded": "8e153ebda7c7cdcb4ab9859326931496f2fafec9552a0539b2da0dffc8e01df77fd7959b61e11c892e8efc65147a9c718ad429e701136de88ff5afa57588922e51737b410bda3afa166644d2c8b28c2b"}
ch0_frame = {"channel": 0, "timestamp": 2033768443706040, "encoded": "fe6b41cf52b13e63c171c010877fddabffc41ebad294b7eef0ce110ebfdb912a44d8df392e1e24de1ac3c2c59106a7440c6d158475362c3a843b13a618638fdbdfeb379706fcaa0c1ee1626b0bcb510b"}

# recording
with open("recording.json", "r") as f:
    recording = json.load(f)

# subscription package
with open("pirated.sub", "rb") as f:
    pirated = f.read()

type_juggling = bytes.fromhex(ch0_frame["encoded"])[:-16] + pirated[:16]

if __name__ == "__main__":
    print("Running pesky neighbor attack")

    time.sleep(1)

    decoder = DecoderIntf(sys.argv[1])

    decoder.list()

    decoder.decode(type_juggling)

    print("Successfully decoded earlier frame")
