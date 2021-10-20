import os
import shutil

folder_path = os.path.realpath("C:/Users/Jussi/Downloads")
files = os.listdir(folder_path)

# Files to be affected
target_files = [
     {  
        "name" : "Guitar Pro",
        "destination" : os.path.realpath("C:/Users/Jussi/Documents/Tabs/moved-tabs"),
        "extensions" : ["gpx","gp2","gp3","gp4","gp5","gp6","gp7"]
    },
    {
        "name": "Images",
        "destination" : os.path.realpath("C:/Users/Jussi/Documents/Tabs/moved-images"),
        "extensions" : ["jpeg", "jpg", "png"]
    }
]


for file in files:
    filename, extension = os.path.splitext(file)
    current_file = os.path.join(folder_path, filename + extension)
    
    for target in target_files:
        # Compare current file extension without dot
        if extension.split(".")[-1].lower() in target["extensions"]:
            if not os.path.isdir(target["destination"]): os.mkdir(target["destination"])
            try:
                shutil.move(current_file, target["destination"])
                print(filename, extension, "moved to", target["destination"])
            except(shutil.Error):
                print(filename, extension, "already exists in destination folder.")



input("Enter to continue...")


# TODO - load target_files from settings.json