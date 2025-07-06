import os # will be used to scan files, folders
import shutil #Will be used to move files alround
import platform #Determines your platforms

#A function to get all the folders avoiding all the hidden files/Folders
def getting_folders(move, all_folders, temp_path_os_list_dir):
    for item in temp_path_os_list_dir:    
        if os.path.isdir(temp_path + move + item) and item.startswith(".") == False:
            all_folders.append(item)
    return all_folders

#A function to remove all the hidden folders ##hidden files typicall start with . so if thet are starting with . then we can make a conditonal checking if the file starts with a . then we remove it
def getting_files(path,file_folder):
    file_folder = os.listdir(path)
    for file in file_folder:
        if file.startswith("."): 
            file_folder.remove(file)
    return file_folder

def filter(banned,file,filtered_file,):
    for f in file:
        if f not in banned:
            filtered_file.append(f)
    return filtered_file
            

if __name__ == "__main__":
    
    print("\nHello user, today we will be organzing your files. I will pull out a list of all the users in this device")
    
    #Determines the path based on the system in your computer
    windows_path = "C:\\Users"
    linux_mac_path = "/Users"
    back_slash = "\\"
    forward_slash = "/"
    
    move = back_slash if platform.system() == "Windows" else forward_slash
    path = windows_path if platform.system() == "Windows" else linux_mac_path
    
    banned = [
    # Windows-specific hidden/system folders
    "Cookies", "Local Settings", "PrintHood", "Recent", "Searches",
    "SendTo", "AppData", "Application Data", "NetHood", "Start Menu",
    "NTUSER.DAT", "NTUSER.DAT.LOG1", "NTUSER.DAT.LOG2", "thumbs.db",
    "desktop.ini", "$Recycle.Bin", "System Volume Information","All Users","Default User","desktop.ini"

    # macOS-specific (non-dot) system folders
    "TemporaryItems", "VolumeIcon.icns",

    # Linux/UNIX (non-dot) folders — mostly excluded unless explicitly named
    "Trash"]
    
    user_folder = os.listdir(path)#gets all client user folders in the c drive
    
    filtered_file = []
    filter(banned,user_folder,filtered_file)
    
    list_user_folder = "\n".join(f"{i}. {pair}" for i, pair in enumerate(filtered_file)) #organinizes the folders with there corresponding number call
    
    while True:
        try:
            command = int(input(f"\nHere is the list, please choose one with its corresponding number to keep going:\n\n{list_user_folder}\n"))
            if filtered_file[command] in filtered_file:
                break
            
        except IndexError:
            print("\nThat value is out of range. Please try again.\n")
            True
            
        except ValueError:
            print("\nInvalid input. Please enter a valid number to continue.")
            True
            
    print("\nYour choice is valid. Let's continue.\n")
    
    #move into the next folder
    temp_path = path + move + filtered_file[command]
    #list all information in this path
    all_info = os.listdir(temp_path)
    
    #we are getting all the folders in this directory and removing any hidden files 
    all_folders = []
    getting_folders(move,all_folders,all_info)
    filtered_folders = []
    filter(banned,all_folders,filtered_folders)
    
    
    #checking
    print(filtered_folders)
            

        
    
    
    
    
    
    

    





