import os # will be used to scan files, folders
import shutil #Will be used to move files alround
import platform #Determines your platforms

#A function to get all the folders avoiding all the hidden files/Folders
def getting_folders(temp_path, all_folders, pathinfo):
    for item in pathinfo:    
        if os.path.isdir(os.path.join(temp_path,item)) and not item.startswith("."):
            all_folders.append(item)
    return all_folders

#A function to remove all the hidden folders ##hidden files typicall start with . so if thet are starting with . then we can make a conditonal checking if the file starts with a . then we remove it
def getting_files(path,files):
    file_folder = os.listdir(path)
    for file in file_folder:
        if not file.startswith("."): 
            files.append(file)
    return files

def filter(banned,file,filtered_file,):
    for f in file:
        if f not in banned:
            filtered_file.append(f)
    return filtered_file

def getting_filenames(title):
    index = title.rfind(".") + 1
    word = ""
    while index < len(title):
        word += title[index]
        index += 1
    return word
        
        
            

if __name__ == "__main__":
    
    print("\nHello user, today we will be organzing your files. I will pull out a list of all the users in this device")
    
    #Determines the path based on the system in your computer
    windows_path = "C:\\Users"
    linux_mac_path = "/Users"
    
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
    temp_path = os.path.join(path,filtered_file[command])
    
    #list all information in this path
    all_info = os.listdir(temp_path)
    
    #we are getting all the folders in this directory and removing any hidden files 
    all_folders_in_this_directory = []
    getting_folders(temp_path,all_folders_in_this_directory,all_info)
    filtered_folders = []
    filter(banned,all_folders_in_this_directory,filtered_folders)
    
    #we basically got to ask the user to pick which folder to organize again inside the other folder
    list_user_folder2 = "\n".join(f"{i}. {pair}" for i, pair in enumerate(filtered_folders)) #organinizes the folders with there corresponding number call inside another directory
    
    while True:
        try:
            command2 = int(input(f"Here is the list, please choose one with its corresponding number to organize:\n\n{list_user_folder2}\n"))
            if filtered_folders[command2] in filtered_folders:
                break
            
        except IndexError:
            print("\nThat value is out of range. Please try again.\n")
            True
            
        except ValueError:
            print("\nInvalid input. Please enter a valid number to continue.")
            True
            
    print("\nYour choice is valid. Let's continue.\n")
    
    #We are going to do a final scan in the final scan for folders
    
    temp_path2 = os.path.join(temp_path,filtered_folders[command2])

    
    final_folders_unorganized = os.listdir(temp_path2)
    final_folders = []
    getting_folders(temp_path2, final_folders, final_folders_unorganized)
    
    #final files all the files in this directory
    final_files = []
    getting_files(temp_path2,final_files)
    
    #filtered_folders has all the folders 1st layer temp1 #final_folders has the 2st layer folder temp2
    total_folders = filtered_folders + final_folders
    os.makedirs(
        os.path.join(temp_path,"Other_Folders"),
        exist_ok=True)
    
    for item in final_folders:
        shutil.move(
            os.path.join(temp_path2,item),
            os.path.join(temp_path,"Other_Folders"))

    for file in final_files:
        
        if "." in file and file not in total_folders:
    
            word = getting_filenames(file)
            
            os.makedirs(
                os.path.join(temp_path,word),exist_ok=True)
            
            shutil.move(
                os.path.join(temp_path2, file),
                os.path.join(temp_path, word))
            
        
        elif "." in file and file in total_folders:
            shutil.move(
                os.path.join(temp_path2,file),
                os.path.join(temp_path,file))
            