#!/bin/bash

export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/include
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib

g++ -std=c++17  -o main main.cpp   -llept -ltesseract

export TESSDATA_PREFIX=./tessdata/old/

./main > Arial-patterns.txt

diff -u  Arial-patterns.txt  Arial-gt.txt