#!/usr/bin/python
def display_dircontent(sPath):
	import os
	for sChild in os.listdir(sPath):
		sChildPath=os.path.join(sPath,sChild)
		if os.path.isdir(sChildPath):
			display_dircontent(sChildPath)
		else:
			print sChildPath
display_dircontent('/root/python')
	
	
