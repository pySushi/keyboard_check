from ctypes import * 
from _winreg import * 


# Return keyboard layout hex code after detecting the layout
def getKeyboardType():
	win =  windll.user32.GetForegroundWindow() 
	tid = windll.user32.GetWindowThreadProcessId(win, 0) 
	kbd = hex(windll.user32.GetKeyboardLayout(tid))
	return kbd
