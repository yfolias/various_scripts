#!/bin/bash
# Yannis Folias
# Loading data to mysql from text file
# Code to be extended accordingly

echo $(date -u)
sleep 1
echo "Generating mysql entries"
sleep 1
echo "........................."
sleep 1
table_1=( 1 2 3 4 5 6 7 8 9 10 )

function checkDirs(){
	dir1="mysql_updates/sample1"

  if [ ! -d "$dir1" ]; then
		echo "$dir1 does not exist and will be created"
		mkdir -p $dir1
	fi
}
function creatingData(){
	echo "Creating txt data"
	for i in "${table_1[@]}"; do 

		echo "1	$i	215	100	215" >> mysql_updates/sample1/sample.txt

	done
}

function updateDb(){
	echo "Updating mysql..."
	sleep 1
	echo "Updating sample table"
	mysql -uroot -ppassword db_sample --execute="LOAD DATA LOCAL INFILE '/root/mysql_updates/sample1/sample.txt' INTO TABLE sample;"

}
checkDirs
sleep 1
creatingData
sleep 1
updateDb
echo "Job done!!!"
