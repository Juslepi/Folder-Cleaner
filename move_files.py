import os
import shutil
import json

folder_path = os.path.realpath("C:/Users/Jussi/Downloads")
files = os.listdir(folder_path)

settings_json = open('files.json')
target_files = json.load(settings_json)

for file in files:
    filename, extension = os.path.splitext(file)
    current_file = os.path.join(folder_path, filename + extension)
    
    for target in target_files:
        # Compare current file extension without dot
        if extension.split(".")[-1].lower() in target["extensions"]:
            if not os.path.isdir(target["destination"]): os.mkdir(target["destination"])
            try:
                shutil.move(current_file, os.path.realpath(target["destination"]))
                print(filename, extension, "moved to", target["destination"])
            except(shutil.Error):
                print(filename, extension, "already exists in destination folder.")
