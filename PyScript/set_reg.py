import winreg

# sub_key's path in HKEY_CURRENT_USER
reg_path=r"Software"
# sub_key's name
reg_name="Tom"
# sub_key's data
reg_value="123"


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
        set_reg_env(reg_name,reg_value)    
    winreg.CloseKey(reg_handler)
