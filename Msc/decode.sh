#!/bin/bash

#echo "Hello what is your number? "
#read tim dat
echo "Provide TIME to be decoded"
read tim
echo "Provide DATE to be decoded"
read dat
echo " "
big1=$(echo $tim | tac -rs .. | echo "$(tr -d '\n')")
big2=$(echo $dat | tac -rs .. | echo "$(tr -d '\n')")
echo "Big-endian numbers for time and date are: " $big1 $big2

#binary=$(echo "obase=2; ibase=16; $big" | bc )
binary1=$(python -c "print ''.join([bin(int(i, 16))[2:].zfill(4) for i in '$big1'])")
binary2=$(python -c "print ''.join([bin(int(i, 16))[2:].zfill(4) for i in '$big2'])")
echo "Binary numbers for time and date are: " $binary1 $binary2
#echo "Binary for time is: " $binary2

decimal1=$(echo "$((0x$big1))")
decimal2=$(echo "$((0x$big2))")

echo "Decimals are: $decimal1 $decimal2"

t_hours=$( echo $binary1 | cut -c1-5 ) 
t_mins=$( echo $binary1 | cut -c6-11 )
t_secs=$( echo $binary1 | cut -c12-16 )

d_year=$( echo $binary2 | cut -c1-7 )
d_mon=$( echo $binary2 | cut -c8-11 )
d_day=$( echo $binary2 | cut -c12-16 )

hour=$( echo "$((2#$t_hours))" )
min=$( echo "$((2#$t_mins))" )
sec=$( echo "$((2#$t_secs))" )
secs=$(( sec*2 ))

dos=1980
year_r=$( echo "$((2#$d_year))" )
year=$(( $year_r + $dos )) 
mon=$( echo "$((2#$d_mon))" )
day=$( echo "$((2#$d_day))" )
echo " "
echo "Converted time: $hour:$min:$secs"
echo "Converted date: $day/$mon/$year"
echo " "
