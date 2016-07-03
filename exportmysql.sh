#!/bin/bash

cat /dev/null > not_found
IFS='
'

for x in `cat listdb.txt`
do

if /usr/bin/mysql -u root -p`cat my` $x  > /dev/null 2>&1 </dev/null
then
  echo  "export $x"
 /usr/bin/mysqldump  -u root -p`cat my`   --single-transaction $x | gzip   > $x.sql.gz
else
     echo $x  >> not_found
fi

done
