import os
import shutil

folder_path = os.path.realpath("C:/Users/Jussi/Downloads")
files = os.listdir(folder_path)

# Files to be affected
guitarPro = {
    "destination" : os.path.realpath("C:/Users/Jussi/Documents/Tabs/moved-tabs"),
    "extensions" : ["gpx","gp2","gp3","gp4","gp5","gp6","gp7"]
}

for file in files:
    filename, extension = os.path.splitext(file)
    current_file = os.path.join(folder_path, filename + extension)
    destination = guitarPro["destination"]

    if extension.split(".")[1] in guitarPro["extensions"]:
        shutil.move(current_file, destination)
        print(f"{current_file} to", destination)
