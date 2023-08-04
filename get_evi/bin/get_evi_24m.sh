# /bin/bash

rm -rf ./evi/*
aws-vault exec aisin-dev-24mm -- python3 get_evi_all.py
