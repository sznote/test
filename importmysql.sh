#!/bin/bash


for x in  `find -type f -name "*.gz"  | cut -d/ -f 2 | cut -d"." -f1`
do
  if /usr/bin/mysql -u root -p`cat my` $x  > /dev/null 2>&1 </dev/null
  then
      echo "found database: $x "
  else
      /usr/bin/mysql -u root -p`cat my` -e  "CREATE DATABASE  $x  DEFAULT CHARACTER SET ujis"
  fi
       echo "import db: $x"
       gunzip < $x.sql.gz | /usr/bin/mysql -u root -p`cat my` $x


done
