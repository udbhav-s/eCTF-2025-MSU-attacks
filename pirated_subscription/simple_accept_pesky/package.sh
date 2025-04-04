#!/bin/bash

# $1: Team name
# $2: Path to team design

set -eo pipefail

rm -f frames.json
rm -f "pesky_ngm_$1.zip"
rm -f pirated.sub

cp $2/pirated.sub pirated.sub

python3 get_frames.py -t "$1"

zip -r "pesky_pirated_$1.zip" pesky_neighbor.py setup.sh frames.json pirated.sub