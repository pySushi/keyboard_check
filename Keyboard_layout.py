from ctypes import * 
from _winreg import * 

import layouts

# Return keyboard layout hex code for the application in the foreground
def getKeyboardType():
	win =  windll.user32.GetForegroundWindow() 
	tid = windll.user32.GetWindowThreadProcessId(win, 0) 
	kbd = hex(windll.user32.GetKeyboardLayout(tid))
	return kbd
