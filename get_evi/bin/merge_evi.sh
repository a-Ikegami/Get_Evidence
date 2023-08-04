# /bin/bash

rm -rf ../merge_evi/evi/*
mv ./evi/* ../merge_evi/evi/
cd ../merge_evi
python3 merge_evi.py
explorer.exe .
