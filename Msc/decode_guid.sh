#!/bin/bash
# Yannis Folias 17/12/2018
# Decode GUIDs 

echo "Provide first 4 bytes"
read first 
echo "Provide next 2 bytes"
read second
echo "Provide next 2 bytes"
read third
echo "Provide next 2 bytes"
read fourth
echo "Provide next 6 bytes"
read last


num1=$(echo $first | tac -rs .. | echo "$(tr -d '\n')")
num2=$(echo $second | tac -rs .. | echo "$(tr -d '\n')")
num3=$(echo $third | tac -rs .. | echo "$(tr -d '\n')")

echo "The decoded guid is: $num1-$num2-$num3-$fourth-$last"

