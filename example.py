#!/usr/bin/env python
import os,glob,subprocess,errno,sys
# Enter device MAC addresses (lowercase) to watch
myKids = {'8c:a9:82:ba:1b:fa': 'Lenovo',
'24:24:e:57:ae:d2': 'ipad-mini'}
present_files = []
allDevices = []
device = {}

# Remove previously present devices
list_of_files = os.listdir("/tmp")
for ifile in list_of_files:
	if ifile.endswith(".present"):
		os.remove(os.path.join("/tmp", ifile))

# Execute arp command to find all currently known devices
proc = subprocess.Popen('arp -a | cut -d" " -f1,4', shell=True, stdout=subprocess.PIPE)

# Build array of dictionary entries for all devices found
for line in proc.stdout:
	item = line.split()
	device["Name"] = item[0]
	device["MAC"] = item[1]
	allDevices.append(device.copy())

# Wait for subprocess to exit
proc.wait()

# Search Array of Dictionaries for items in myKids
# Print name of device if found
for kid in myKids.iterkeys():
	for device in allDevices:
		if device.get('MAC') == kid:
			filename = "./" + myKids.get(kid) + ".present"
			f = open(filename,'w')
			f.close()

# Exit code based on success of original subprocess
sys.exit(proc.returncode)