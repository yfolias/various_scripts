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
offset=$((134774*24*60*60)) # number of days from Jan 1, 1601 to Jan 1, 1970, converted to seconds
unixTimestamp=$((decimal/10000000-offset)) # convert 100-nanosecond interval to second, adjust for offset
date -d @$unixTimestamp # display that timestamp
echo " "
