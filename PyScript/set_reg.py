import winreg

reg_path=r"Software\perforce\environment"

def set_reg_env(name,value):
    winreg.SetValueEx(reg_handler,f"{name}",0,winreg.REG_SZ,f"{value}")

def isexisted_reg_env(): 
    try:       
        winreg.EnumValue(reg_handler,0)
        return True
    except OSError as e:
        # print(e)
        return False          
            
if __name__ == "__main__" :
    reg_handler=winreg.OpenKey(winreg.HKEY_CURRENT_USER,reg_path,0,winreg.KEY_ALL_ACCESS)
    if isexisted_reg_env():
        print("reg_variables are existed.")
    else:
        print("Cann't find reg_variables!But it's created now")
        set_reg_env("Tom","123")    
    winreg.CloseKey(reg_handler)
