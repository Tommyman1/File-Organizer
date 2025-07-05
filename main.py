import os # will be used to scan files, folders
import shutil #Will be used to move files alround
import platform

if __name__ == "__main__":
    
    print("\nHello user, today we will be organzing your files. I will pull out a list of all the users in this device")
    
    #Determines the path based on the system in your computer
    windows_path = "C:\\Users"
    linux_mac_path = "//Users"
    path = windows_path if platform.system() == "Windows" else linux_mac_path
    
    user_folder = os.listdir(path)#gets all client user folders in the c drive
    
    user_folder.remove("All Users")#Hidden in folder
    user_folder.remove("Default User")#Hidden in folder
    user_folder.remove("desktop.ini")#Hidden in folder
    
    list_user_folder = "\n".join(f"{i}. {pair}" for i, pair in enumerate(user_folder)) #organinizes the folders with there corresponding number call
    
    while True:
        try:
            command = int(input(f"\nHere is the list please choose one with its corresponding number to keep going:\n\n{list_user_folder}\n"))
            if user_folder[command] in user_folder:
                break
            
        except IndexError:
            print("\nThat value is out of range. Please try again.\n")
            True
            
        except ValueError:
            print("\nInvalid input. Please enter a valid number to continue.")
            True
            
    print("\nYour choice is valid. Let's continue.\n")
        

        
    
    
    
    
    
    

    





