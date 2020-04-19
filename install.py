import sys
import re
import Framework.ui.Convert_to_EXE as WinInstall

def Func():
    
    if re.search("^win",sys.platform):
        WinInstall.Func()

        
    else:
        pass


if __name__ == "__main__":
    Func()
