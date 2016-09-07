#!/bin/bash

tmp=`pwd`
domain=${tmp##*/}

openssl verify -verbose -CAfile  ca_bundle.crt  ${domain}.crt
