#!/bin/bash
# Yannis Folias 16/12/2018
# Ntfs timestamps 

echo "Provide TIMESTAMP to be decoded"
read timestamp

echo " "
big=$(echo $timestamp | tac -rs .. | echo "$(tr -d '\n')")
echo "Big-endian for timestamp is: " $big


binary1=$(python -c "print ''.join([bin(int(i, 16))[2:].zfill(4) for i in '$big'])")

echo "Binary is: $binary1"

decimal=$(echo "$((0x$big))")
echo "Decimal is: $decimal"

echo " "
offset=$((134774*24*60*60))
unixTimestamp=$((decimal/10000000-offset))
date -d @$unixTimestamp
echo " "
