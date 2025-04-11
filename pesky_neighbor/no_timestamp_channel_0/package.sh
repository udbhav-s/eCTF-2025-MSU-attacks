#!/bin/bash

set -eo pipefail

rm -f frames.json
rm -f *.zip

python3 get_frames.py -t "$1"

zip -r "pesky_ngm_$1.zip" pesky_neighbor.py setup.sh frames.json