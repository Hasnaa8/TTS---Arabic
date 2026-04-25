#!/bin/sh
INPUT_TEXT="$1"
python3 test.py	"$INPUT_TEXT"
mbrola -v 20 voices/ar1 output_file.pho audio.wav
play audio.wav
