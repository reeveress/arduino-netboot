import os
import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description = 'Builds bootloader with the specified MAC address and burns it to Arduino. Make sure Arduino is plugged in with ICSP (In-Circuit Serial Programmer) dongle to Computer with avr-gcc tools',
                                    formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('mac_address', action = 'store', help = 'Specify the MAC address to give Arduino with quotes and curly braces, i.e.{0x00,0x0f,0x0f,0x0f,0x0f,0x0f}')
args= parser.parse_args()

os.system("make clean")
time.sleep(1)
os.system("make bootloader mac=%s"%args.mac_address)
time.sleep(2)
os.system("make upload")
time.sleep(2)
os.system("make fuses")
