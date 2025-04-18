ch3_frame = {"channel": 3, "timestamp": 2047018172095339, "encoded": "f0f38a7176b7a1f0bc253c69c5baab357e24c90b83bb96619915b05a899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9d75c2324a402ee3c1e85291d8e3eeb528cba5705e8b89a4bcef525c0dce15ca9d22fb23277e2d8ac48bc"}
ch4_frame = {"channel": 4, "timestamp": 2047018172095396, "encoded": "f7f38a71b9b7a1f0bc253c699eb8a0322d20980b80ef943f9a40b101899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9800a2324a402ee3c1e857749863dbe588aef5101b3ea9817cff0c0a2c5cf1c17c43574972d081cf66030"}
ch1_frame = {"channel": 1, "timestamp": 2047018172095064, "encoded": "f2f38a7145b6a1f0bc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a1125fa0a5f282cad4062324a402ee3c1e852e49da6ebb0e82ba0752b8ed9f4b94f0ff842d5fffea96bfaa5c3248705b1dd2"}
ch2_frame = {"channel": 2, "timestamp": 2047018172095273, "encoded": "f1f38a7134b7a1f0bc253c69c9eda83c79769a5987ea95609a45b053899697d4b6e1b631092ca31f6ad7a1125fa0a5f282c9d3072324a402ee3c1e85761bd93aec5cdfe8540eb9eb9d1bc7f47794509f853423017ad8a10b645722cf"}
ch0_frame = {"channel": 0, "timestamp": 2047018173619389, "encoded": "f3f38a71a0f048f1bc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a1125fa3f2a286c8835a2324a402ee3c1e85794ddc6bb95bd8ed0050bae49f1cc2f1f44acc515c75d227c691d3bbc0215610"}

_ch3_frame = {"channel": 3, "timestamp": 2047019092496728, "encoded": "f0f38a7145fd85bbbc253c69c5baab357e24c90b83bb96619915b05a899697d4b6e1b631092ca31f6ad7a11204f0a7f6869ad4062324a402ee3c1e852b1a8a30e85d89e95157b9e5cc1cc5f9060e3ab0a37c9ce95eb96c91b9e338e1"}
_ch2_frame = {"channel": 2, "timestamp": 2047019092496651, "encoded": "f1f38a7116fd85bbbc253c69c9eda83c79769a5987ea95609a45b053899697d4b6e1b631092ca31f6ad7a11204f0a7f6869ad15c2324a402ee3c1e85784f893db30cdfbd0557edbece1f91f64068665a0066680dc4f9185a741ee89c"}
_ch1_frame = {"channel": 1, "timestamp": 2047019092496404, "encoded": "f2f38a7109fc85bbbc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a11204f0a7f6869bd00a2324a402ee3c1e857f48893eef0e8fbd5406babcce4a94f6a2a2c6f061aaef6df308d1c641df7fbe"}
_ch4_frame = {"channel": 4, "timestamp": 2047019092496787, "encoded": "f7f38a718efd85bbbc253c699eb8a0322d20980b80ef943f9a40b101899697d4b6e1b631092ca31f6ad7a11204f0a7f6869ad80d2324a402ee3c1e852a48da69bf0c8dea5005bfbf9d4a93a4debb0572395f724b63888cdf9d431b55"}
_ch0_frame = {"channel": 0, "timestamp": 2047019093704056, "encoded": "f3f38a716511b3bbbc253c6992e3fe692d709354c0b7c82a9f1be40c899697d4b6e1b631092ca31f6ad7a11204f0a6f0d1cfd6062324a402ee3c1e852c1c8e69b95e82eb5005bcb9cb4fcef7ebf0432a009c6be85ea911b03d3b5ea9"}

def xor(a, b):
    """XOR two byte strings of equal length"""
    return bytes(x ^ y for x, y in zip(a, b))

def xor_frames(frame1, frame2):
    """XOR two frames"""
    # XOR the encoded values
    xor_encoded = xor(bytes.fromhex(frame1["encoded"]), bytes.fromhex(frame2["encoded"]))
    
    return xor_encoded

for i in range(5):
    xor_result = xor_frames(globals()[f"ch{i}_frame"], globals()[f"_ch{0}_frame"])
    # print(f"XOR result: {xor_result}")
    b = b'\0'*12+b'noflagonthischan' #^ flag ^00054ff44c9b8490^ time ^5b9f55c38fec62bb\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xdcP\xc9\xcf\xcd\xad\x88\x0e\xaa\xf6='\xe9\x8fC5\x0cY\xceZ\x9a\xb3\t\xa3H\x962 $\xccn2\x8a\x16_P\xe4\xf4b\xd9J\x9cm\xe7\xd8\xce\x8fV\x90\x82\xb9N\xd9\x19\xb3aT\xd9\\\x9b\x82Z\x86\r"
    xor_result = xor(b, xor_result)[-16:]
    print(i, xor_result)
    print()

recorded = {"timestamp": 105696366422543, "encoded": "f2f38a71124601245d003b699ab5a03c2d74ce02d6ef93619a15e451899697d4b6e1b631092ca31868d2f01352a4f6f2d6cad1582324a402ee3c1e852d4d886deb0fd9e80357b2e89919cef76f2fff5df38b2ea7335e62ae1943e5e1"}
print(f'ectf{{recording_{xor(xor_frames(globals()[f"ch0_frame"], recorded), b'\0'*12+b'noflagonthischan')[-16:].decode()}}}')