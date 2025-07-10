import os # will be used to scan files, folders
import shutil #Will be used to move files alround
import platform #Determines your platforms

#A function to get all the folders avoiding all the hidden files/Folders
def getting_folders(temp_path, all_folders, pathinfo):
    for item in pathinfo:    
        if os.path.isdir(os.path.join(temp_path,item)) and not item.startswith("."):
            all_folders.append(item)
    return all_folders

#A function to pull all the files and not the hidden files
def get_file_name(path,files):
    file_folder = os.listdir(path)
    for file in file_folder:
        if not file.startswith("."): 
            files.append(file)
    return files

#A function filter all the files I do not want accessed from the file returning the filtered file
def filter_banned(banned,file,filtered_file,):
    for f in file:
        if f not in banned:
            filtered_file.append(f)
    return filtered_file

#function that gets the file names by going at the end and getting the name of the frst instance of "." if it dosent we dont do anything to the file
def getting_filenames(title):
    ext = os.path.splitext(title)[-1]
    if ext:
        return ext[1:].lower()
    else:
        return ''
        
#pre determined folders for organization
predefined_folders = {
"images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".pdf"],
"videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
"audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
"documents": [".doc", ".docx", ".odt", ".rtf"],
"spreadsheets": [".xls", ".xlsx", ".ods", ".csv"],
"presentations": [".ppt", ".pptx", ".odp"],
"textfiles": [".txt", ".md"],
"executables": [".exe", ".msi", ".sh", ".bat", ".app"],
"archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
"scripts": [".py", ".js", ".java", ".cpp", ".html", ".css"],
"Other_Folders": []}

banned = [
# Windows-specific hidden/system folders
"Cookies", "Local Settings", "PrintHood", "Recent", "Searches",
"SendTo", "AppData", "Application Data", "NetHood", "Start Menu",
"NTUSER.DAT", "NTUSER.DAT.LOG1", "NTUSER.DAT.LOG2", "thumbs.db",
"desktop.ini", "$Recycle.Bin", "System Volume Information","All Users","Default User",

# macOS-specific (non-dot) system folders
"TemporaryItems", "VolumeIcon.icns",

# Linux/UNIX (non-dot) folders — mostly excluded unless explicitly named
    "Trash"]

#Determines the path based on the system in your computer
windows_path = "C:\\Users"
linux_mac_path = "/Users"

if __name__ == "__main__":
    
    print("\nHello user, today we will be organizing your files. I will pull out a list of all the users in this device")
    
    path = windows_path if platform.system() == "Windows" else linux_mac_path
    
    user_folder = os.listdir(path)#gets all client user folders in the c drive
    
    filtered_file = []
    filter_banned(banned,user_folder,filtered_file)
    
    #organizes the folders with there corresponding number call
    list_user_folder = "\n".join(f"{i}. {pair}" for i, pair in enumerate(filtered_file)) 
    final = 1
    
    #Loops so the user has the option to try and organize a different user folder
    while final != 0:
        
        #ask user which user user folder they want to organize
        while True:
            #error handling
            try:
                command = int(input(f"\nHere is the list, please choose one with its corresponding number to keep going:\n\n{list_user_folder}\n"))
                
                #if user type a value greater then the amount in the folders and it continues to the loop again
                if command >= len(filtered_file):
                    print("\nThat value is out of range. Please try again.\n")
                    continue
                
                #if they type negative one they can simply leave
                if command <= -1:
                    print("\nTo exit, type -1\n")
                    exit()
                #if they type a valid command the while loop breaks    
                else:
                    break
            #if a string is typed instead of getting a value error it will just repeat the while loop and tell them they put an invalid value   
            except ValueError:
                print("\nInvalid input. Please enter a valid number to continue.")
                    
        print("\nYour choice is valid. Let's continue.\n") 
        
        #move into the next folder
        temp_path = os.path.join(path,filtered_file[command])
        
        #list all information in this path
        all_info = os.listdir(temp_path)
        
        #we are getting all the folders in this directory and removing any hidden files 
        all_folders_in_this_directory = []
        getting_folders(temp_path,all_folders_in_this_directory,all_info)
        filtered_folders = []
        filter_banned(banned,all_folders_in_this_directory,filtered_folders)
        
        #we basically got to ask the user to pick which folder to organize again inside the other folder
        list_user_folder2 = "\n".join(f"{i}. {pair}" for i, pair in enumerate(filtered_folders)) 
        
        #if the folder that was chosen does not have anything inside    
        if not filtered_folders:
            print("\nNo subfolders found to organize.\n")
            continue
    
        #ask user which user user folder they want to organize
        while True:
            #error handling
            try:
                command2 = int(input(f"\nHere is the list, please choose one with its corresponding number to keep going:\n\n{list_user_folder2}\n"))
                
                #if user type a value greater then the amount in the folders and it continues to the loop again
                if command2 <= -1:
                    print("\nTo exit, type -1\n")
                    exit()
                
                #if user type a value greater then the amount in the folders and it continues to the loop again    
                elif command2 >= len(filtered_folders):
                    print("\nThat value is out of range. Please try again.\n")
                    
                #if they type a valid command the while loop breaks    
                else:
                    break
            #if a string is typed instead of getting a value error it will just repeat the while loop and tell them they put an invalid value    
            except ValueError:
                print("\nInvalid input. Please enter a valid number to continue.")
                    
        print("\nYour choice is valid. Let's continue.\n")
        
        #We are going to do a final scan in the final scan for folders
        
        temp_path2 = os.path.join(temp_path,filtered_folders[command2])
        
        final_folders_unorganized = os.listdir(temp_path2)
        
        #if the folder that was chosen does not have anything inside    
        if not final_folders_unorganized:
            print("\nNo subfolders found to organize.\n")
            continue
        
        #will store all the folders in final folders using getting folders functions
        final_folders = []
        getting_folders(temp_path2, final_folders, final_folders_unorganized)
        
        #final files all the files in this directory
        final_files = []
        get_file_name(temp_path2,final_files)
        
        #filtered_folders has all the folders 1st layer temp1 #final_folders has the 2st layer folder temp2
        user_selected_folders = filtered_folders + final_folders
    
        #folders inside the pre made ones inside the category folders
        known_extensions = []
        
        #folders pre determined ones
        categorie_key = []
        
        #makes a folder for all the category
        for categories, extension_files in predefined_folders.items():
            os.makedirs(
            os.path.join(temp_path,categories.lower()),
            exist_ok=True)
            
        #moves all the folders in final folders to other folders
        for folder in final_folders:
            try:
                shutil.move(
                os.path.join(temp_path2,folder),
                os.path.join(temp_path,"Other_Folders"))
            except shutil.Error as e:
                print(f"Could not move{os.path.join(temp_path2,folder)} to {os.path.join(temp_path,"Other_Folders")}: {e}")
        
        #adds to categorie key and known_extensions
        for categories, extension_files in predefined_folders.items():
            categorie_key.append(categories)
            for extension in extension_files:
                known_extensions.append(extension.replace(".",""))
        
        #everyfolder we have have
        all_known_folders = set(user_selected_folders + known_extensions + categorie_key)
        
        #adds new files not already in folders into folders as well as creates folders that are not established
        for file in final_files:
            
            #makes files into folders then moves them there
            if "." in file and getting_filenames(file).lower() not in all_known_folders:
                word = getting_filenames(file).lower()
                os.makedirs(os.path.join(temp_path,word),exist_ok=True)
                
                try:
                    shutil.move(os.path.join(temp_path2, file),os.path.join(temp_path, word))
                except shutil.Error as e:
                    count = 0
                    while True:
                        part1,part2 = os.path.splitext(file)
                        count += 1
                        new_file = part1 + "_" + str(count) + part2
                        if os.path.exists(os.path.join(temp_path, word,new_file)) == False:
                            os.rename((os.path.join(temp_path2, file)),(os.path.join(temp_path2, new_file)))
                            shutil.move(os.path.join(temp_path2, new_file),os.path.join(temp_path, word))
                            break
                        else:
                            continue       
                            
                            
            #moves files into the premade folders   
            elif "." in file and getting_filenames(file).lower() in known_extensions:
                target = "." + getting_filenames(file).lower()
                for categorie, extension in predefined_folders.items():
                    if target in extension:
                        word = getting_filenames(file).lower()
                        
                        try:
                            shutil.move(
                            os.path.join(temp_path2,file),
                            os.path.join(temp_path,categorie.lower(),word))
                        except shutil.Error as e:
                            count = 0
                            while True:
                                part1,part2 = os.path.splitext(file)
                                count += 1
                                new_file = part1 + "_" + str(count) + part2
                                
                                if os.path.exists(os.path.join(temp_path, word,new_file)) == False:
                                    os.rename((os.path.join(temp_path2, file)),(os.path.join(temp_path2, new_file)))
                                    shutil.move(os.path.join(temp_path2,new_file),os.path.join(temp_path,categorie.lower()))
                                    break
                                else:
                                    continue       
                            
            #moves folders into other folders                
            else:
                try:
                    shutil.move(os.path.join(temp_path2,file),os.path.join(temp_path, 'Other_Folders'))
                except shutil.Error as e:
                    print(f"Could not move{os.path.join(temp_path2,file)} to {os.path.join(temp_path, 'Other_Folders')}: in {e}")
                          
        #provides an exits and the option to organize a different user folder        
        while True:
            final = int(input("\nWould you like to organize a different folder?\n"
                "0: Exit!\n"
                "1: Choose a different User folder\n"
                "Enter your choice (0, 1): "))
            if final in (0,1):
                break
            else:
                print("\nInvalid input. Please enter a valid number to continue.")
                
        #wipes the data to make sure there nothing in there for the next loop
        all_known_folders.clear()
        known_extensions.clear()
        categorie_key.clear()
        user_selected_folders.clear()
        final_files.clear()
        final_folders.clear()
        all_folders_in_this_directory.clear()
        filtered_folders.clear()
                
    print("Goodbye Have a nice day")    