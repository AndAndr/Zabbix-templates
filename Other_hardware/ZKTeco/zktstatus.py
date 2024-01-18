#
#Usage: python zktstatus.py IPaddress
#
from zklib import zklib,zkconst
import sys
import time

if len (sys.argv) != 2:
  sys.exit (1)
zktaddress = sys.argv[1]
zkt = zklib.ZKLib("{}".format (zktaddress), 4370)
if zkt.connect() == True:
  print zkt.serialNumber()
else:
  print ("~CMD_ACK_OK=0")
