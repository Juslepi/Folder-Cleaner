import os
import shutil
import json

settings_json = open('files.json')
settings = json.load(settings_json)

folder_path = os.path.realpath(settings["source"])
target_files = settings["target"]

files = os.listdir(folder_path)


for file in files:
    filename, extension = os.path.splitext(file)
    current_file = os.path.join(folder_path, filename + extension)
    
    for target in target_files:
        # Compare current file extension without dot
        if extension.split(".")[-1].lower() in target["extensions"]:
            if not os.path.isdir(target["destination"]): os.mkdir(target["destination"])
            try:
                shutil.move(current_file, os.path.realpath(target["destination"]))
                print(filename + extension, "moved to", target["destination"])
            except(shutil.Error):
                print(filename + extension, "already exists in destination folder.")

input("Press Enter...")