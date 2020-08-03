#!/usr/bin/python
import os
import sys

os.system("lsusb > out.txt")

with open("out.txt") as fp:
	line = fp.readline()
	cnt = 1
   	while line:
    		if (line[83:89] == "Gadget"): dev = line[15:18]
       		line = fp.readline()
       		cnt += 1

os.system("rm out.txt")
os.system("sudo ~/bin/reset_usb.py -d " + dev)