#!/bin/bash
name=${1::-2}
gcc -g $1 -o ./outputs/$name
./outputs/${name}.exe