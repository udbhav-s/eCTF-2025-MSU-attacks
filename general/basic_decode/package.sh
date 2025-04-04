#!/bin/bash

# $1: Team name
# $2: Path to team design

set -eo pipefail

rm -f frames.json
rm -f *.zip
rm -f *.sub

for sub in $2/*.sub
do
    cp $sub $(basename $sub)
done

python3 ../../utils/dump_frames.py -t "$1" -o frames.json

zip -r "pesky_basic_$1.zip" pesky_neighbor.py setup.sh frames.json *.sub