#!/bin/bash


IFS='
'

info=''

tmp=`pwd`
domain=${tmp##*/}


#Create Key.

openssl genrsa -out  ${domain}.key 2048 -sha256

sleep 2


if [ -e info.dat ]; then

    for x in  `cat info.dat`
    do
      info="/${x}${info}"
    done

    openssl req -out   ${domain}.csr -key ${domain}.key -sha256  -new -subj "${info}/CN=${domain}"

else

    openssl req -out   ${domain}.csr -key ${domain}.key -sha256  -new

fi



#openssl req -out   ${domain}.csr -key ${domain}.key -sha256  -new
#openssl req -out   ${domain}.csr -key ${domain}.key -sha256  -new -subj "/C=JP/ST=/CN=${domain}"

echo "## check match ##"

openssl  req  -noout -modulus -in ${domain}.csr  | openssl md5
openssl  rsa -noout -modulus -in  ${domain}.key  | openssl md5
openssl  req  -in  ${domain}.csr  -noout -text
