# Overview

Execution of a padding oracle attack against a team
This attack exploits a design flaw where there is use of AES in CBC (Cipher Block Chaining) mode with no explicit integrity checks for frames or subscriptions, and the validity of the PKCS#7 padding is checked to verify decrypted contents.

# Running

The script `padding_oracle.py` can be run locally with a connected attacker board from a python in a virtual environment with the host tools installed.  
The `find_blocks` function can be used to find all 80 bytes of encrypted content for a frame in UCF's design.   

# Used against
- UCF