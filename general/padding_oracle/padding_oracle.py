# Run from a venv containing the installed host tools and dependencies

import struct
from time import sleep
import random
from ectf25.utils.decoder import DecoderIntf, Opcode, Message
from loguru import logger
from get_frame import get_frame

decoder = DecoderIntf("/dev/ttyACM0")


def make_frame(channel, timestamp, data):
    return struct.pack("<IQ", channel, timestamp) + data


def make_frame_msg(channel, timestamp, data):
    return Message(Opcode.DECODE, make_frame(channel, timestamp, data))


frame_data = get_frame("54.86.219.63", 2502)

# recording playback
# frame_data = {'channel': 1, "timestamp": 124074024752855, "encoded": "01000000186a3f83f661cb91a2f97d41a291abe1056b710555abb28d3075f55446232a8f0829a8647dfa46c7abc1ac546a408fb5e7423d8bcea8ef5f59d9576d90e05ea7029bbffcb2b5229d191c91d8330a3a43f01d5ef5f7f82fc4154c50e98c54bc95"}

# frame_data = {'channel': 1, 'timestamp': 1961896442386669, 'encoded': '010000003ae6fcff386cc8afc266e2f2eafe0ba43c62af9ff5902f8083862a515e44cec2c0b7f9e2283d75c7ed4fb5db7e87e816a29ebb3915908029bda6f9056f8f45b9a4b62d6b1cdf2fde7892aa8faac20493bd51333ec64e7949e58edcde9f25911b'}
# frame_data = {"channel": 4, "timestamp": 1961901714025334, "encoded": "040000008a09e13b2fe21e489d8b40b060bc717b21970354a57f561015afeebdf89ae24068fbc04d635e9d54209e08fba018d7bd93bb4440deead23a9270ccab726356a87bdc0fda6c01dfa4e84c542debe506824aae3d632bcae5d5afa0f872e6cb3361"}

print("Got frame: ")
print(frame_data)


def decode_test():
    for i in range(5):
        f = get_frame("54.86.219.63", 2501)
        print(decoder.decode(bytes.fromhex(f["encoded"])))


frame = bytes.fromhex(frame_data["encoded"])
ch, iv = frame[:4], frame[4:20]
enc = frame[20:]
blocks = [enc[(16 * i) : (16 * (i + 1))] for i in range(5)]

# new_blocks = blocks[:]

# decoded = [132, 142, 17, 82, 116, 181, 70, 224, 120, 157, 164, 130, 166, 201, 14, 154]
# change_byte = new_blocks[3][-(len(decoded)+1)]


# bidx: index of previous block
def frame_replace_block(bidx, ba):
    # If bidx is -1, we are using IV as previous block
    # and we want to decrypt the first encrypted block
    if bidx == -1:
        new_frame = ch + bytes(ba) + enc[:16]
        return new_frame

    # We are decrypting a later encrypted block
    new_blocks = blocks[:]
    new_blocks[bidx] = bytes(ba)
    new_enc = (b"").join(new_blocks)
    new_frame = frame[:20] + new_enc
    # Cut off last blocks depending on which block we're finding
    # Block 3 is used to find block index 4 (the last block)
    if bidx < 3:
        new_frame = new_frame[: -(3 - bidx) * 16]
    return new_frame


def frame_passes_padding(frame, i):
    try:
        decoder.decode(frame)
        print(f"Successful padding decrypt with byte {i}!")
        return True
    except Exception as e:
        print(f"Decoder threw error for byte {i}")
        print(str(e))

        return not ("Cryptographic" in str(e))


def next_block_byte(bidx, last_block, decoded):
    change_byte = last_block[-(len(decoded) + 1)]
    for i in range(256):
        # We know the actual padding for the frame is 0x08
        # So the original byte cannot yield a 0x01
        if len(decoded) == 0 and i == change_byte:
            continue

        print(f"Trying byte {i:03d} for block {bidx:1d}")

        ba = bytearray(last_block)

        # print([int(n) for n in ba])
        # Set last k-1 bytes to k for padding where k = len(decoded) + 1
        for n, d in enumerate(decoded[::-1]):
            ba[-(n + 1)] = (d ^ (n + 1)) ^ (len(decoded) + 1)

        # Set byte we are enumerating to find correct padding for n with
        ba[-(len(decoded) + 1)] = i

        # print([int(n) for n in ba])

        new_frame = frame_replace_block(bidx, ba)

        padding_pass = frame_passes_padding(new_frame, i)
        if padding_pass:
            # If this is the last byte, confirm it is 0x01
            # by altering the second last byte of last_block
            if len(decoded) == 0:
                print(f"Confirming byte {i:03d} for block {bidx:1d}")
                ba[-2] = ba[-2] ^ 0xFF
                confirm_frame = frame_replace_block(bidx, ba)
                padding_pass = frame_passes_padding(confirm_frame, i)
                if padding_pass:
                    print("Correct byte!")
                    return i
                else:
                    print(f"Padding not correct! Continuing")
                    continue
            else:
                return i


def bruteforce_block(bidx, last_block, decoded):
    while len(decoded) < 16:
        print(f"Decoded: {decoded}")
        sleep(1)
        res = next_block_byte(bidx, last_block, decoded)

        if res is None:
            print("Error in algorithm!! Could not find next byte in block")
            break

        decoded.insert(0, res)


# ch4 nosub
# decrypted_blocks = [b'v\xab\xbf\xd6V\xf8\x06\x009dea0225', b'43d783a1^ flag ^', b'0006f856d6bfab76', b'^ time ^cb329be6', b'628eb9e4\x08\x08\x08\x08\x08\x08\x08\x08']
decrypted_blocks = []


def find_blocks():
    logger.disable("ectf25")
    # n is the block we are finding by altering n-1
    for n in range(4, -1, -1):
        decoded = []
        if n == 0:
            last_block = iv
        else:
            last_block = blocks[n - 1]
        bruteforce_block(n - 1, last_block, decoded)

        decrypted_block = [
            last_block[-(i + 1)] ^ decoded[-(i + 1)] ^ (i + 1) for i in range(16)
        ]
        dbytes = bytes(decrypted_block[::-1])

        decrypted_blocks.insert(0, dbytes)

    return (b"").join(decrypted_blocks)


breakpoint()
